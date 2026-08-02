# 06_API_Design.md

# EquiMind AI

**API Design**

Version: v0.1.0

Status: Draft

---

# 1. Purpose

This document defines the REST API specification for EquiMind AI.

The API serves as the communication layer between the frontend and backend.

It provides endpoints for:

* Authentication
* Company search
* Document management
* AI-powered financial analysis
* Company comparison
* Report generation
* Chat history

The API follows REST principles and exchanges data using JSON.

---

# 2. API Principles

The API is designed according to the following principles:

* RESTful resource design
* Stateless requests
* Consistent response formats
* Secure authentication
* Predictable error handling
* Versioned endpoints

Base URL

```text
/api/v1
```

---

# 3. Authentication Endpoints

## Register User

**POST**

```text
/api/v1/auth/register
```

Purpose

Create a new user account.

---

## Login

**POST**

```text
/api/v1/auth/login
```

Purpose

Authenticate a user and return a JWT access token.

---

## Current User

**GET**

```text
/api/v1/auth/me
```

Purpose

Retrieve the authenticated user's profile.

---

## Logout

**POST**

```text
/api/v1/auth/logout
```

Purpose

Invalidate the current session.

---

# 4. Company Endpoints

## Search Companies

**GET**

```text
/api/v1/companies/search
```

Purpose

Search companies by name or ticker.

---

## Company Details

**GET**

```text
/api/v1/companies/{ticker}
```

Purpose

Retrieve company profile and metadata.

---

## Company Financial Summary

**GET**

```text
/api/v1/companies/{ticker}/summary
```

Purpose

Return key financial metrics and business overview.

---

# 5. Document Endpoints

## Ingest Company Documents

**POST**

```text
/api/v1/documents/ingest
```

Purpose

Download or process company financial documents.

---

## Document Status

**GET**

```text
/api/v1/documents/status/{company}
```

Purpose

Check ingestion and indexing progress.

---

## List Documents

**GET**

```text
/api/v1/documents/{company}
```

Purpose

Return all indexed documents for a company.

---

# 6. AI Chat Endpoints

## Create Chat Session

**POST**

```text
/api/v1/chat/session
```

Purpose

Start a new AI research session.

---

## Ask Question

**POST**

```text
/api/v1/chat/query
```

Purpose

Submit a natural language financial question.

Example

```json
{
    "company": "NVDA",
    "question": "Summarize NVIDIA's revenue growth over the past three years."
}
```

Response

```json
{
    "answer": "...",
    "confidence": 0.94,
    "citations": [],
    "sources": []
}
```

---

## Conversation History

**GET**

```text
/api/v1/chat/history/{session_id}
```

Purpose

Retrieve previous conversation messages.

---

# 7. Financial Analysis Endpoints

## Financial Ratios

**GET**

```text
/api/v1/financials/{ticker}/ratios
```

Purpose

Return profitability, liquidity, leverage, valuation, and efficiency ratios.

---

## Financial Trends

**GET**

```text
/api/v1/financials/{ticker}/trends
```

Purpose

Return historical growth and trend analysis.

---

## Earnings Summary

**GET**

```text
/api/v1/financials/{ticker}/earnings
```

Purpose

Generate an AI summary of recent earnings reports.

---

## Risk Analysis

**GET**

```text
/api/v1/financials/{ticker}/risks
```

Purpose

Return major company risks extracted from filings.

---

# 8. Company Comparison Endpoints

## Compare Companies

**POST**

```text
/api/v1/compare
```

Purpose

Compare two or more companies across financial and qualitative metrics.

Example

```json
{
    "companies": [
        "AAPL",
        "MSFT",
        "GOOGL"
    ]
}
```

---

# 9. Report Endpoints

## Generate Investment Memo

**POST**

```text
/api/v1/reports/generate
```

Purpose

Generate a structured investment research report.

---

## List Reports

**GET**

```text
/api/v1/reports
```

Purpose

Return previously generated reports.

---

## Retrieve Report

**GET**

```text
/api/v1/reports/{report_id}
```

Purpose

Retrieve a previously generated investment memo.

---

# 10. Health Endpoints

## Health Check

**GET**

```text
/api/v1/health
```

Purpose

Verify backend availability.

---

## Readiness Check

**GET**

```text
/api/v1/ready
```

Purpose

Verify dependent services are operational.

---

# 11. Standard Response Format

Successful responses follow a consistent structure.

```json
{
    "success": true,
    "message": "",
    "data": {}
}
```

---

# 12. Standard Error Format

Errors follow a unified structure.

```json
{
    "success": false,
    "error": {
        "code": "RESOURCE_NOT_FOUND",
        "message": "Requested company does not exist."
    }
}
```

---

# 13. Authentication

Protected endpoints require a valid JWT access token.

Authorization Header

```text
Authorization: Bearer <token>
```

Unauthenticated requests receive an HTTP 401 response.

---

# 14. HTTP Status Codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | Success               |
| 201  | Resource Created      |
| 400  | Invalid Request       |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Resource Not Found    |
| 409  | Conflict              |
| 422  | Validation Error      |
| 500  | Internal Server Error |

---

# 15. Versioning Strategy

All APIs are versioned.

Current Version

```text
/api/v1
```

Future releases may introduce:

```text
/api/v2
```

without breaking existing integrations.

---

# 16. Design Principles

The API follows these principles:

* Predictable endpoint naming.
* Stateless communication.
* Consistent request and response formats.
* Clear separation of resources.
* Secure authentication.
* Backward compatibility through versioning.

