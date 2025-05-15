# ingest.py
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
from pymilvus import connections, Collection, CollectionSchema, FieldSchema, DataType, utility

# Connect to Milvus
connections.connect("default", host="localhost", port="19530")

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    return " ".join([page.get_text() for page in doc])

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        chunk = text[start:start + chunk_size]
        chunks.append(chunk.strip())
        start += chunk_size - overlap
    return chunks

def create_milvus_collection(collection_name, dim):
    if utility.has_collection(collection_name):
        print(f"Collection '{collection_name}' already exists.")
        return Collection(name=collection_name)

    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=dim),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=4096),
        FieldSchema(name="source", dtype=DataType.VARCHAR, max_length=1024),
    ]
    schema = CollectionSchema(fields, description="PDF text embeddings")
    collection = Collection(name=collection_name, schema=schema)
    collection.create_index("vector", {"index_type": "IVF_FLAT", "metric_type": "COSINE", "params": {"nlist": 128}})
    collection.load()
    return collection

def insert_embeddings(collection, chunks, embeddings, source_name):
    data = [
        [embedding.tolist() for embedding in embeddings],
        chunks,
        [source_name] * len(chunks)
    ]
    collection.insert(data)
    print(f"Inserted {len(chunks)} records into '{collection.name}'.")

if __name__ == "__main__":
    pdf_path = "IPL_Teams.pdf"
    collection_name = "IPL_collection"

    print("Loading model...")
    # model = SentenceTransformer("all-mpnet-base-v2")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Extracting and chunking PDF...")
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text, chunk_size=500, overlap=50)

    print("Generating embeddings...")
    embeddings = model.encode(chunks, show_progress_bar=True)

    print("Creating or loading collection...")
    collection = create_milvus_collection(collection_name, dim=len(embeddings[0]))

    print("Inserting into collection...")
    insert_embeddings(collection, chunks, embeddings, source_name=pdf_path)
