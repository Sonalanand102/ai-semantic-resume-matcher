🚀 Live Demo: https://ai-job-matcher-frontend-yuai.vercel.app

📖 Architecture Overview Included

🐳 Dockerized Deployment

☁️ AWS EC2 Hosted Backend

---

## Demo

### Landing Page

<img width="1470" height="836" alt="Screenshot 2026-05-31 at 5 38 02 AM" src="https://github.com/user-attachments/assets/c4a5e078-07fc-4d4b-9792-af198e6baaf4" />

<img width="1470" height="833" alt="Screenshot 2026-05-31 at 5 38 21 AM" src="https://github.com/user-attachments/assets/3e6ecc98-33b1-4c4a-a51d-bb13383847fe" />

### Processing Pipeline

<img width="1465" height="839" alt="Screenshot 2026-05-31 at 5 42 25 AM" src="https://github.com/user-attachments/assets/6c7ddf3a-1ff9-4f33-993d-d0a30fa6231c" />

### Results Dashboard

<img width="1470" height="827" alt="Screenshot 2026-05-31 at 5 44 00 AM" src="https://github.com/user-attachments/assets/fca55249-4859-4c57-a503-5247c02bd9f2" />

### Architecture Overview

<img width="1470" height="836" alt="Screenshot 2026-05-31 at 5 44 38 AM" src="https://github.com/user-attachments/assets/12c1c76f-6d30-4e2f-b365-ce9218c71c6d" />

<img width="1470" height="831" alt="Screenshot 2026-05-31 at 5 44 51 AM" src="https://github.com/user-attachments/assets/4695f150-cbe3-4233-a586-a74262a37af0" />

---

# AI Semantic Resume Matcher

An AI-powered resume matching platform that recommends relevant jobs using **Semantic Search**, **Hybrid Retrieval**, and **LLM-based Reranking** instead of relying solely on traditional keyword matching.

## Problem Statement

Traditional job portals primarily depend on keyword-based matching. As a result, relevant candidates can be overlooked when their resumes and job descriptions use different terminology to describe similar skills.

This project explores how modern AI retrieval techniques can improve job recommendations by understanding semantic meaning rather than exact keywords.

---

## Features

* Resume Upload & PDF Text Extraction
* Gemini Embeddings Generation
* Vector Similarity Search using pgvector
* Hybrid Retrieval (Semantic Search + Keyword Search)
* Metadata Filtering
* Redis-based Embedding Caching
* LLM-powered Reranking
* Dockerized Deployment
* AWS EC2 Deployment

---

## System Architecture

Resume Upload
→ PDF Extraction
→ Gemini Embeddings
→ Redis Cache
→ Hybrid Retrieval
→ Semantic Search
→ Keyword Search
→ Combined Ranking
→ LLM Reranking
→ Top Job Matches

---

## Tech Stack

### Backend

* FastAPI
* Python
* SQLAlchemy
* Alembic

### AI Layer

* Gemini API
* Embeddings
* Semantic Search
* LLM Reranking

### Data Layer

* PostgreSQL
* pgvector
* Redis

### Deployment

* Docker
* AWS EC2

---

## AI Concepts Implemented

* Embeddings
* Vector Search
* Semantic Search
* Hybrid Retrieval
* Metadata Filtering
* Redis Caching
* LLM Reranking
* Retrieval-Augmented Ranking Concepts

---

## API Endpoints

### Upload Jobs

POST /jobs

Uploads and indexes jobs by generating embeddings and storing them in PostgreSQL.

### Match Resume

POST /match-resume

Uploads a resume and returns ranked job recommendations based on semantic similarity and reranking.

---

## Deployment Architecture

Frontend (Vercel)

↓

Backend (FastAPI on AWS EC2)

↓

PostgreSQL + pgvector

↓

Redis Cache

↓

Gemini API

---

## Future Improvements

* Automated Job Scraping
* Batch Embedding Generation
* Background Workers
* Retrieval Evaluation Metrics
* Advanced Ranking Strategies
* Production Monitoring & Observability

---

## Key Learnings

This project helped me gain hands-on experience with:

* Embeddings
* Vector Databases
* Semantic Search
* Hybrid Retrieval Systems
* LLM-based Reranking
* FastAPI
* Docker
* AWS Deployment

It also provided practical exposure to the retrieval layer that powers many modern AI applications, recommendation systems, and RAG-based architectures.
