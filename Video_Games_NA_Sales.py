import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 

# Load the dataset
dataset= pd.read_csv('vgsales new.csv')  # Adjust for your file type (e.g., .xlsx for Excel)

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



y = np.arange(len(top_10_games['Name']))  # Create indices for each game

# Set bar width
width = 0.4

plt.figure(figsize=(10, 6))

# Plot separate bars for NA Sales and Global Sales
plt.barh(y - width / 2, top_10_games['NA_Sales'], height=width, color='blue', label='North America Sales')
plt.barh(y + width / 2, top_10_games['Global_Sales'], height=width, color='green', alpha=0.7, label='Global Sales')

# Add labels and title
plt.xlabel('Sales (in millions)')
plt.ylabel('Game Titles')
plt.title('Top Ten Selling Video Games in North America')

# Add custom y-ticks
plt.yticks(y, top_10_games['Name'])

# Add legend
plt.legend()

# Adjust layout for better readability
plt.tight_layout()

# Show plot
plt.show()