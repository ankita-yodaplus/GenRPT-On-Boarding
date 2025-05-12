import os
import pandas as pd
os.makedirs("output", exist_ok=True)
DATA_PATH = "data/sentences.csv"

df = pd.read_csv(DATA_PATH)
print(f"Loaded {len(df)} rows from {DATA_PATH}")

df.dropna(subset=["text"], inplace=True)
df["text"] = df["text"].str.strip().str.lower()
print(f"After cleaning: {len(df)} rows remain")

import re

def clean_text(s: str) -> str:
    return re.sub(r"[^a-z0-9\s]", "", s)

df["cleaned_text"] = df["text"].apply(clean_text)

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(df["cleaned_text"].tolist(), show_progress_bar=True)

df["embedding"] = embeddings.tolist()
print("Embeddings generated and added to DataFrame.")

OUTPUT_PICKLE = "output/text_embeddings.pkl"
OUTPUT_CSV = "output/text_embeddings.csv"

df.to_pickle(OUTPUT_PICKLE)
df.to_csv(OUTPUT_CSV, index=False)
print(f"Saved processed data to {OUTPUT_PICKLE} and {OUTPUT_CSV}")