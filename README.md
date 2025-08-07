# Stock & Job Management System

A simple Python desktop application built with Tkinter for managing stock inventory and job checkout/return operations.  
It stores data persistently in a text file (`stock.txt`) with auto-incrementing IDs and quantity tracking.

## Features

- Add new stock items with description and quantity  
- Update stock quantities without removing items  
- Job tab for checking out and returning stock items  
- Stock validation to prevent over-checkout  
- Data saved and loaded automatically from `stock.txt`

## Functions
- from tkinter import ttk, messagebox

-Purpose: Imports ttk (themed widgets for tkinter) and messagebox (for displaying messages) to enhance the GUI and handle errors

- if not os.path.exists(STOCK_FILE):

-Purpose: Checks if the stock file exists. If it doesn't, the program creates it with default stock data.

- iid, desc, qty = line.strip().split(",", 2)

-Purpose: Splits each line from the stock file into item ID, description, and quantity, which are then stored in a dictionary for use in the app

- self.images[item_id] = default_photo

-Purpose: Assigns a default image to the item in case the image couldn't be loaded from the URL.

- response.raise_for_status()

-Purpose: Raises an error if the image URL is invalid or the image cannot be fetched, preventing further execution

- notebook.add(stock_frame, text="Stock")

-Purpose: Adds a tab to the notebook for displaying stock items in the GUI, allowing users to switch between tabs (e.g., stock and job tabs)

- self.image_label.configure(image=self.images[item_id])

-Purpose: Updates the image displayed on the GUI when a user selects a stock item, showing the corresponding image

- self.stock[new_id] = {"desc": desc, "qty": qty}

-Purpose: Adds a new item to the stock dictionary with its description and quantity, then saves the updated stock

- self.stock[iid]["qty"] = new_qty

-Purpose: Updates the quantity of an existing stock item by modifying the corresponding entry(matches the id) in the stock dictionary

- if self.stock[iid]["qty"] < qty:

-Purpose:  Checks if there is enough stock to be taken, preventing users from taking more items than available

## How to Run

1. Make sure you have Python 3 installed (with Tkinter).  
2. Clone the repository:  
   ```bash
   git clone https://github.com/chanvany/chanvany.github.io
