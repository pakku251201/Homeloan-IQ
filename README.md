# 🏡 Homeloan IQ — Home Loan Decision Support System

**An explainable, data-driven home loan review demo built with Python, Flask, and Google BigQuery.**

Homeloan IQ demonstrates how a bank can streamline home loan application reviews by combining applicant information, repayment history, simulated credit bureau data, property checks, and affordability rules into a single review dashboard.

Rather than making an automated lending decision, the system provides transparent recommendations and supporting reasons to help a credit officer review each application.

## ✨ Key Features

- **End-to-end review workflow:** Six stages covering application intake, KYC and documents, credit assessment, property checks, affordability, and officer review.
- **Explainable recommendations:** Displays the checks performed, reasons for flags, and relevant policy references.
- **Applicant dashboard:** Reviews applications, filters recommendations, and examines individual cases.
- **Human-in-the-loop decisions:** Credit officers can approve, refer, or decline cases through the interface.
- **Decision logging:** Includes a BigQuery-backed audit trail for officer decisions, subject to the configured Google Cloud environment and permissions.
- **Data integration:** Uses Google BigQuery to query consolidated applicant information.
- **Data upload:** Supports adding sample applicants and uploading CSV files through the dashboard.
- **Supporting documentation:** Includes the solution approach, architecture, research note, FAQ, and AI usage log.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Data warehouse | Google BigQuery |
| Data generation | Python, CSV |
| Deployment packaging | Docker |
| Testing | Pytest |

## 🏗️ Architecture

```text
Synthetic Applicant Data
          │
          ▼
   CSV Data Generation
          │
          ▼
   BigQuery Data Tables
          │
          ▼
  Consolidated Applicant View
          │
          ▼
      Flask Backend
          │
          ▼
   Loan Review Dashboard
          │
          ▼
 Explainable Policy Checks
          │
          ▼
  Credit Officer Review
          │
          ▼
    Decision Audit Log
```

The prototype separates data storage, application logic, and the user interface. Credit policy checks currently use deterministic rules rather than a live LLM-based agent.

## 🔍 Assessment Workflow

| Stage | Checks performed |
|---|---|
| 1. Application intake | Completeness and data quality |
| 2. KYC and documents | Verification status and income mismatches |
| 3. Credit assessment | Simulated credit score and repayment history |
| 4. Property assessment | Simulated CERSAI charge and collateral checks |
| 5. Affordability | FOIR, EMI burden, and loan-to-value rules |
| 6. Officer review | Recommendation, reasons, and recorded decision |

The system produces one of three recommendations:

- **Approve:** No configured rule has raised a blocking issue.
- **Refer:** A flag or missing information requires human review.
- **Decline:** One or more configured rules indicate that the case does not meet the demo's criteria.

These are prototype outcomes, not actual bank credit decisions.

## 📂 Project Structure

```text
Homeloan-IQ/
├── app.py
├── make_data.py
├── load_to_bigquery.py
├── schema.sql
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
├── data/
│   └── Synthetic CSV datasets
├── docs/
│   ├── approach and architecture
│   ├── research note
│   ├── AI usage log
│   ├── data dictionary
│   └── official sources
├── static/
│   ├── index.html
│   ├── approach.html
│   ├── architecture.html
│   ├── about.html
│   ├── faq.html
│   └── contact.html
└── tests/
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or later
- A Google Cloud project with BigQuery enabled
- Google Cloud credentials with the necessary BigQuery permissions

### 1. Clone the repository

```bash
git clone https://github.com/pakku251201/Homeloan-IQ.git
cd Homeloan-IQ
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Google Cloud

Authenticate using the Google Cloud CLI:

```bash
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
```

Enable the BigQuery API in your Google Cloud project. Ensure your authenticated account has the required permissions to create or query tables and views and to write decision records where supported.

### 5. Generate the demo data

```bash
python make_data.py
```

This generates synthetic applicant and supporting datasets. Check the `data/` folder and the script's output before proceeding.

### 6. Load the data into BigQuery

Set your project and dataset:

```bash
export GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
export DATASET=loanpilot
```

Run the data-loading script:

```bash
python load_to_bigquery.py
```

Review `schema.sql` and the loader configuration before running. The loader may replace existing demo tables, so do not point it at production data.

### 7. Start the application

```bash
python app.py
```

Open [http://localhost:8080](http://localhost:8080).

The application requires a working BigQuery connection for its BigQuery-backed features. Confirm the health endpoint and load the applicant data from the dashboard.

## 🧪 Testing

Run the available project tests:

```bash
pytest -q
```

The tests cover selected project functionality. Passing tests alone does not establish that Google Cloud integration or the complete application workflow works in every environment.

## 🔐 Security and Responsible Use

- Uses synthetic applicant data for demonstration.
- Simulates external credit bureau and property-check services.
- Requires a human credit officer to make the final decision.
- Does not claim compliance certification or production lending readiness.
- Requires appropriate IAM permissions and secure credential handling.
- Should not be used to process real customer financial information without security, privacy, regulatory, and model-risk reviews.

## 🔮 Potential Enhancements

- Add real, authorised integrations with credit bureau and property verification providers.
- Introduce an LLM-based orchestration layer with controlled tools and traceable actions.
- Add role-based access control and stronger audit logging.
- Implement monitoring, evaluation, and model governance.
- Deploy the application to Google Cloud Run and configure a secure production data pipeline.

These are potential enhancements; they should not be interpreted as currently implemented features.

## 👨‍💻 Author

**Pratheek Rao**

GitHub: [@pakku251201](https://github.com/pakku251201)

---

