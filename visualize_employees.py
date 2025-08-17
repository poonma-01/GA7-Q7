# visualize_employees.py
# Q7 — Data Visualization with ChatGPT
# Verification Email: 23f2003677@ds.study.iitm.ac.in

import os
import random
import pandas as pd
import plotly.express as px

OUT_CSV = "employees.csv"
OUT_HTML = "employee_department_histogram.html"
N = 100

def generate_sample_data(n=100):
    random.seed(2025)
    depts = ["Marketing", "Sales", "HR", "Engineering", "Operations", "Finance", "Legal"]
    regions = ["North", "South", "East", "West"]
    probs = [0.18, 0.25, 0.10, 0.30, 0.10, 0.05, 0.02]
    rows = []
    for i in range(1, n+1):
        dept = random.choices(depts, weights=probs, k=1)[0]
        region = random.choice(regions)
        score = round(random.uniform(50, 100), 1)
        rows.append({"EmployeeID": f"E{i:03d}", "Department": dept, "Region": region, "PerfScore": score})
    return pd.DataFrame(rows)

def main():
    if os.path.exists(OUT_CSV):
        df = pd.read_csv(OUT_CSV)
    else:
        df = generate_sample_data(N)
        df.to_csv(OUT_CSV, index=False)

    marketing_count = (df["Department"] == "Marketing").sum()
    print("Verification email: 23f2003677@ds.study.iitm.ac.in")
    print(f"Frequency count for 'Marketing' department: {marketing_count}")

    dept_counts = df["Department"].value_counts().reset_index()
    dept_counts.columns = ["Department", "Count"]

    fig = px.bar(dept_counts, x="Department", y="Count",
                 title="Employee Count by Department",
                 labels={"Count": "Number of Employees"},
                 text="Count")
    fig.update_traces(textposition="outside")
    fig.write_html(OUT_HTML, include_plotlyjs="cdn", full_html=True)

if __name__ == "__main__":
    main()
