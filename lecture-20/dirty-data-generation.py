import pandas as pd
import numpy as np
import datetime

# --- Configuration ---
num_employees = 200
output_filename = 'dirty_employee_data.csv'

# --- Data Generation ---
np.random.seed(42) # for reproducibility

# Possible department names with inconsistencies
departments = ['Sales', 'Marketing', 'Technology', 'Tech', 'Human Resources', 'HR', 'hr', 'IT']
department_weights = [0.25, 0.15, 0.15, 0.1, 0.1, 0.1, 0.05, 0.1]

# Generate basic employee data
data = {
    'employee_id': [1000 + i for i in range(num_employees)],
    'name': [f'Employee_{i}' for i in range(num_employees)],
    'department': np.random.choice(departments, num_employees, p=department_weights),
    'salary': np.random.normal(loc=75000, scale=15000, size=num_employees).round(-2),
    'start_date': pd.to_datetime(pd.date_range(start='2020-01-01', periods=num_employees, freq='W'))
}

df = pd.DataFrame(data)

# --- Introduce 'Dirtiness' ---

# 1. Introduce missing salaries (approx 15% of data)
salary_missing_indices = df.sample(frac=0.15, random_state=1).index
df.loc[salary_missing_indices, 'salary'] = np.nan

# 2. Introduce missing start dates (approx 10% of data)
date_missing_indices = df.sample(frac=0.10, random_state=2).index
df.loc[date_missing_indices, 'start_date'] = pd.NaT

# 3. Introduce some completely empty rows for 'department'
dept_missing_indices = df.sample(frac=0.05, random_state=3).index
df.loc[dept_missing_indices, 'department'] = np.nan

# 4. Convert start_date to string to simulate incorrect data type
df['start_date'] = df['start_date'].dt.strftime('%Y-%m-%d').astype('object')
# Re-introduce NaNs after string conversion, as NaT becomes 'NaT' string
df.loc[date_missing_indices, 'start_date'] = np.nan


# --- Save to CSV ---
try:
    df.to_csv(output_filename, index=False)
    print(f"Successfully created '{output_filename}' with {len(df)} rows.")
    print("The file contains missing salaries, missing/inconsistent departments, and missing dates.")
except Exception as e:
    print(f"An error occurred while saving the file: {e}")

