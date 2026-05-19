# 🧠 Semantic RAG Agent-

A context-aware Retrieval-Augmented Generation (RAG) system powered by local LLMs and semantic search.

---

## 🚀 Overview

This project implements a lightweight yet powerful RAG pipeline that enhances LLM responses using relevant contextual data.
It combines embedding-based retrieval with local model inference for efficient and privacy-focused AI.

---

## ⚙️ Features

* 🔍 Semantic search using SentenceTransformers
* 🧩 Intelligent chunking with overlap strategy
* 📊 Cosine similarity-based retrieval (Top-K matches)
* 🧠 Context injection into LLM prompts
* 💻 Local LLM execution via GPT4All (offline capable)

---

## 🏗️ Architecture

```
User Input
   ↓
Chunking
   ↓
Embedding (MiniLM)
   ↓
Cosine Similarity
   ↓
Top-K Context Retrieval
   ↓
Prompt Injection
   ↓
Local LLM (GPT4All)
   ↓
Final Response
```

---

## 📁 Project Structure

```
rag-agent/
│
├── main.py           # Main chat loop + LLM interaction
├── chunks.py         # Chunking + embedding + retrieval logic
├── similarity.py     # Semantic mapping & metadata logic
├── data.json         # Preprocessed knowledge chunks
├── data_set.txt      # Raw dataset
```

---

## ⚡ Setup

```bash
pip install gpt4all sentence-transformers scikit-learn numpy
```

---

## ▶️ Run

```bash
python main.py
```

---

## 🧠 Models Used

* MiniLM (`all-MiniLM-L6-v2`) for embeddings
* GPT4All-supported GGUF models (Mistral / LLaMA)

---

## 📌 Notes

* Large model files (`.gguf`) are not included in the repository
* Designed for local/offline AI workflows
* Optimized for low-resource environments

---

## 👨‍💻 Author

Faizan Imran
AI Engineer | Full Stack Developer

---

## ⭐ Future Improvements

* API deployment (FastAPI / Vercel)
* Streaming responses
* Vector database integration (FAISS / Chroma)
* Multi-document support

---
