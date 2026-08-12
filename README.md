# Data Cleaning & Reporting Automation

## Objective
Automate data cleaning and reporting workflows using Python.

## Assignment Requirements Covered
- Python automation
- Handling missing values
- Removing duplicate records
- Fixing inconsistent text and date formats
- Converting invalid numeric values
- Generating an automated report
- Creating a visual summary

## Dataset
`raw_employee_data.csv` is intentionally messy so the cleaning process can be demonstrated.

## Cleaning Steps
1. Load raw CSV data.
2. Remove duplicate rows.
3. Trim extra spaces.
4. Standardize names and city names.
5. Standardize department names.
6. Convert salary to numeric and handle invalid/missing values using the median.
7. Replace missing emails with a placeholder.
8. Standardize dates.
9. Save the cleaned dataset.

## Reporting
The script automatically creates:
- `cleaned_employee_data.csv`
- `automated_report.txt`
- `department_summary.png`

## How to Run

Open this folder in VS Code and run:

```bash
pip install -r requirements.txt
python data_cleaning_automation.py
```

## Expected Workflow

```text
Raw Data
   ↓
Load CSV
   ↓
Remove Duplicates
   ↓
Handle Missing Values
   ↓
Fix Inconsistent Data
   ↓
Save Clean Dataset
   ↓
Generate Report
   ↓
Generate Visualization
```

## Conclusion
The project demonstrates how Python can automate repetitive data preprocessing and reporting tasks. Automation improves consistency, reduces manual work, and produces repeatable reports.
