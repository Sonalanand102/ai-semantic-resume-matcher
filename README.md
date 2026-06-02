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
