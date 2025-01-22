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