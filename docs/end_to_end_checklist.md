# End-to-end verification checklist

## Local UI (no Google Cloud credentials needed after `pip install -r requirements.txt`)
1. Start with `python app.py` and open `http://localhost:8080`.
2. Confirm dashboard and Approach, Architecture, About, FAQ, Contact pages open.
3. Confirm synthetic fallback applicants appear when BigQuery is not configured.
4. Select an applicant and inspect each check, reason and policy reference.

## BigQuery integration (requires a real Google Cloud project and permissions)
1. Run `gcloud auth application-default login`.
2. Set `GOOGLE_CLOUD_PROJECT` or `gcloud config set project YOUR_PROJECT_ID`.
3. Run `python make_data.py` and `python load_to_bigquery.py` from the project root.
4. Confirm the `loanpilot.applicant_view` view returns rows.
5. Click **Load from BigQuery**. The UI should show a success or actionable error message.
6. Submit an officer decision. Confirm the UI says it was saved; then query `loanpilot.decision_log` to verify the row.

## Before submission
- Update `docs/ai_usage_log.md` to reflect your actual tool use and time saved; do not invent an estimate.
- Review and open the cited official sources in `docs/research_note.md`.
- Keep the synthetic-data/mock-service disclaimer visible.
- Do not describe the current deterministic rule engine as an autonomous LLM agent.
- Cloud Run deployment is optional and is not marked complete until you deploy and test the URL.
