# LoanPilot Autonomous — Agentic AI Home Loan Approval Demo

A presales proof-of-concept for Indian home-loan processing. Uses synthetic applicant data, mock bureau/CERSAI checks, BigQuery for joined data and officer-decision logging, and a browser-based deterministic policy workflow. **It is not a production credit-decision system and does not autonomously sanction loans.** Final decisions remain with a human officer.

## Deliverables
- **D1:** Loan journey dashboard (`/`) with evidence, rule checks, explanations and officer actions.
- **D2:** Business approach story (`/approach`).
- **D3:** Technical/business architecture (`/architecture`).
- **D4:** About, FAQ and Contact (`/about`, `/faq`, `/contact`).
- **D5:** `docs/research_note.md` and PDF.
- **D6:** `docs/ai_usage_log.md` and PDF. The log is a draft; update the time estimate and details to reflect your own actual use before submission.
- **Walkthrough:** `docs/walkthrough_script.md` provides a 5-minute presentation script.
- **Unstructured examples:** `docs/sample_policies/` contains synthetic policy/checklist documents; `docs/sample_applicant_documents/` contains explicitly fake sample document examples. These examples are not OCR-ingested by the current app.

## Run locally
Python 3.11 or 3.12 recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python make_data.py
# Configure Google Cloud ADC and project first (see below)
python load_to_bigquery.py
python app.py
```
Open `http://localhost:8080`. For a demo without BigQuery, the front-end attempts BigQuery first and falls back to generated sample applicants if the API is unavailable. The UI now reports when applicant loading or decision logging fails; officer decisions persist only when BigQuery is configured. See `docs/end_to_end_checklist.md` for a verification runbook and `docs/walkthrough_script.md` for the live demo narrative.

## BigQuery setup
```bash
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
gcloud services enable bigquery.googleapis.com
python load_to_bigquery.py
```
The loader creates dataset `loanpilot`, six source tables, `decision_log`, and `applicant_view`. It replaces the six source tables each time it runs (`WRITE_TRUNCATE`). Use only synthetic data. If your project has a different dataset/location, update configuration consistently.

## Cloud Run (optional bonus)
```bash
gcloud run deploy loanpilot --source . --region asia-south1 --allow-unauthenticated
```
Before deployment, ensure the Cloud Run runtime service account has BigQuery Job User and the required dataset/table permissions. Do not make real applicant information public. The hosted URL must be tested after deployment; this repository does not claim it has already been deployed.

## Important limitations
- Decision rules run in JavaScript and are deterministic, not an LLM agent. The UI explains rule outcomes and requires officer action; do not describe it as autonomous AI sanctioning.
- Credit bureau and CERSAI results are mock records. No live government/bureau integration exists.
- Policy thresholds are demonstration assumptions. Only source-linked regulatory facts in the research note are represented as external claims; bank-specific policy must be confirmed by the bank.
- The app is an educational demo, not production-ready for security, compliance, fairness, or lending decisions.
