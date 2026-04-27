from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

import numpy as np

with open("/Users/Faizanimran/Downloads/rag agent/data.json", "r") as f:
    data = json.load(f)

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 🔥 STEP 1: Extract ONLY chunk texts
chunks_data = data["vector_search_ready"]["chunks"]
texts = [chunk["text"] for chunk in chunks_data]


db_embeddings = model.encode(texts)

print("\n=== DATABASE EMBEDDINGS CREATED ===")
for i, emb in enumerate(db_embeddings):
    print(f"\nChunk {i+1}:")
    print(texts[i])
    print("Embedding (first 10 values):", emb[:10])



def create_chunks(text, chunk_size=120, overlap=40):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i : i + chunk_size])
        chunks.append(chunk)

    return chunks


def process_input(user_input):
    chunks = create_chunks(user_input)

    print("\n--- USER CHUNKS ---")
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}: {chunk}")

    embeddings = model.encode(chunks)

    print("\n--- USER EMBEDDINGS ---")
    for i, emb in enumerate(embeddings):
        print(f"\nEmbedding {i+1} (first 10 values):")
        print(emb[:10])

    return chunks, embeddings


def search_similar(user_input, threshold=0.35, top_k=5):
    _, query_embeddings = process_input(user_input)
    all_scores = cosine_similarity(query_embeddings, db_embeddings)

    # 🔥 best score per DB chunk
    scores = np.max(all_scores, axis=0)

    # 🔥 top K chunks (sirf 1 nahi)
    top_indices = np.argsort(scores)[-top_k:][::-1]

    print("\n=== TOP MATCHES ===")

    selected_chunks = []
    seen = set()

    for i in top_indices:
        score = scores[i]
        print(f"\nScore: {score:.4f}")
        print("Text:", texts[i])

        # 🔥 soft filtering (hard cutoff nahi)
        if score >= threshold:
            chunk = texts[i].strip()

            # 🔥 duplicate remove
            if chunk not in seen:
                selected_chunks.append(chunk)
                seen.add(chunk)

    if not selected_chunks:
        print("❌ No strong match → returning None")
        return None

    print("\n✅ Using multiple chunks")

    # 🔥 IMPORTANT: newline separation
    return "\n\n".join(selected_chunks)
