import os
import tkinter as tk
from tkinter import ttk, messagebox

# Define the filename for storing stock data
STOCK_FILE = "stock.txt"

class StockApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stock & Job Management")  # Set the title of the window
        self.geometry("600x480")  # Set the window size
        self.initialize_stock_file()  # Initialize stock file if it doesn't exist
        self.stock = self.load_stock()  # Load the stock data into the stock dictionary - data structure used to store information about the items in stock.
        self.create_widgets()  # Create the user interface widgets( UI (User Interface) of this stock management application is created using Tkinter and the widgets in Tkinter are elements of the GUI (like buttons, labels, and text boxes))
        self.refresh_list()  # Refresh the list of stock items in the GUI(Responsible for whenever there is a change in the stock data.)

    def initialize_stock_file(self):
        """
        Check if the stock file exists; if not, create it with default items.
        """
        if not os.path.exists(STOCK_FILE):  # If the stock file doesn't exist
            default = "\n".join([
                "1,Screw,100",
                "2,Hammer,10",
                "3,Saw,20",
                "4,Steel,5",
                "5,Timber,2",
            ])  # Default stock items to be written in the file
            with open(STOCK_FILE, "w") as f:
                f.write(default)  # Write the default data to the file
            print("Stock file created with default items.")

    def load_stock(self):
        """
        Load stock data from the file into a dictionary.
        """
        s = {}  # Create an empty dictionary to hold stock data(doesn't contain any data initially, but can later be populated with data)
        try:
            with open(STOCK_FILE) as f:
                for line in f:
                    if not line.strip():
                        continue  # Skip empty lines
                    iid, desc, qty = line.strip().split(",", 2)  # Split each line by commas
                    s[int(iid)] = {"desc": desc, "qty": int(qty)}  # Add to the dictionary with item ID as key(process of storing a value in a dictionary where the key is the item ID, and the value is the data associated with that item (like its description and quantity).)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load stock:\n{e}")
        return s  # Return the stock dictionary(core data structure of the application.)

    def save_stock(self):
        """
        Save the current stock data back to the file.
        """
        with open(STOCK_FILE, "w") as f:
            for iid, item in sorted(self.stock.items()):  # Sort stock items by ID
                f.write(f"{iid},{item['desc']},{item['qty']}\n")  # Write each item to the file( save or store each stock item from the program into an external file (in this case, stock.txt))
                f.flush()  # Flush after each write operation to ensure data is saved( forcing the data to be immediately written to disk after it’s written in memory. This ensures that the file actually contains the data at that moment, without relying on automatic buffering mechanisms(a system that automatically manages buffering without requiring explicit user or programmer intervention).) Buffering is the process of storing(temporarily) in a dedicated memory store.

    def create_widgets(self):
        """
        Create the GUI widgets (buttons, labels, entries, etc.).
        """
        # Create a tabbed interface with "Stock" and "Jobs" tabs
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, pady=8, padx=8)  # Add the notebook (tab) widget

        # Create frames for each tab
        stock_frame = ttk.Frame(notebook)
        job_frame = ttk.Frame(notebook)
        notebook.add(stock_frame, text="Stock")
        notebook.add(job_frame, text="Jobs")

        # STOCK tab UI

    # Frame for the stock list (Treeview) (graphical user interface (GUI) element used to display the stock items in an organized, table-like format in the application.)
        list_frame = ttk.Frame(stock_frame)
        list_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Treeview to display stock items with columns for description and quantity(using the Treeview widget in Tkinter to visually present a list of stock items in a table-like format.)
        self.tree = ttk.Treeview(list_frame, height=10, columns=("desc", "qty"), show="headings")
        self.tree.heading("desc", text="Description")  # Column header for Description
        self.tree.heading("qty", text="Quantity")  # Column header for Quantity
        self.tree.pack(fill="both", expand=True)

        # Separator for visual separation between elements(create a clear visual distinction or space between different sections or elements on the screen.)
        ttk.Separator(stock_frame).pack(fill="x", padx=10, pady=5)

        # Frame for actions (adding items, setting quantities) (container widget (action_frame) used in the GUI layout to group and organize interactive elements)
        action_frame = ttk.Frame(stock_frame)
        action_frame.pack(fill="x", padx=10, pady=5)

        # Entries for adding a new item
        self.add_desc = tk.Entry(action_frame, width=20)  # Description entry
        self.add_qty = tk.Entry(action_frame, width=8, justify="right")  # Quantity entry
        ttk.Button(action_frame, text="Add Item", command=self.add_item).grid(row=0, column=0, padx=4, pady=4)  # Button to add item
        tk.Label(action_frame, text="Desc:").grid(row=0, column=1, padx=4)  # Label for Description
        self.add_desc.grid(row=0, column=2)  # Position for description input
        tk.Label(action_frame, text="Qty:").grid(row=0, column=3, padx=4)  # Label for Quantity
        self.add_qty.grid(row=0, column=4)  # Position for quantity input

        # Entries for setting the quantity of an existing item
        self.update_id = tk.Entry(action_frame, width=6)  # Item ID input for updating quantity
        self.update_qty = tk.Entry(action_frame, width=8, justify="right")  # New quantity input
        ttk.Button(action_frame, text="Set Qty", command=self.set_qty).grid(row=1, column=0, padx=4, pady=4)  # Button to set quantity
        tk.Label(action_frame, text="ID:").grid(row=1, column=1)  # Label for Item ID
        self.update_id.grid(row=1, column=2)  # Position for item ID input
        tk.Label(action_frame, text="New Qty:").grid(row=1, column=3)  # Label for new quantity
        self.update_qty.grid(row=1, column=4)  # Position for new quantity input

        # ==== JOBS tab UI ====

        # Inner frame for job actions(managing job-related actions like taking or returning stock items)
        job_frame_inner = ttk.Frame(job_frame)
        job_frame_inner.pack(fill="x", padx=10, pady=10)

        # Entry for item ID to take or return
        self.job_id = tk.Entry(job_frame_inner, width=6)  # Item ID input for job actions
        # Entry for quantity to take
        self.job_qty = tk.Entry(job_frame_inner, width=8, justify="right")  # Quantity input for taking items
        ttk.Button(job_frame_inner, text="Take", command=lambda r=False: self.take_or_return(False)).grid(row=0, column=0)  # Button to take items
        tk.Label(job_frame_inner, text="→ Qty:").grid(row=0, column=1)  # Label for the quantity to take
        self.job_qty.grid(row=0, column=2)  # Position the take quantity input
        tk.Label(job_frame_inner, text="ID:").grid(row=0, column=3)  # Label for the item ID
        self.job_id.grid(row=0, column=4)  # Position the item ID input

        # Button to return items to stock
        ttk.Button(job_frame_inner, text="Return", command=lambda r=True: self.take_or_return(True)).grid(row=1, column=0)  # Button to return items
        tk.Label(job_frame_inner, text="← Qty:").grid(row=1, column=1)  # Label for the quantity to return
        self.return_qty = tk.Entry(job_frame_inner, width=8, justify="right")  # Input for return quantity
        self.return_qty.grid(row=1, column=2)  # Position the return quantity input field

    def refresh_list(self):
        """
        Update the list of stock items in the Treeview.
        """
        # Clear the current list
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Insert all stock items into the list
        for iid, it in sorted(self.stock.items()):
            self.tree.insert("", "end", iid, values=(it["desc"], it["qty"]))

    def add_item(self):
        """
        Add a new stock item based on user input.
        """
        desc = self.add_desc.get().strip()  # Get the description input by the user
        try:
            qty = int(self.add_qty.get())  # Try to convert the quantity to an integer
            assert qty >= 0  # Ensure the quantity is non-negative
        except:
            return messagebox.showerror("Error", "Enter a non-negative integer for quantity.")  # Show error if invalid quantity
        if not desc:  # Ensure description is not empty
            return messagebox.showerror("Error", "Description cannot be empty.")
        new_id = max(self.stock, default=0) + 1  # Generate a new item ID
        self.stock[new_id] = {"desc": desc, "qty": qty}  # Add the item to the stock dictionary
        self.save_stock()  # Save the updated stock data
        self.refresh_list()  # Refresh the stock list in the GUI
        messagebox.showinfo("Added", f"Added item {desc} (ID {new_id}) qty {qty}")  # Show confirmation message
        self.add_desc.delete(0, tk.END)  # Clear the description input
        self.add_qty.delete(0, tk.END)  # Clear the quantity input

    def set_qty(self):
        """
        Set the quantity of an existing stock item.
        """
        try:
            iid = int(self.update_id.get())  # Get the item ID
            new_qty = int(self.update_qty.get())  # Get the new quantity
        except:
            return messagebox.showerror("Error", "Enter valid item ID and quantity.")  # Show error if invalid input
        if iid not in self.stock:  # Check if the item ID exists
            return messagebox.showerror("Error", "Item ID not found.")  # Show error if not found
        self.stock[iid]["qty"] = new_qty  # Update the item's quantity
        self.save_stock()  # Save the updated stock data
        self.refresh_list()  # Refresh the stock list in the GUI
        messagebox.showinfo("Updated", f"Updated item {iid} quantity to {new_qty}")  # Show confirmation message
        self.update_id.delete(0, tk.END)  # Clear the item ID input
        self.update_qty.delete(0, tk.END)  # Clear the new quantity input

    def take_or_return(self, is_returning):
        """
        Take or return stock items based on the job action.
        """
        try:
            iid = int(self.job_id.get())  # Get the item ID
            qty = int(self.job_qty.get())  # Get the quantity for the job
        except:
            return messagebox.showerror("Error", "Enter valid item ID and quantity.")  # Show error if invalid input
        if iid not in self.stock:  # Check if the item ID exists
            return messagebox.showerror("Error", "Item ID not found.")  # Show error if not found
        if is_returning:  # Check if returning items
            self.stock[iid]["qty"] += qty  # Add the quantity back to the stock
            action = "returned"
        else:  # If taking items
            if self.stock[iid]["qty"] < qty:  # Check if there is enough quantity to take
                return messagebox.showerror("Error", "Not enough stock available.")  # Show error if insufficient stock
            self.stock[iid]["qty"] -= qty  # Decrease the quantity from the stock
            action = "taken"
        self.save_stock()  # Save the updated stock data
        self.refresh_list()  # Refresh the stock list in the GUI
        messagebox.showinfo("Success", f"{qty} items {action} (ID {iid})")  # Show success message
        self.job_id.delete(0, tk.END)  # Clear the item ID input
        self.job_qty.delete(0, tk.END)  # Clear the quantity input
        self.return_qty.delete(0, tk.END)  # Clear the return quantity input
if __name__ == "__main__":
    # Run the application
    StockApp().mainloop()  # Start the Tkinter main event loop, making the app interactive
