# LoanPilot architecture

```text
Synthetic source CSVs
  ├─ customers / income / KYC
  ├─ applications / requested loan / property
  ├─ repayment history
  ├─ mock bureau response
  └─ mock CERSAI property-charge response
             │ Python loader (CSV autodetect)
             ▼
        BigQuery raw tables
             │ SQL joins / aggregation
             ▼
       applicant_view (gold view)
             │ Flask API: GET /api/applicants
             ▼
       Browser demo / loan officer UI
             │ deterministic checks
             ├─ intake and data-quality checks
             ├─ document/KYC flags
             ├─ credit, FOIR and LTV rules
             ├─ collateral and repayment flags
             └─ explainable recommendation + policy citation
             │ officer choice
             ▼
       Flask POST /api/decision → BigQuery decision_log
```

## Design principles
- **Lakehouse-style foundation:** BigQuery consolidates structured records and mock external checks; policy text is represented in the UI as a small demo policy book. This prototype does not implement a document OCR/vector search pipeline.
- **Evidence before recommendation:** display the fields used by each rule and the reason for any referral.
- **Human in the loop:** recommendation is not sanction. An authorised officer records the decision.
- **Governance:** synthetic data only, deterministic rules, audit record of officer decision, policy versioning is a future enhancement.
- **External tools:** bureau and CERSAI are stubbed by synthetic tables; no live APIs are called.

## Current vs future state
Current implementation: deterministic JavaScript rules + Flask endpoints + BigQuery view and decision log. Future production work would require authentication/authorisation, role-based access, encrypted document storage, policy version control, monitoring, fairness testing, model validation, human overrides, immutable audit logs and security review.
