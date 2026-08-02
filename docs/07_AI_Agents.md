# 07_AI_Agents.md

# EquiMind AI

**AI Agent Design**

Version: v0.1.0

Status: Draft

---

# 1. Purpose

This document defines the AI agent architecture of EquiMind AI.

The platform uses a modular multi-agent system where each agent performs a single specialized responsibility.

Rather than allowing a single LLM to solve every problem, the workload is divided into independent agents responsible for retrieval, financial analysis, qualitative reasoning, report generation, and citation validation.

This design improves maintainability, explainability, scalability, and overall system reliability.

---

# 2. Agent Architecture

```text
                 User Query
                      │
                      ▼
             Query Orchestrator
                      │
                      ▼
           Query Rewrite Agent
                      │
                      ▼
             Retrieval Agent
                      │
                      ▼
             Reranking Agent
                      │
                      ▼
      Financial Intelligence Layer
          │         │          │
          │         │          │
 Financial   Qualitative   Risk
 Metrics      Analysis   Intelligence
          │         │          │
          └─────────┴──────────┘
                    │
                    ▼
        Report Generation Agent
                    │
                    ▼
       Citation Validation Agent
                    │
                    ▼
               Gemini LLM
                    │
                    ▼
             Final AI Response
```

---

# 3. Agent Design Principles

Every agent follows the same principles:

* Single responsibility.
* Clearly defined input.
* Clearly defined output.
* Independent implementation.
* No shared business logic.
* Stateless execution.
* Easily testable.

---

# 4. Query Orchestrator

## Responsibility

Coordinates the complete execution pipeline.

The orchestrator determines the order in which agents execute and manages data flow between them.

### Input

User request.

### Output

Final structured response.

The orchestrator never performs financial analysis or retrieval itself.

---

# 5. Query Rewrite Agent

## Responsibility

Improve user queries before retrieval.

Tasks include:

* Clarify vague questions.
* Normalize company names.
* Identify financial terminology.
* Detect user intent.
* Produce retrieval-friendly queries.

### Example

Input

"What about Apple's profits?"

Output

"Summarize Apple's net income and profitability trends using recent annual and quarterly filings."

---

# 6. Retrieval Agent

## Responsibility

Retrieve relevant financial knowledge.

Tasks

* Hybrid search
* Metadata filtering
* Company filtering
* Document selection

The agent returns candidate document chunks without interpretation.

---

# 7. Reranking Agent

## Responsibility

Rank retrieved documents by relevance.

Tasks

* Score retrieved chunks.
* Remove irrelevant context.
* Select highest-quality evidence.

Output

Top-ranked document passages.

---

# 8. Financial Metrics Agent

## Responsibility

Perform quantitative financial analysis.

Tasks

* Revenue growth
* Net income growth
* EPS analysis
* Liquidity ratios
* Profitability ratios
* Leverage ratios
* Valuation ratios
* Margin analysis
* Trend computation

Output

Structured financial metrics.

---

# 9. Qualitative Analysis Agent

## Responsibility

Analyze non-numeric business information.

Tasks

* Management discussion
* Earnings call summaries
* Business strategy
* Competitive positioning
* Product developments
* Market opportunities

Output

Structured qualitative insights.

---

# 10. Risk Intelligence Agent

## Responsibility

Identify and summarize company risks.

Tasks

* Regulatory risks
* Litigation
* Supply chain issues
* Geopolitical exposure
* Market risks
* Operational risks
* Technology risks

Output

Prioritized risk summary.

---

# 11. Report Generation Agent

## Responsibility

Combine quantitative and qualitative findings into a structured report.

Possible outputs include:

* Company summary
* Earnings summary
* Company comparison
* Investment memo
* Financial overview

The report generation agent formats information but does not invent facts.

---

# 12. Citation Validation Agent

## Responsibility

Verify evidence supporting every generated response.

Tasks

* Validate document references.
* Associate page numbers.
* Remove unsupported statements.
* Calculate confidence score.

Only verified evidence is forwarded for final response generation.

---

# 13. Gemini LLM

## Responsibility

Generate the final natural language response.

Inputs

* Original user query.
* Retrieved evidence.
* Financial metrics.
* Qualitative analysis.
* Risk analysis.
* Validated citations.

The LLM performs reasoning and synthesis only.

It does not retrieve documents or compute financial metrics.

---

# 14. Agent Communication

Agents communicate sequentially.

Each agent receives structured outputs from the previous stage and produces structured outputs for the next stage.

No agent communicates directly with unrelated agents.

---

# 15. Failure Handling

If an agent fails:

* Stop downstream execution.
* Log the failure.
* Return a meaningful error to the orchestrator.
* Prevent propagation of incomplete or invalid data.

This ensures predictable system behavior.

---

# 16. Logging

Every agent records:

* Execution start
* Execution completion
* Processing time
* Success or failure
* Error details (if applicable)

These logs support monitoring, debugging, and performance optimization.

---

# 17. Future Extensions

The modular design allows additional agents to be introduced without affecting existing components.

Examples include:

* ESG Analysis Agent
* Valuation Agent
* Macroeconomic Analysis Agent
* Insider Trading Analysis Agent
* Portfolio Optimization Agent

These extensions are outside the scope of Version 1.0.

---

# 18. Guiding Principles

The AI layer follows these principles:

* Specialized responsibilities.
* Modular execution.
* Explainable processing.
* Evidence-based reasoning.
* Separation of computation and language generation.
* Reusable agent architecture.

