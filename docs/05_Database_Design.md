# 05_Database_Design.md

# EquiMind AI

**Database Design**

Version: v0.1.0

Status: Draft

---

# 1. Purpose

This document defines the persistent storage architecture of EquiMind AI.

The system uses multiple storage technologies, each selected for a specific responsibility:

* PostgreSQL for structured relational data
* Qdrant for vector embeddings
* Redis for caching and session management
* Document Storage for raw and processed files

Each storage system has a single responsibility and complements the overall architecture.

---

# 2. Database Overview

| Storage          | Purpose                      |
| ---------------- | ---------------------------- |
| PostgreSQL       | Structured application data  |
| Qdrant           | Vector embeddings            |
| Redis            | Cache and session storage    |
| Document Storage | PDFs and processed documents |

---

# 3. PostgreSQL Schema

PostgreSQL stores all structured and relational data required by the application.

---

## users

Stores registered users.

| Column        | Type               |
| ------------- | ------------------ |
| id            | UUID (Primary Key) |
| full_name     | VARCHAR            |
| email         | VARCHAR (Unique)   |
| password_hash | VARCHAR            |
| role          | VARCHAR            |
| created_at    | TIMESTAMP          |
| updated_at    | TIMESTAMP          |

---

## companies

Stores company metadata.

| Column       | Type               |
| ------------ | ------------------ |
| id           | UUID (Primary Key) |
| ticker       | VARCHAR (Unique)   |
| company_name | VARCHAR            |
| exchange     | VARCHAR            |
| sector       | VARCHAR            |
| industry     | VARCHAR            |
| headquarters | VARCHAR            |
| website      | VARCHAR            |
| created_at   | TIMESTAMP          |
| updated_at   | TIMESTAMP          |

---

## documents

Represents every financial document ingested by the system.

| Column        | Type               |
| ------------- | ------------------ |
| id            | UUID (Primary Key) |
| company_id    | UUID (Foreign Key) |
| document_type | VARCHAR            |
| title         | VARCHAR            |
| source        | VARCHAR            |
| file_path     | TEXT               |
| filing_date   | DATE               |
| uploaded_at   | TIMESTAMP          |

---

## document_chunks

Stores metadata for indexed chunks.

| Column       | Type               |
| ------------ | ------------------ |
| id           | UUID (Primary Key) |
| document_id  | UUID (Foreign Key) |
| chunk_number | INTEGER            |
| page_number  | INTEGER            |
| vector_id    | UUID               |
| created_at   | TIMESTAMP          |

*Note: Chunk text and embeddings are stored in Qdrant. PostgreSQL stores only metadata.*

---

## chat_sessions

Represents a user conversation.

| Column     | Type                         |
| ---------- | ---------------------------- |
| id         | UUID (Primary Key)           |
| user_id    | UUID (Foreign Key)           |
| company_id | UUID (Foreign Key, Nullable) |
| created_at | TIMESTAMP                    |
| updated_at | TIMESTAMP                    |

---

## chat_messages

Stores conversation history.

| Column     | Type               |
| ---------- | ------------------ |
| id         | UUID (Primary Key) |
| session_id | UUID (Foreign Key) |
| sender     | VARCHAR            |
| message    | TEXT               |
| created_at | TIMESTAMP          |

---

## generated_reports

Stores AI-generated investment memos.

| Column         | Type               |
| -------------- | ------------------ |
| id             | UUID (Primary Key) |
| company_id     | UUID (Foreign Key) |
| user_id        | UUID (Foreign Key) |
| report_type    | VARCHAR            |
| report_content | TEXT               |
| generated_at   | TIMESTAMP          |

---

# 4. Entity Relationships

```text
users
   │
   └────── chat_sessions
               │
               └────── chat_messages

companies
   │
   ├────── documents
   │            │
   │            └────── document_chunks
   │
   └────── generated_reports
```

---

# 5. Qdrant Design

Qdrant stores semantic representations of financial documents.

Collection Name:

financial_documents

Each vector record contains:

* Vector embedding
* Chunk text
* Company ticker
* Document ID
* Chunk ID
* Page number
* Document type
* Filing date

This metadata enables efficient filtering during retrieval.

---

# 6. Redis Design

Redis stores temporary and frequently accessed data.

Use Cases:

* User sessions
* Cached retrieval results
* Frequently requested company data
* AI context cache
* Rate limiting (future)

Redis is treated as a volatile storage layer and should never be considered the source of truth.

---

# 7. Document Storage

Stores raw and processed files.

Examples:

* Annual reports
* Quarterly reports
* Earnings call transcripts
* OCR outputs
* Parsed text files

The database stores references to these files rather than the files themselves.

---

# 8. Indexing Strategy

PostgreSQL

Indexes:

* email
* ticker
* company_id
* filing_date
* session_id

Qdrant

Indexes:

* company ticker
* document type
* filing date

Redis

Automatic in-memory indexing.

---

# 9. Data Integrity

The database follows these principles:

* Primary keys on every table.
* Foreign key constraints.
* Unique constraints where applicable.
* Cascading behavior defined explicitly.
* Timestamp tracking for auditing.

These measures ensure consistency and traceability across the application.

---

# 10. Security Considerations

* Passwords are stored only as secure hashes.
* Sensitive credentials remain outside the database.
* Database access is controlled through the backend.
* Direct client access to the database is prohibited.

---

# 11. Backup Strategy

Persistent data should support regular backups.

Critical components include:

* PostgreSQL database
* Qdrant collections
* Uploaded financial documents

Redis is excluded because it stores temporary data.

---

# 12. Scalability

The database design supports future growth by allowing:

* Additional document types
* New report formats
* More companies
* Larger document collections
* Additional AI-generated artifacts

The schema is normalized to reduce redundancy while remaining flexible for future expansion.

---

# 13. Guiding Principles

The storage architecture follows these principles:

* Structured data belongs in PostgreSQL.
* Semantic knowledge belongs in Qdrant.
* Temporary state belongs in Redis.
* Files belong in document storage.
* Every record must be traceable.
* Every relationship must be explicit.
