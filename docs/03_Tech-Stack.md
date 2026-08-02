# 03_Tech_Stack.md

# EquiMind AI

**Technology Stack & Architectural Decisions**

Version: v0.1.0

Status: Draft

---

# 1. Philosophy

The technology stack for EquiMind AI has been selected based on the following principles:

* Production readiness
* Scalability
* Maintainability
* Community support
* Performance
* Modularity
* Learning value
* Industry adoption

Technologies were selected because they best satisfy the project's technical requirements—not because they are trendy.

---

# 2. System Overview

| Layer               | Technology                 |
| ------------------- | -------------------------- |
| Frontend            | React + TypeScript         |
| Backend             | FastAPI                    |
| AI Orchestration    | LangGraph                  |
| LLM                 | Google Gemini              |
| Embeddings          | BAAI bge-small-en-v1.5     |
| Reranker            | BAAI bge-reranker-base     |
| Vector Database     | Qdrant                     |
| Relational Database | PostgreSQL                 |
| Cache               | Redis                      |
| Search              | BM25 + Dense Vector Search |
| PDF Parsing         | PyMuPDF                    |
| OCR                 | EasyOCR                    |
| Charts              | Plotly                     |
| Authentication      | JWT                        |
| Containerization    | Docker                     |
| Reverse Proxy       | Nginx (Future)             |
| Testing             | Pytest                     |
| RAG Evaluation      | RAGAS + DeepEval           |

---

# 3. Frontend

## React

### Why?

* Industry-standard frontend framework.
* Component-based architecture.
* Large ecosystem.
* Easy integration with FastAPI.
* Excellent state management options.

### Alternatives Considered

* Streamlit
* Next.js
* Vue.js

### Decision

React provides greater flexibility and mirrors the architecture used in production web applications.

---

## TypeScript

### Why?

* Static typing.
* Better IDE support.
* Easier refactoring.
* Improved maintainability.

### Decision

Chosen over JavaScript for better long-term scalability.

---

# 4. Backend

## FastAPI

### Why?

* High performance.
* Automatic OpenAPI documentation.
* Type-safe request validation.
* Native asynchronous support.
* Modern Python ecosystem.

### Alternatives

* Flask
* Django

### Decision

FastAPI is well suited for AI and data-intensive APIs due to its speed and developer experience.

---

# 5. AI Orchestration

## LangGraph

### Why?

* Supports graph-based workflows.
* Enables multi-agent orchestration.
* Maintains explicit execution flow.
* Better suited for complex AI pipelines than linear chains.

### Alternatives

* CrewAI
* AutoGen
* LangChain Chains

### Decision

LangGraph offers greater control over workflow execution and is better aligned with the modular architecture of EquiMind AI.

---

# 6. Large Language Model

## Google Gemini

### Why?

* Strong reasoning capabilities.
* Good support for long-context inputs.
* Accessible API.
* Suitable for document understanding.

### Alternatives

* OpenAI GPT
* Claude
* Llama

### Decision

The LLM is treated as a replaceable component. Business logic remains independent of the model provider.

---

# 7. Embedding Model

## BAAI bge-small-en-v1.5

### Why?

* High retrieval quality.
* Lightweight.
* Fast inference.
* Open-source.

### Alternatives

* OpenAI Embeddings
* E5
* MiniLM

### Decision

Provides a good balance between accuracy, speed, and deployment cost.

---

# 8. Reranker

## BAAI bge-reranker-base

### Why?

* Improves retrieval precision.
* Better document ranking.
* Strong benchmark performance.

### Alternatives

* Cohere Rerank
* CrossEncoder

### Decision

Selected to improve answer quality before LLM generation.

---

# 9. Vector Database

## Qdrant

### Why?

* Production-ready.
* Fast similarity search.
* Metadata filtering.
* Docker support.
* REST and gRPC APIs.

### Alternatives

* ChromaDB
* FAISS
* Pinecone

### Decision

Chosen for scalability, filtering capabilities, and self-hosting support.

---

# 10. Relational Database

## PostgreSQL

### Why?

* ACID compliance.
* Reliable transactions.
* Mature ecosystem.
* Strong SQL support.

### Stores

* Users
* Companies
* Metadata
* Chat history
* Configuration

### Alternatives

* MySQL
* SQLite
* MongoDB

### Decision

PostgreSQL is well suited for structured financial metadata.

---

# 11. Cache

## Redis

### Why?

* Fast in-memory storage.
* Session management.
* Frequently accessed query caching.
* Reduced API latency.

### Decision

Improves responsiveness and reduces repeated computations.

---

# 12. Search

## Hybrid Search

Components:

* BM25
* Dense Vector Search

### Why?

BM25 captures exact keyword matches.

Dense retrieval captures semantic similarity.

Combining both improves retrieval quality.

---

# 13. PDF Parsing

## PyMuPDF

### Why?

* Fast text extraction.
* Layout preservation.
* Metadata extraction.
* Robust PDF support.

---

# 14. OCR

## EasyOCR

### Why?

* Open-source.
* Good multilingual support.
* Easy integration.
* Sufficient accuracy for scanned financial documents.

---

# 15. Financial Visualization

## Plotly

### Why?

* Interactive charts.
* Financial dashboard support.
* Browser-based rendering.
* Easy React integration.

---

# 16. Authentication

## JWT

### Why?

* Stateless authentication.
* Scalable.
* API friendly.

---

# 17. Containerization

## Docker

### Why?

* Environment consistency.
* Simplified deployment.
* Dependency isolation.
* Reproducibility.

---

# 18. Testing

## Pytest

### Why?

* Mature Python testing framework.
* Rich plugin ecosystem.
* Easy integration with CI/CD.

---

# 19. AI Evaluation

## RAGAS

Purpose:

Evaluate retrieval quality, faithfulness, and answer relevance.

## DeepEval

Purpose:

Evaluate LLM outputs and end-to-end AI performance.

---

# 20. Guiding Principles

Every technology in EquiMind AI must satisfy the following:

* Clearly defined responsibility.
* Easy to replace if required.
* Strong community support.
* Production suitability.
* Long-term maintainability.

The architecture is intentionally modular so that individual technologies (e.g., LLMs or embedding models) can be replaced without affecting the overall system design.
