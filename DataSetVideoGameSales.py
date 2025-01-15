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

