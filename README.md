# 🌐 Website RAG Question Answering

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to index any website and ask natural language questions about its content.

Instead of sending the entire webpage to an LLM, the application scrapes the website, converts it into semantic embeddings using Sentence Transformers, stores them in ChromaDB, retrieves only the most relevant information, and generates accurate answers using the Groq API.

---

## 🚀 Features

- 🌍 Index any public website
- 🕷 Scrape website content automatically
- ✂ Chunk text into semantic pieces
- 🧠 Generate embeddings using Sentence Transformers
- 💾 Store embeddings in ChromaDB
- 🔍 Semantic similarity search
- 🤖 Generate answers using Groq Llama 3.1
- ⚡ FastAPI backend
- 🎨 Simple HTML/CSS/JavaScript frontend

---

## 🛠 Tech Stack

### Backend

- FastAPI
- Python

### AI

- Groq API
- Llama 3.1 8B Instant
- Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database

- ChromaDB

### Web Scraping

- Requests
- BeautifulSoup

### Frontend

- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```
Q_A_LLM/

│
├── chroma_db/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── scraper.py
├── db.py
├── rag.py
├── main.py
│
├── requirements.txt
└── README.md
```

---

## ⚙ Workflow

```
Website URL
      │
      ▼
Website Scraper
      │
      ▼
Extract Text
      │
      ▼
Chunk Text
      │
      ▼
Sentence Transformer
      │
      ▼
ChromaDB
      │
Question
      │
      ▼
Similarity Search
      │
      ▼
Relevant Chunks
      │
      ▼
Groq LLM
      │
      ▼
Answer
```

---

## 📦 Installation

Clone the repository

```bash
git clone <repository-url>

cd Q_A_LLM
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env`

```env
GROQ_API_KEY=YOUR_API_KEY
```

---

## ▶ Run

```bash
uvicorn main:app --reload
```

Visit

```
http://127.0.0.1:8000
```

---

## 📷 Demo

### Index Website

- Paste website URL
- Click **Index Website**

### Ask Questions

Example:

```
How do I install FastAPI?
```

```
What are path parameters?
```

```
How does dependency injection work?
```

---

## 📚 What I Learned

- Retrieval Augmented Generation (RAG)
- ChromaDB
- Semantic Search
- Sentence Embeddings
- FastAPI
- REST APIs
- BeautifulSoup
- Website Scraping
- Prompt Engineering
- LLM Integration
- Vector Databases

---

## 🔮 Future Improvements

- Crawl multiple pages automatically
- Better semantic chunking
- PDF support
- Source citations
- Conversation memory
- Streaming responses
- Authentication
- Multi-user support

---

## 👨‍💻 Author

**Pavan Sasank**

Computer Science Engineering Student

Interested in AI • Machine Learning • GenAI • Backend Development