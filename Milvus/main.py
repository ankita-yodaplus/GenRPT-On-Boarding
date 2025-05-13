import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
from pymilvus import connections, Collection, CollectionSchema, FieldSchema, DataType, utility
import numpy as np

# Step 1: Connect to Milvus
connections.connect("default", host="localhost", port="19530")

# Step 2: Extract text from PDF
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Step 3: Chunk text into smaller sections
def chunk_text(text, max_length=500):
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""
    for para in paragraphs:
        if len(current_chunk) + len(para) < max_length:
            current_chunk += para + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

# Step 4: Truncate UTF-8 text to avoid oversized entries
def truncate_utf8(text, max_bytes=2048):
    if not text:
        return ""
    encoded = text.encode("utf-8")
    if len(encoded) <= max_bytes:
        return text
    while len(encoded) > max_bytes:
        text = text[:-1]
        encoded = text.encode("utf-8")
    return text

# Step 5: Create collection in Milvus if not exists
def create_milvus_collection(collection_name, dim):
    if utility.has_collection(collection_name):
        print(f"Collection '{collection_name}' already exists.")
        return Collection(name=collection_name)

    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=dim),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=2048),
        FieldSchema(name="source", dtype=DataType.VARCHAR, max_length=512),
    ]
    schema = CollectionSchema(fields, description="PDF text embeddings")
    collection = Collection(name=collection_name, schema=schema)
    collection.create_index("vector", {"index_type": "IVF_FLAT", "metric_type": "COSINE", "params": {"nlist": 128}})
    collection.load()  # Load the collection after creating index
    return collection

# Step 6: Insert data into Milvus
def insert_embeddings(collection, chunks, embeddings, source_name):
    data = [
        [embedding.tolist() for embedding in embeddings],
        [truncate_utf8(chunk) for chunk in chunks],
        [source_name] * len(chunks)
    ]
    collection.insert(data)
    print(f"Inserted {len(chunks)} records into '{collection.name}'.")

# Step 7: Semantic Search
def semantic_search(query_text, model, collection, top_k=5):
    query_vector = model.encode([query_text])[0]
    collection.load()  # Ensure the collection is loaded
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

# === MAIN EXECUTION ===

# Load model
model = SentenceTransformer("all-mpnet-base-v2")

# Extract and chunk PDF
pdf_path = "Supporting Document for Release Process Flow.pdf"
raw_text = extract_text_from_pdf(pdf_path)
chunks = chunk_text(raw_text)
print("Total Chunks:", len(chunks))

# Generate embeddings
embeddings = model.encode(chunks, show_progress_bar=True)

# Prepare Milvus
collection_name = "pdf_collection2"
embedding_dim = len(embeddings[0])
collection = create_milvus_collection(collection_name, dim=embedding_dim)

# Insert into Milvus
insert_embeddings(collection, chunks, embeddings, source_name="Supporting Document for Release Process Flow")

# Semantic Search Example
print("\n=== Semantic Search Results ===")
semantic_search("What is the release process flow?", model, collection)
