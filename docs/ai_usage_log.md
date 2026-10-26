# AI usage log — LoanPilot Autonomous

**Purpose:** This is a draft record of AI-assisted work for the assignment. Edit it to match the tools, prompts, changes and time estimates you personally used before submitting. Do not report estimates as measured facts.

| Work area | AI-assisted activity | Human review/correction |
|---|---|---|
| Scope and design | Structured the home-loan workflow, BigQuery layer, mock bureau/CERSAI sources and human review gate. | Kept scope to one loan product and retained synthetic data only. |
| Data and SQL | Helped draft synthetic customer/application data generation, CSV loading and a BigQuery joined view. | Corrected a BigQuery `IFNULL(BOOL, STRING)` type mismatch by making the output type explicit. |
| Application | Helped build the Flask API and browser dashboard with checks, explanations and officer-decision logging. | Tested locally; verified startup and BigQuery connectivity separately rather than assuming cloud setup worked. |
| Documentation | Drafted architecture, workflow research and source list. | Regulatory claims and process descriptions need source verification; no professional interview is claimed. |
| Testing/troubleshooting | Used screenshots and Python/BigQuery tracebacks to diagnose missing dependencies and SQL errors. | Followed actual errors and checked outputs after each fix. |

## Prompts that illustrate the work
- “Build a synthetic-data home-loan approval demo using BigQuery, mock credit/property checks and a human approval step.”
- “Diagnose the BigQuery `IFNULL` type mismatch and propose the smallest safe SQL correction.”
- “Compare the working app against deliverables D1–D6 and identify missing pages and documents.”

## Time saved
**Estimate to be completed by the author:** compare the time you believe each task would take manually with actual time spent using AI. Do not claim a specific number until you have made that estimate. Suggested calculation: `estimated manual hours − actual hours = estimated hours saved`.

## Limitations and responsibility
AI-generated code and text can contain mistakes. I reviewed and corrected code using observed errors, used synthetic data, and retained human decision authority. The current decision engine is deterministic rule-based logic, not a deployed LLM agent. Verify all source links and technical tests before submission.
