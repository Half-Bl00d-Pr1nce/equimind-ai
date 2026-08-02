# 09_Deployment.md

# EquiMind AI

**Deployment Architecture**

Version: v0.1.0

Status: Draft

---

# 1. Purpose

This document defines the deployment architecture of EquiMind AI.

The deployment strategy ensures that all application components operate as independent services while communicating through well-defined interfaces.

The deployment architecture emphasizes reproducibility, scalability, maintainability, and production readiness.

---

# 2. Deployment Objectives

The deployment architecture is designed to:

* Provide consistent environments across development and production.
* Isolate services using containers.
* Simplify local development.
* Support future cloud deployment.
* Enable horizontal scaling where appropriate.
* Maintain clear separation of responsibilities.

---

# 3. Deployment Overview

```text id="0q8n5j"
                 User
                   │
                   ▼
           React Frontend
                   │
                   ▼
             FastAPI Backend
                   │
      ┌────────────┼────────────┐
      │            │            │
      ▼            ▼            ▼
 PostgreSQL     Qdrant       Redis
      │
      ▼
Document Storage
```

All services are containerized and communicate over an isolated Docker network.

---

# 4. Service Architecture

## Frontend

Responsibilities:

* User interface
* Dashboard
* Authentication
* Charts
* AI chat
* Company comparison

Runs independently from the backend.

---

## Backend

Responsibilities:

* REST API
* Authentication
* AI orchestration
* Financial analysis
* RAG pipeline
* Database interaction

Acts as the central application service.

---

## PostgreSQL

Stores structured application data.

Persistent storage includes:

* Users
* Companies
* Documents
* Chat history
* Reports
* Metadata

---

## Qdrant

Stores vector embeddings.

Responsibilities:

* Semantic retrieval
* Metadata filtering
* Similarity search

---

## Redis

Responsibilities:

* Session storage
* Caching
* Temporary context
* Frequently requested queries

Redis stores only transient data.

---

## Document Storage

Stores:

* Financial reports
* Parsed documents
* OCR output
* Uploaded files

The backend stores references rather than embedding files in the database.

---

# 5. Containerization

Each major service is deployed within its own Docker container.

Containers include:

* frontend
* backend
* postgres
* qdrant
* redis

This separation improves maintainability and fault isolation.

---

# 6. Docker Compose

Docker Compose orchestrates local development.

Responsibilities:

* Build services
* Start services
* Configure networking
* Mount persistent volumes
* Load environment variables

Developers can launch the complete platform using a single command.

---

# 7. Environment Configuration

Configuration is externalized through environment variables.

Examples include:

* Database credentials
* API keys
* JWT secret
* Redis connection
* Qdrant connection
* Application settings

Sensitive information is never hardcoded.

---

# 8. Persistent Volumes

Persistent storage is required for:

PostgreSQL

* Database files

Qdrant

* Vector collections

Document Storage

* Financial documents
* Parsed files

Redis does not require persistent storage for Version 1.0.

---

# 9. Network Design

Containers communicate through a dedicated internal Docker network.

Characteristics:

* Service isolation
* Internal hostname resolution
* Controlled communication
* Reduced external exposure

Only frontend and backend expose public ports.

---

# 10. Logging

Each service maintains independent logs.

Log categories include:

* API requests
* AI pipeline execution
* Database operations
* Retrieval events
* Authentication
* Errors
* Startup events

Logs support debugging and operational monitoring.

---

# 11. Security

Deployment follows these principles:

* Environment variables for secrets.
* No hardcoded credentials.
* Backend-only database access.
* JWT authentication.
* Internal service communication.
* Input validation.

Future enhancements may include HTTPS termination and reverse proxy support.

---

# 12. Scalability

The deployment architecture supports future scaling.

Examples:

Frontend

Multiple frontend instances.

Backend

Multiple API instances behind a load balancer.

Qdrant

Clustered deployment if required.

PostgreSQL

Managed database or replication.

Redis

Distributed cache.

These enhancements are outside the scope of Version 1.0 but are compatible with the current architecture.

---

# 13. Backup Strategy

Regular backups should include:

* PostgreSQL database
* Qdrant vector collections
* Uploaded financial documents

Redis cache is excluded because it stores temporary information.

---

# 14. Disaster Recovery

If a service becomes unavailable:

* Restart the affected container.
* Restore persistent storage if necessary.
* Verify service health.
* Resume normal operation.

Container isolation minimizes the impact of individual service failures.

---

# 15. Health Monitoring

Each service exposes health checks where applicable.

Monitoring includes:

* Backend availability
* Database connectivity
* Vector database availability
* Cache availability

These checks support automated recovery and troubleshooting.

---

# 16. Deployment Principles

The deployment architecture follows these principles:

* Containerized services.
* Independent components.
* Reproducible environments.
* Minimal coupling.
* Secure configuration.
* Persistent storage for critical data.
* Operational simplicity.

