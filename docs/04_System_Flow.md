# 04_Data_Flow.md

# EquiMind AI

**Data Flow Design**

Version: v0.1.0

Status: Draft

---

# 1. Purpose

This document describes how data flows through EquiMind AI.

It defines the movement of information from ingestion to storage, retrieval, financial analysis, AI reasoning, and response generation.

The objective is to ensure every stage of the system has a clearly defined responsibility, predictable inputs and outputs, and well-defined interactions with adjacent components.

---

# 2. High-Level Data Flow

```
                User Request
                     │
                     ▼
              React Frontend
                     │
                     ▼
              FastAPI Backend
                     │
                     ▼
             Query Orchestrator
                     │
                     ▼
            Query Rewrite Agent
                     │
                     ▼
             Retrieval Pipeline
                     │
        ┌────────────┴────────────┐
        │                         │
   BM25 Search             Vector Search
        │                         │
        └────────────┬────────────┘
                     ▼
              Reranking Agent
                     │
                     ▼
      Financial Intelligence Layer
                     │
        ┌────────────┼────────────┐
        │            │            │
 Financial      Qualitative     Risk
 Metrics         Analysis     Intelligence
        │            │            │
        └────────────┼────────────┘
                     ▼
          Report Generation Agent
                     │
                     ▼
          Citation Validation Layer
                     │
                     ▼
                Gemini LLM
                     │
                     ▼
             Final AI Response
                     │
                     ▼
               React Frontend
```

---

# 3. System Data Lifecycle

The system operates through six sequential stages.

1. Data Ingestion
2. Knowledge Base Construction
3. Query Processing
4. Financial Intelligence
5. AI Response Generation
6. User Presentation

Each stage has clearly defined inputs, outputs, and responsibilities.

---

# 4. Stage 1 — Data Ingestion

## Input

Public financial information including:

* Annual Reports (10-K)
* Quarterly Reports (10-Q)
* Earnings Call Transcripts
* Financial Statements
* Financial News
* Company Metadata

## Processing

* Download documents
* Parse PDF files
* Perform OCR when required
* Extract raw text
* Extract document metadata

## Output

Structured financial documents ready for indexing.

---

# 5. Stage 2 — Knowledge Base Construction

## Input

Structured financial documents.

## Processing

* Clean extracted text
* Intelligent chunking
* Generate embeddings
* Store embeddings in Qdrant
* Generate BM25 index
* Store metadata in PostgreSQL

## Output

Searchable financial knowledge base.

---

# 6. Stage 3 — Query Processing

## Input

Natural language query.

Example:

> Compare NVIDIA and AMD revenue growth over the last three years.

## Processing

* Receive request
* Validate request
* Rewrite query
* Identify companies
* Detect user intent
* Determine required data sources

## Output

Structured query for retrieval.

---

# 7. Stage 4 — Retrieval Pipeline

## Input

Structured query.

## Processing

* Execute BM25 search
* Execute vector search
* Merge retrieved candidates
* Apply reranking
* Select highest-quality context

## Output

Relevant document passages with metadata and citations.

---

# 8. Stage 5 — Financial Intelligence Layer

## Input

Retrieved financial information.

## Processing

### Financial Metrics

* Financial ratio computation
* Growth calculation
* Margin analysis
* Trend identification

### Qualitative Analysis

* Earnings summary
* Management discussion
* Business strategy
* Competitive positioning

### Risk Intelligence

* Risk factor extraction
* Regulatory risks
* Litigation
* Supply chain issues
* Geopolitical exposure

## Output

Structured financial intelligence.

---

# 9. Stage 6 — AI Response Generation

## Input

Financial intelligence.

Retrieved context.

Original user query.

## Processing

* Construct prompt
* Supply retrieved evidence
* Generate grounded response
* Validate citations
* Compute confidence score

## Output

Evidence-backed AI response.

---

# 10. Stage 7 — Presentation Layer

## Input

Validated AI response.

## Processing

Display:

* AI response
* Citations
* Financial metrics
* Charts
* Company information
* Conversation history

## Output

Interactive user experience.

---

# 11. Data Stores

## PostgreSQL

Stores:

* Company metadata
* User information
* Chat history
* Configuration
* Document metadata

---

## Qdrant

Stores:

* Vector embeddings
* Chunk metadata

---

## Redis

Stores:

* Session cache
* Frequently used queries
* Temporary AI context

---

## Document Storage

Stores:

* PDFs
* OCR output
* Parsed documents

---

# 12. External Data Sources

EquiMind AI interacts with external services for financial information.

Sources include:

* Financial filings
* Earnings call transcripts
* Financial news providers
* Company metadata providers

The ingestion layer standardizes all retrieved information before it enters the knowledge base.

---

# 13. Error Handling

Each stage validates its inputs before processing.

If an error occurs:

* Log the failure.
* Return an informative error to the previous layer.
* Prevent propagation of corrupted data.

This ensures the integrity of the overall pipeline.

---

# 14. Logging

Every major event in the pipeline should be logged.

Examples include:

* Document ingestion
* Embedding generation
* Retrieval execution
* AI response generation
* API requests
* Processing failures

Logs support debugging, monitoring, and future performance optimization.

---

# 15. Guiding Principles

The EquiMind AI data flow follows these principles:

* One directional data movement.
* Modular processing stages.
* Clearly defined responsibilities.
* Stateless service interactions where appropriate.
* Reproducible processing.
* Explainable AI outputs.
* Traceable evidence for every generated response.

