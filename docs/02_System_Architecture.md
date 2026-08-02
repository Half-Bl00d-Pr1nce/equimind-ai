                          USER
                            │
                    React Frontend
                            │
                     FastAPI Backend
                            │
──────────────────────────────────────────────────────────────

                 API / Service Layer

──────────────────────────────────────────────────────────────

                    Query Orchestrator
                      (LangGraph)

                            │
                            ▼

                   Query Rewrite Agent

                            │
                            ▼

                    Retrieval Agent

              ┌─────────────┴─────────────┐
              │                           │
          BM25 Search              Vector Search
              │                           │
              └─────────────┬─────────────┘
                            ▼

                    Reranking Agent

                            ▼

                Financial Metrics Agent

                            ▼

             Qualitative Analysis Agent

                            ▼

                Risk Intelligence Agent

                            ▼

                Report Generation Agent

                            ▼

                 Citation Validation

                            ▼

                     Gemini LLM

                            ▼

                     Final Response

──────────────────────────────────────────────────────────────

                 Persistent Storage Layer

──────────────────────────────────────────────────────────────

 PostgreSQL      Qdrant      Redis      Document Storage

──────────────────────────────────────────────────────────────

                 Data Ingestion Layer

──────────────────────────────────────────────────────────────

 SEC Filings
 Earnings Reports
 Financial Statements
 Earnings Call Transcripts
 Financial News
 PDF Parser
 OCR Pipeline