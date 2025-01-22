import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 

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

# Code for the question: What are the ten 10 selling video games in North America and how much those ten games made in total global sales? 
# This filter the dataset to remove the NA_sales that has 0 or doesn't have a value
dataset_filter = dataset[dataset['NA_Sales'] > 0]

#Sorts the dataset from top to bottom
sorted_dataset = dataset_filter.sort_values(by='NA_Sales', ascending=False)

#This sorts for only calling the top ten games in sells in NA
top_10_games = sorted_dataset[['Name','Platform','NA_Sales', 'Global_Sales']].head(10)

#This gets the sum of the total global sales of the top ten games
global_sales = top_10_games['Global_Sales'].sum()

print("Top 10 selling games in North America:")
print(top_10_games)

print(f"Total Global Sale of the ten selling games is {global_sales:.2f} million")


# Code for the Question: How do sales vary by genre in Japan compared to Europe?

# Drop rows with missing values in 'Genre', 'JP_Sales', or 'EU_Sales'
dataset = dataset.dropna(subset=['Genre', 'JP_Sales', 'EU_Sales'])

# Group by Genre and calculate total sales for Japan and Europe
sales_by_genre = dataset.groupby('Genre')[['JP_Sales', 'EU_Sales']].sum()

# Sort genres by total sales in Japan for better visualization
sales_by_genre = sales_by_genre.sort_values('JP_Sales', ascending=False)

# Plot a grouped bar chart to compare sales
x = np.arange(len(sales_by_genre))  # Label locations
width = 0.35  # Width of the bars

fig, ax = plt.subplots(figsize=(12, 8))

# Add bars for JP_Sales and EU_Sales
bar1 = ax.bar(x - width/2, sales_by_genre['JP_Sales'], width, label='Japan (JP Sales)', color='red')
bar2 = ax.bar(x + width/2, sales_by_genre['EU_Sales'], width, label='Europe (EU Sales)', color='blue')

# Add titles and labels
ax.set_title('Sales by Genre in Japan vs. Europe', fontsize=16)
ax.set_xlabel('Genre', fontsize=14)
ax.set_ylabel('Total Sales (in millions)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(sales_by_genre.index, rotation=45)
ax.legend(fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()