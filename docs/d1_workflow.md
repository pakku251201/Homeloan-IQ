# D1 — Loan approval demo journey

## Implemented demo journey
1. **Intake:** applicant records are generated synthetically, uploaded as CSV, or loaded from the BigQuery `applicant_view`.
2. **Data quality:** required fields, missing values, impossible values and unusual numeric values are checked.
3. **KYC and documents:** KYC status and income-document mismatch are flagged for review.
4. **Credit and repayment:** synthetic/mock bureau score and repayment-bounce count are evaluated.
5. **Property and affordability:** mock CERSAI charge, FOIR, EMI and LTV are evaluated against illustrative policy thresholds.
6. **Recommendation:** the browser rule engine returns Approve, Refer or Decline with check-level explanations and policy references.
7. **Human review:** an officer selects Approve, Refer/Hold or Decline. The Flask API writes the choice and timestamp to BigQuery `decision_log` when configured.

## Data source map
| Logical source | Fields used | Status |
|---|---|---|
| Applications / customers | ID, applicant name, income, requested amount, property value, tenure | Synthetic demo data; can be loaded from BigQuery view or CSV |
| Accounts / repayments | Existing EMI and bounce count | Synthetic demo data; combined into the view or supplied by CSV |
| Credit bureau | Credit score | Mock/synthetic; no live bureau API |
| CERSAI | Existing property charge indicator | Mock/synthetic; no live CERSAI API |
| Policy book | Credit score, FOIR, LTV and referral thresholds | Illustrative demo thresholds; not an actual bank's approved policy |
| Officer decision log | Officer choice and timestamp | BigQuery `decision_log`, if backend credentials and table are available |

## Important boundary
The current app uses deterministic JavaScript rules. The labels “agent activity” and “agent trace” describe sequential workflow steps, not autonomous LLM agents. Final lending decisions remain with a human officer. BigQuery connectivity and decision persistence must be tested in the target Google Cloud project before the demo is described as end-to-end verified.

## Validation checklist
- [ ] Run `python load_to_bigquery.py` successfully and confirm the six source tables plus `applicant_view` exist.
- [ ] Open the dashboard and click **Load from BigQuery**; confirm records appear.
- [ ] Select a case and confirm check-level reasons and policy references appear.
- [ ] Submit an officer choice; confirm an inserted row appears in `decision_log`.
- [ ] Try a synthetic edge case (missing score, high FOIR, charge found) and confirm it routes to Refer/Decline as expected.
