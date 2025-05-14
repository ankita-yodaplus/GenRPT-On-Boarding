import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
from pymilvus import connections, Collection, CollectionSchema, FieldSchema, DataType, utility
import numpy as np

# ---------------- Step 1: Connect to Milvus ----------------
connections.connect("default", host="localhost", port="19530")


# ---------------- Step 2: Extract Text from PDF ----------------
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    return " ".join([page.get_text() for page in doc])


# ---------------- Step 3: Improved Chunking (Sliding Window) ----------------
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk.strip())
        start += chunk_size - overlap
    return chunks


# ---------------- Step 4: Create Milvus Collection ----------------
def create_milvus_collection(collection_name, dim):
    if utility.has_collection(collection_name):
        print(f"Collection '{collection_name}' already exists.")
        return Collection(name=collection_name)

    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=dim),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=4096),  # increased length
        FieldSchema(name="source", dtype=DataType.VARCHAR, max_length=1024),  # increased length
    ]
    schema = CollectionSchema(fields, description="PDF text embeddings")
    collection = Collection(name=collection_name, schema=schema)
    collection.create_index("vector", {"index_type": "IVF_FLAT", "metric_type": "COSINE", "params": {"nlist": 128}})
    collection.load()
    return collection


# ---------------- Step 5: Insert Embeddings ----------------
def insert_embeddings(collection, chunks, embeddings, source_name):
    data = [
        [embedding.tolist() for embedding in embeddings],
        chunks,
        [source_name] * len(chunks)
    ]
    collection.insert(data)
    print(f"Inserted {len(chunks)} records into '{collection.name}'.")


# ---------------- Step 6: Semantic Search ----------------
def semantic_search(query_text, model, collection, top_k=5):
    query_vector = model.encode([query_text])[0]
    collection.load()
    search_params = {"metric_type": "COSINE", "params": {"nprobe": 10}}
    results = collection.search(
        data=[query_vector],
        anns_field="vector",
        param=search_params,
        limit=top_k,
        output_fields=["text", "source"]
    )
    for result in results[0]:
        print(f"\nScore: {result.score:.4f}\nText: {result.entity.get('text')}\nSource: {result.entity.get('source')}")


# ---------------- === MAIN EXECUTION === ----------------
if __name__ == "__main__":
    model = SentenceTransformer("all-mpnet-base-v2")

    pdf_path = "IPL_Teams.pdf"
    raw_text = extract_text_from_pdf(pdf_path)
    print("Extracted text length:", len(raw_text))

    chunks = chunk_text(raw_text, chunk_size=500, overlap=50)
    print("Total Chunks:", len(chunks))
    print("First Chunk Preview:", chunks[0][:300])

    embeddings = model.encode(chunks, show_progress_bar=True)

    collection_name = "IPL_collection"
    embedding_dim = len(embeddings[0])
    collection = create_milvus_collection(collection_name, dim=embedding_dim)

    insert_embeddings(collection, chunks, embeddings, source_name=pdf_path)

    print("\n=== Semantic Search Results ===")
    semantic_search("Who replaced Ashish Nehra in the Pune Warriors team in 2011?", model, collection)
