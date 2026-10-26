# make_data.py - creates pretend bank data as CSV files (no real customers).
# Why: BigQuery needs data to hold. These files act as the bank's core banking, bureau and CERSAI sources.
import csv
import random

random.seed(7)  # fixed seed so every run gives the same data, which makes demos repeatable
COUNT = 600     # how many applicants to create

first_names = ["Anita", "Rohit", "Sana", "Vikram", "Meera", "Arjun", "Priya", "Karan", "Divya", "Imran", "Lakshmi", "Suresh"]
last_names = ["Rao", "Mehta", "Khan", "Singh", "Nair", "Iyer", "Sharma", "Reddy", "Das", "Patel"]
employer_types = ["salaried", "salaried", "salaried", "self-employed", "government"]

def save(filename, header, rows):
    # Writes one CSV file into the data folder.
    with open("data/" + filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

customers, accounts, repayments, bureau, cersai, applications = [], [], [], [], [], []

for i in range(1, COUNT + 1):
    customer_id = "C" + str(1000 + i)
    application_id = "A" + str(1000 + i)
    income = random.randint(30000, 200000)
    existing_emi = round(income * random.random() * 0.3) if random.random() < 0.6 else 0
    cibil = random.randint(600, 850)
    kyc = "pending" if random.random() < 0.04 else "verified"
    name = random.choice(first_names) + " " + random.choice(last_names)
    customers.append([customer_id, name, random.choice(employer_types), income, existing_emi, kyc])
    accounts.append([customer_id, round(income * random.uniform(0.2, 4))])

    # Bureau data: about 1 in 100 customers has no score, so the agents meet missing data.
    if random.random() > 0.01:
        bureau.append([customer_id, cibil])

    # Repayment history: 12 months of the existing loan. Lower scores bounce more often.
    if existing_emi > 0:
        bounce_chance = (850 - cibil) / 600
        for month in range(1, 13):
            repayments.append([customer_id, month, 1 if random.random() < bounce_chance else 0])

    # The loan request. Property value is usually higher than the loan.
    amount = round(income * random.uniform(40, 130) / 50000) * 50000
    property_value = round(amount / random.uniform(0.55, 0.95) / 50000) * 50000
    if random.random() < 0.01:
        property_value = amount // 2   # impossible case on purpose: loan bigger than property
    doc_issue = "Salary slip does not match bank credits" if random.random() < 0.07 else ""
    applications.append([application_id, customer_id, amount, property_value, random.choice([10, 15, 20, 25]), doc_issue])
    cersai.append([application_id, "yes" if random.random() < 0.08 else "no"])

save("customers.csv", ["customer_id", "name", "employer_type", "income", "existing_emi", "kyc_status"], customers)
save("accounts.csv", ["customer_id", "avg_balance"], accounts)
save("repayments.csv", ["customer_id", "month", "bounced"], repayments)
save("bureau.csv", ["customer_id", "cibil"], bureau)
save("cersai.csv", ["application_id", "charge"], cersai)
save("applications.csv", ["application_id", "customer_id", "amount", "property_value", "years", "doc_issue"], applications)
print("Created", COUNT, "applicants and", len(repayments), "repayment rows in the data folder")
