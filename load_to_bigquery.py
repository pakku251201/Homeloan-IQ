# load_to_bigquery.py - uploads the CSV files into BigQuery and builds the gold view.
# New library: google-cloud-bigquery is Google's official Python tool for talking to BigQuery.
from google.cloud import bigquery

client = bigquery.Client()          # uses the login from "gcloud auth application-default login"
project = client.project
dataset_name = "loanpilot"
tables = ["customers", "accounts", "repayments", "bureau", "cersai", "applications"]

# Make the dataset (a folder of tables). exists_ok means no error if it is already there.
client.create_dataset(bigquery.Dataset(project + "." + dataset_name), exists_ok=True)

for table in tables:
    # autodetect lets BigQuery guess column types from the CSV, so we do not write schemas by hand.
    # WRITE_TRUNCATE replaces old rows, so running this twice does not duplicate data.
    job_settings = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1,
                                          autodetect=True, write_disposition="WRITE_TRUNCATE")
    with open("data/" + table + ".csv", "rb") as f:
        client.load_table_from_file(f, project + "." + dataset_name + "." + table, job_config=job_settings).result()
    print("Loaded", table)

# Table that stores what credit officers decide. The app writes here.
log_schema = [bigquery.SchemaField("application_id", "STRING"), bigquery.SchemaField("officer_decision", "STRING"),
              bigquery.SchemaField("logged_at", "TIMESTAMP")]
client.create_table(bigquery.Table(project + "." + dataset_name + ".decision_log", schema=log_schema), exists_ok=True)

# Build the view from schema.sql by filling in the project and dataset names.
sql = open("schema.sql").read().replace("PROJECT", project).replace("DATASET", dataset_name)
client.query(sql).result()
print("Done. View ready: " + project + "." + dataset_name + ".applicant_view")
