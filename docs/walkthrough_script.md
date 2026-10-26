# 5-minute LoanPilot walkthrough

**0:00–0:30 — Business problem.** Home-loan underwriting combines application, customer/account, repayment, bureau and property evidence. LoanPilot demonstrates a shared evidence view and explainable checks. All records and external responses are synthetic/mock.

**0:30–1:15 — Data foundation.** Open Architecture. Explain CSV source files → BigQuery tables → `applicant_view` → Flask API → dashboard. Bureau/CERSAI are not live integrations.

**1:15–2:45 — Case review.** Open Loan review, load or generate sample applicants, select a case, inspect workflow stages, provenance, check results, reasons and illustrative policy labels. These are deterministic specialist workflow steps, not an LLM runtime.

**2:45–3:45 — Human decision.** Submit Approve, Refer or Decline. If BigQuery is configured, verify success and inspect `loanpilot.decision_log`. If not configured, state that honestly.

**3:45–4:30 — Value and controls.** Potential value: less manual evidence collation, more consistent visible checks and better traceability. No measured time saving or risk reduction is claimed. Human review and synthetic data are explicit limits.

**4:30–5:00 — Close.** Production next steps: connect approved enterprise sources, retrieve versioned policies, add governed agent orchestration, evaluate with credit/risk/compliance, and baseline turnaround time before claiming improvements.

## Truthful Q&A
- Real autonomous AI agent? No; current logic is deterministic and rule-based.
- Live CIBIL/CERSAI? No; mock data only.
- Publicly deployed? Only if the presenter deploys and tests a Cloud Run URL.
- Automatic approval? No; an authorised officer retains final authority.
