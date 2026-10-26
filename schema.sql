-- The "gold" view: one row per application with everything the agents need.
-- Why a view: raw tables stay untouched and the agents always read one joined, clean shape.
-- PROJECT and DATASET are replaced by load_to_bigquery.py.
CREATE OR REPLACE VIEW `PROJECT.DATASET.applicant_view` AS
SELECT
  a.application_id AS id, c.name, c.income, c.existing_emi AS old_emi, b.cibil,
  a.amount, a.property_value AS property, a.years,
  IFNULL(CAST(x.charge AS STRING), 'no') AS charge,
  IFNULL(CAST(a.doc_issue AS STRING), '') AS doc_issue,
  IFNULL(r.bounces, 0) AS bounces, c.kyc_status, c.employer_type, ac.avg_balance
FROM `PROJECT.DATASET.applications` a
JOIN `PROJECT.DATASET.customers` c USING (customer_id)
LEFT JOIN `PROJECT.DATASET.bureau` b USING (customer_id)
LEFT JOIN `PROJECT.DATASET.cersai` x USING (application_id)
LEFT JOIN `PROJECT.DATASET.accounts` ac USING (customer_id)
LEFT JOIN (SELECT customer_id, SUM(bounced) AS bounces FROM `PROJECT.DATASET.repayments` GROUP BY customer_id) r USING (customer_id);
