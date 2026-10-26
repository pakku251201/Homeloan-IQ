
# app.py - LoanPilot Autonomous
# Flask web server with BigQuery applicant data and demo-mode decision logging.

import csv
import io
import os
from datetime import datetime, timezone

from flask import Flask, request, send_from_directory, jsonify
from google.cloud import bigquery

app = Flask(__name__, static_folder="static")

# BigQuery configuration
client = bigquery.Client()
dataset = os.environ.get("DATASET", "loanpilot")

# Demo-only decision storage.
# Decisions remain available while this Flask process is running.
# They are cleared when the application restarts.
demo_decisions = []


@app.route("/")
def home():
    """Serve the main dashboard."""
    return send_from_directory("static", "index.html")


@app.route("/<page>")
def supporting_page(page):
    """Serve the supporting project pages."""
    allowed = {
        "approach",
        "architecture",
        "about",
        "faq",
        "contact"
    }

    if page not in allowed:
        return "Not found", 404

    return send_from_directory("static", page + ".html")


@app.route("/api/health")
def health():
    """Check whether the Flask application is running."""
    return jsonify({
        "status": "ok",
        "app": "LoanPilot Autonomous",
        "data": "synthetic/demo",
        "decision_storage": "temporary in-memory demo mode"
    })


@app.route("/api/applicants")
def applicants():
    """Load applicant records from the BigQuery view and return CSV."""
    query = (
        f"SELECT * FROM `{client.project}.{dataset}.applicant_view` "
        "LIMIT 5000"
    )

    try:
        rows = list(client.query(query).result())

        if not rows:
            return "", 204

        output = io.StringIO()
        writer = csv.writer(output)
        columns = list(rows[0].keys())

        writer.writerow(columns)

        for row in rows:
            writer.writerow([
                "" if row[column] is None else row[column]
                for column in columns
            ])

        return output.getvalue(), 200, {
            "Content-Type": "text/csv; charset=utf-8"
        }

    except Exception:
        app.logger.exception("Failed to load applicants from BigQuery")

        return jsonify({
            "error": (
                "Could not load applicants from BigQuery. "
                "Check the Flask terminal."
            )
        }), 500


@app.route("/api/decision", methods=["POST"])
def decision():
    """
    Record a credit officer's decision in temporary demo memory.

    This intentionally does not write to BigQuery because the current
    Google Cloud project does not permit the required writes without
    enabling billing.
    """
    data = request.get_json(silent=True) or {}

    applicant_id = str(data.get("id", "")).strip()
    choice = str(data.get("choice", "")).strip().title()

    allowed_choices = {"Approve", "Refer", "Decline"}

    if not applicant_id:
        return jsonify({
            "error": "An application ID is required."
        }), 400

    if choice not in allowed_choices:
        return jsonify({
            "error": "Choice must be Approve, Refer, or Decline."
        }), 400

    record = {
        "application_id": applicant_id,
        "officer_decision": choice,
        "logged_at": datetime.now(timezone.utc).isoformat(),
        "storage": "demo-memory"
    }

    # Keep the latest decision per applicant in this running process.
    existing_index = next(
        (
            index for index, item in enumerate(demo_decisions)
            if item["application_id"] == applicant_id
        ),
        None
    )

    if existing_index is not None:
        demo_decisions[existing_index] = record
    else:
        demo_decisions.append(record)

    app.logger.info(
        "Demo decision recorded: %s -> %s",
        applicant_id,
        choice
    )

    return jsonify({
        "success": True,
        "message": (
            "Decision recorded in demo mode. "
            "It has NOT been saved to BigQuery."
        ),
        "decision": record
    }), 200


@app.route("/api/decisions")
def get_decisions():
    """Return decisions recorded during this Flask session."""
    return jsonify({
        "storage": "demo-memory",
        "persistent": False,
        "decisions": demo_decisions
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        debug=False
    )
