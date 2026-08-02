# 08_RAG_Pipeline.md

# EquiMind AI

**Retrieval-Augmented Generation (RAG) Pipeline Design**

Version: v0.1.0

Status: Draft

---

# 1. Purpose

This document defines the Retrieval-Augmented Generation (RAG) pipeline used by EquiMind AI.

The objective of the pipeline is to transform raw financial documents into a searchable knowledge base that supports accurate, evidence-backed responses.

Rather than relying solely on the knowledge of a Large Language Model, EquiMind AI retrieves relevant financial information from trusted documents before generating answers.

This approach improves factual accuracy, transparency, and explainability.

---

# 2. Pipeline Overview

```text id="5j3c9m"
Financial Documents
        │
        ▼
Document Ingestion
        │
        ▼
Text Extraction
        │
        ▼
OCR (if required)
        │
        ▼
Text Cleaning
        │
        ▼
Smart Chunking
        │
        ▼
Embedding Generation
        │
        ▼
Qdrant Storage
        │
        ▼
Hybrid Retrieval
(BM25 + Vector Search)
        │
        ▼
Reranking
        │
        ▼
Context Selection
        │
        ▼
Financial Intelligence Layer
        │
        ▼
Prompt Construction
        │
        ▼
Gemini LLM
        │
        ▼
Citation Validation
        │
        ▼
Final Response
```

---

# 3. Stage 1 — Document Ingestion

## Input Sources

The ingestion pipeline accepts publicly available financial information, including:

* Annual Reports (10-K)
* Quarterly Reports (10-Q)
* Earnings Call Transcripts
* Financial Statements
* Financial News
* Company Metadata

The ingestion layer standardizes all incoming data before further processing.

---

# 4. Stage 2 — Text Extraction

The system extracts textual content from each document.

Processing includes:

* PDF parsing
* Metadata extraction
* Page tracking
* Layout preservation where applicable

The extracted text is associated with document metadata for traceability.

---

# 5. Stage 3 — OCR

When documents contain scanned pages or image-based content, OCR is applied.

Responsibilities:

* Detect scanned pages.
* Extract readable text.
* Preserve page references.
* Integrate extracted text into the document.

OCR is executed only when necessary.

---

# 6. Stage 4 — Text Cleaning

Extracted text is normalized before indexing.

Processing includes:

* Remove redundant whitespace.
* Normalize line breaks.
* Remove extraction artifacts.
* Preserve financial terminology.
* Preserve numerical values.

The objective is to improve downstream retrieval quality without altering document meaning.

---

# 7. Stage 5 — Smart Chunking

Large financial documents are divided into manageable chunks.

Objectives:

* Preserve semantic context.
* Avoid splitting important financial information.
* Maintain traceability to original pages.

Each chunk is associated with:

* Company
* Document
* Page number
* Chunk identifier

---

# 8. Stage 6 — Embedding Generation

Each chunk is transformed into a dense vector representation.

The embedding captures semantic meaning while preserving document metadata.

Stored metadata includes:

* Company ticker
* Document ID
* Document type
* Filing date
* Page number
* Chunk ID

Embeddings are stored in Qdrant.

---

# 9. Stage 7 — Knowledge Base

The knowledge base consists of:

## Qdrant

Stores semantic embeddings.

## PostgreSQL

Stores metadata.

## Document Storage

Stores original files.

Together, these systems provide efficient retrieval while maintaining traceability.

---

# 10. Stage 8 — Hybrid Retrieval

When a user submits a query, the retrieval pipeline executes two complementary searches.

## BM25 Search

Optimized for:

* Exact terminology
* Company names
* Financial metrics
* Accounting terminology

## Dense Vector Search

Optimized for:

* Semantic similarity
* Natural language questions
* Conceptual understanding

Results from both searches are merged into a unified candidate set.

---

# 11. Stage 9 — Reranking

Retrieved candidates are reranked according to relevance.

The reranking stage:

* Improves context quality.
* Removes less relevant passages.
* Prioritizes evidence most likely to answer the user's question.

Only the highest-ranked passages continue through the pipeline.

---

# 12. Stage 10 — Context Selection

The pipeline selects the final evidence set.

Selection criteria include:

* Relevance
* Diversity
* Document quality
* Company consistency
* Query coverage

The selected context forms the factual basis of the AI response.

---

# 13. Stage 11 — Financial Intelligence Layer

Before prompting the LLM, the retrieved evidence is processed by the Financial Intelligence Layer.

Responsibilities include:

* Financial metric computation
* Trend analysis
* Qualitative analysis
* Risk extraction

This stage transforms raw evidence into structured financial insights.

---

# 14. Stage 12 — Prompt Construction

A structured prompt is created using:

* Original user query
* Retrieved evidence
* Financial analysis
* Risk analysis
* Citation metadata

The prompt is designed to encourage grounded, evidence-based responses.

---

# 15. Stage 13 — Response Generation

The Gemini LLM synthesizes the supplied information into a coherent answer.

The LLM performs:

* Reasoning
* Explanation
* Summarization
* Natural language generation

The LLM does not retrieve documents or compute financial metrics.

---

# 16. Stage 14 — Citation Validation

Every generated response undergoes citation validation.

Responsibilities:

* Verify supporting evidence.
* Associate page references.
* Remove unsupported claims.
* Compute confidence score.

Only validated responses are returned to the user.

---

# 17. Failure Handling

The pipeline validates each stage before proceeding.

If a stage fails:

* Processing stops.
* The failure is logged.
* A structured error is returned.
* Invalid context is discarded.

This prevents hallucination caused by incomplete or corrupted inputs.

---

# 18. Logging

Each stage records:

* Processing start
* Processing completion
* Execution time
* Number of processed chunks
* Retrieval statistics
* Errors (if any)

These logs support monitoring and future optimization.

---

# 19. Design Principles

The RAG pipeline follows these principles:

* Evidence before generation.
* Retrieval before reasoning.
* Structured analysis before language generation.
* Explainability through citations.
* Modular processing stages.
* Reproducible results.

