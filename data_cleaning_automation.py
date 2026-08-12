import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parent
RAW_FILE = BASE / "raw_employee_data.csv"
CLEAN_FILE = BASE / "cleaned_employee_data.csv"
REPORT_FILE = BASE / "automated_report.txt"
CHART_FILE = BASE / "department_summary.png"

# 1. Load raw data
df = pd.read_csv(RAW_FILE)
original_rows = len(df)

# 2. Remove exact duplicate rows
duplicate_rows = df.duplicated().sum()
df = df.drop_duplicates().copy()

# 3. Standardize text columns
for col in ["Name", "Email", "City", "Department"]:
    df[col] = df[col].astype("string").str.strip()

df["Name"] = df["Name"].str.title()
df["City"] = df["City"].str.title()
df["Department"] = df["Department"].str.title()

# 4. Clean salary: invalid values become missing, then fill with median
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
missing_salary_before = int(df["Salary"].isna().sum())
salary_median = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(salary_median)

# 5. Handle missing email with a clear placeholder
missing_email_before = int(df["Email"].isna().sum())
df["Email"] = df["Email"].fillna("not_provided@example.com")

# 6. Standardize dates
df["JoinDate"] = pd.to_datetime(df["JoinDate"], errors="coerce", dayfirst=False)
missing_dates = int(df["JoinDate"].isna().sum())
df["JoinDate"] = df["JoinDate"].fillna(pd.Timestamp("2026-01-01"))
df["JoinDate"] = df["JoinDate"].dt.strftime("%Y-%m-%d")

# 7. Save cleaned dataset
df.to_csv(CLEAN_FILE, index=False)

# 8. Create summary
department_summary = (
    df.groupby("Department")
      .agg(EmployeeCount=("EmployeeID", "count"),
           AverageSalary=("Salary", "mean"),
           TotalSalary=("Salary", "sum"))
      .reset_index()
)
department_summary["AverageSalary"] = department_summary["AverageSalary"].round(2)

# 9. Create visualization
plt.figure(figsize=(9, 6))
plt.bar(department_summary["Department"], department_summary["AverageSalary"])
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Average Salary by Department")
plt.tight_layout()
plt.savefig(CHART_FILE, dpi=150)
plt.close()

# 10. Generate automated text report
with open(REPORT_FILE, "w", encoding="utf-8") as f:
    f.write("DATA CLEANING & REPORTING AUTOMATION REPORT\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Original rows: {original_rows}\n")
    f.write(f"Duplicate rows removed: {duplicate_rows}\n")
    f.write(f"Rows after cleaning: {len(df)}\n")
    f.write(f"Missing/invalid salary values handled: {missing_salary_before}\n")
    f.write(f"Missing email values handled: {missing_email_before}\n")
    f.write(f"Invalid/missing dates handled: {missing_dates}\n")
    f.write(f"Overall average salary: {df['Salary'].mean():.2f}\n\n")
    f.write("DEPARTMENT SUMMARY\n")
    f.write("-" * 50 + "\n")
    f.write(department_summary.to_string(index=False))
    f.write("\n\nFiles generated automatically:\n")
    f.write("- cleaned_employee_data.csv\n")
    f.write("- automated_report.txt\n")
    f.write("- department_summary.png\n")

print("========== DATA CLEANING & REPORTING AUTOMATION ==========")
print(f"Original rows: {original_rows}")
print(f"Duplicate rows removed: {duplicate_rows}")
print(f"Rows after cleaning: {len(df)}")
print(f"Missing/invalid salary values handled: {missing_salary_before}")
print(f"Missing email values handled: {missing_email_before}")
print(f"Invalid/missing dates handled: {missing_dates}")
print(f"Overall average salary: {df['Salary'].mean():.2f}")
print("\nDepartment summary:")
print(department_summary.to_string(index=False))
print("\nGenerated:")
print("cleaned_employee_data.csv")
print("automated_report.txt")
print("department_summary.png")
