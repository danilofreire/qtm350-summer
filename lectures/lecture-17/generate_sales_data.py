import pandas as pd
import numpy as np
import datetime

# --- Configuration ---
num_rows = 1000
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2024, 12, 31)
product_categories = {
    "Electronics": {"base_price": 250, "price_std": 150},
    "Groceries": {"base_price": 50, "price_std": 25},
    "Apparel": {"base_price": 80, "price_std": 40},
    "Home Goods": {"base_price": 120, "price_std": 60},
    "Books": {"base_price": 20, "price_std": 10}
}
output_filename = "store_sales.csv"

# --- Data Generation ---

# Create an evenly spaced date range using the idiomatic pandas function
date_range = pd.date_range(start=start_date, end=end_date, periods=num_rows)

# Assign product categories randomly
categories_list = list(product_categories.keys())
assigned_categories = np.random.choice(categories_list, num_rows, p=[0.2, 0.4, 0.15, 0.15, 0.1])

# Generate units sold (with some randomness)
units_sold = np.random.poisson(lam=5, size=num_rows) + 1

# Generate revenue based on category base price and units sold
revenue_list = []
for i in range(num_rows):
    cat = assigned_categories[i]
    base_price = product_categories[cat]['base_price']
    price_std = product_categories[cat]['price_std']
    
    # Simulate a price for this specific transaction
    transaction_price = np.random.normal(loc=base_price, scale=price_std)
    # Ensure price is not negative
    transaction_price = max(5, transaction_price) 
    
    # Calculate revenue
    revenue = transaction_price * units_sold[i]
    revenue_list.append(revenue)

# --- Create DataFrame and Save ---
df = pd.DataFrame({
    'date': date_range.date,
    'product_category': assigned_categories,
    'units_sold': units_sold,
    'revenue': revenue_list
})

# Round revenue to 2 decimal places
df['revenue'] = df['revenue'].round(2)

# Save to CSV
try:
    df.to_csv(output_filename, index=False)
    print(f"Successfully created '{output_filename}' with {len(df)} rows.")
except Exception as e:
    print(f"An error occurred while saving the file: {e}")

