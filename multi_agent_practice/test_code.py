import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime, timedelta

# Create a sample dataset that matches the presentation
np.random.seed(42)

# Generate sample data
categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Home & Garden']
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(365)]

data = []
for date in dates[:100]:  # Use first 100 days for testing
    for category in categories:
        units_sold = np.random.randint(10, 100)
        revenue = units_sold * np.random.uniform(10, 50)
        data.append({
            'date': date,
            'product_category': category,
            'units_sold': units_sold,
            'revenue': revenue
        })

# Create DataFrame
df = pd.DataFrame(data)
print(f"Dataset shape: {df.shape}")
print("\nDataset preview:")
print(df.head())
print(f"\nProduct categories: {df['product_category'].unique()}")

# Test the generated code from our agents
print("\n" + "="*50)
print("TESTING THE GENERATED CODE:")
print("="*50)

# Test 1: Bar chart code
print("\n1. Testing bar chart code...")
revenue_by_category = df.groupby('product_category')['revenue'].sum().reset_index()
print("Revenue by category:")
print(revenue_by_category)

plt.figure(figsize=(10, 6))
sns.barplot(x='product_category', y='revenue', data=revenue_by_category)
plt.title('Total Revenue by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('revenue_by_category.png')
plt.close()
print("✅ Bar chart created and saved as 'revenue_by_category.png'")

# Test 2: Line chart code (with monthly aggregation)
print("\n2. Testing line chart code...")
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')
monthly_revenue = df.groupby('month')['revenue'].sum().reset_index()
monthly_revenue['month_str'] = monthly_revenue['month'].astype(str)

plt.figure(figsize=(12, 6))
sns.lineplot(x='month_str', y='revenue', data=monthly_revenue)
plt.title('Revenue Over Time by Month')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('revenue_over_time.png')
plt.close()
print("✅ Line chart created and saved as 'revenue_over_time.png'")

print("\n" + "="*50)
print("✅ ALL TESTS PASSED! The generated code works perfectly.")
print("="*50)
