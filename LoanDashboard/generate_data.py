import pandas as pd
import random

def generate_synthetic_data(num_entries=1000):
    data = []
    for i in range(num_entries):
        customer_id = f"CUST-{i+1:04d}"
        name = f"Customer-{i+1}"
        age = random.randint(21, 65)
        address = f"Address-{random.randint(1, 500)}"
        loan_amount_requested = random.randint(5000, 500000)
        loan_repayment_history = random.choice([0, 1])  # binary
        monthly_income = random.randint(20000, 100000)
        monthly_expenditure = random.randint(5000, 75000)
        other_loans = random.randint(0, 5)
        # Logic for loan eligibility
        loan_eligibility = (
            1 if monthly_income > 1.5 * loan_amount_requested and loan_repayment_history == 1 else 0
        )
        data.append([
            customer_id, name, age, address, loan_amount_requested,
            loan_repayment_history, monthly_income, monthly_expenditure,
            other_loans, loan_eligibility
        ])

    columns = [
        "Customer ID", "Name", "Age", "Address",
        "Loan Amount Requested", "Loan Repayment History",
        "Monthly Income", "Monthly Expenditure",
        "Other Loans", "Loan Eligibility"
    ]
    df = pd.DataFrame(data, columns=columns)
    df.to_csv("loan_data.csv", index=False)
    print("Synthetic data saved as 'loan_data.csv'.")

generate_synthetic_data()
