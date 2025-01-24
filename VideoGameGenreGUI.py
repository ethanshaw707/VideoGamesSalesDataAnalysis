# How popular is each genre in the regions?
##Ethan Shaw's Code
import pandas as pd
import tkinter as tk
from tkinter import ttk

# Load the dataset
df = pd.read_csv('vgsales new.csv', sep=',')

# Select only the relevant sales columns and group by Genre
genre_sales = df[['Genre', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].groupby('Genre').sum()

# Create a simple GUI using tkinter
def show_sales():
    # Get the selected genre
    selected_genre = genre_var.get()
    
    # Check if the genre exists and display the sales
    if selected_genre in genre_sales.index:
        sales = genre_sales.loc[selected_genre]
        result.set(f"Sales for {selected_genre}:\n" + sales.to_string())
    else:
        result.set(f"The genre '{selected_genre}' was not found in the dataset.")

# Initialize the main window
root = tk.Tk()
root.title("Video Game Sales by Genre")

# Dropdown menu for genres
genre_var = tk.StringVar()
genres = list(genre_sales.index)
genre_dropdown = ttk.Combobox(root, textvariable=genre_var)
genre_dropdown['values'] = genres
genre_dropdown['state'] = 'readonly'  # Make the dropdown read-only
genre_dropdown.pack(pady=10)

# Button to display sales
show_button = tk.Button(root, text="Show Sales", command=show_sales)
show_button.pack(pady=5)

# Label to display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, justify=tk.LEFT)
result_label.pack(pady=10)


# Run the main loop
root.mainloop()
