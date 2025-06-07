import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('store_sales.csv')

# Extract the 'units_sold' column
units_sold = df['units_sold']

# Create a histogram to visualize the distribution of units sold
plt.hist(units_sold, bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Frequency')

# Show the plot
plt.show()