import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset= pd.read_csv('vgsales new.csv')  # Adjust for your file type (e.g., .xlsx for Excel)

# Preview the dataset
print("First 5 rows of the dataset:")
print(dataset.head())

# Summary information about the dataset
print("\nDataset Information:")
print(dataset.info())

# Basic statistics
print("\nDescriptive Statistics:")
print(dataset.describe())

dataset = dataset.dropna(subset=['Year'])

# Ensure 'Year' is an integer
dataset['Year'] = dataset['Year'].astype(int)

# Group sales data by year and calculate the total sales for each region
sales_trends = dataset.groupby('Year')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()

# Create a bar chart
sales_trends.plot(kind='bar', stacked=True, figsize=(14, 8))

# Add titles and labels
plt.title('Video Game Sales Trends by Region (Yearly)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Total Sales (in millions)', fontsize=14)
plt.legend(title="Region", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()