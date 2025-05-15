# search.py
from sentence_transformers import SentenceTransformer
from pymilvus import connections, Collection

# Connect to Milvus
connections.connect("default", host="localhost", port="19530")

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
        print(f"\nScore: {result.score:.4f}")
        print(f"Text: {result.entity.get('text')}")
        print(f"Source: {result.entity.get('source')}")

if __name__ == "__main__":
    collection_name = "IPL_collection"
    query = input("Enter your question: ")

    print("Loading model...")
    # model = SentenceTransformer("all-mpnet-base-v2")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Connecting to existing collection...")
    collection = Collection(name=collection_name)

    print("Running semantic search...")
    semantic_search(query, model, collection)

