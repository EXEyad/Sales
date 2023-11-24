import tkinter as tk
import sqlite3

# Function to view sales data
def view_sales():
  sales_data = cursor.execute('SELECT * FROM sales').fetchall()

  for row in sales_data:
    product_name, quantity, price = row
    print(
      f'Product Name: {product_name}, Quantity: {quantity}, Price: {price}')

# Function to add a product to the database
def add_product():
  product_name = product_name_entry.get()
  quantity = int(quantity_entry.get())
  price = float(price_entry.get())

  cursor.execute('INSERT INTO sales VALUES (?, ?, ?)',
                 (product_name, quantity, price))
  conn.commit()

  clear_fields()

# Function to clear entry fields
def clear_fields():
  product_name_entry.delete(0, tk.END)
  quantity_entry.delete(0, tk.END)
  price_entry.delete(0, tk.END)

# Create a database connection
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create the sales table if it doesn't exist
cursor.execute(
  'CREATE TABLE IF NOT EXISTS sales (product_name TEXT, quantity INTEGER, price REAL)'
)

# Define the GUI window
window = tk.Tk()
window.title('Sales Management System')

# Create product name entry field
product_name_label = tk.Label(window, text='Product Name:')
product_name_label.grid(row=0, column=0)
product_name_entry = tk.Entry(window)
product_name_entry.grid(row=0, column=1)

img = tk.PhotoImage(file='icons/icon.png')
imgl = tk.Label(window, image=img)
imgl.grid(row=1, column=2)
#Create quantity entry field
quantity_label = tk.Label(window, text='Quantity:')
quantity_label.grid(row=1, column=0)
quantity_entry = tk.Entry(window)
quantity_entry.grid(row=1, column=1)

# Create price entry field
price_label = tk.Label(window, text='Price:')
price_label.grid(row=2, column=0)
price_entry = tk.Entry(window)
price_entry.grid(row=2, column=1)

# Define the add product button
add_product_button = tk.Button(window, text='Add Product', command=add_product)
add_product_button.grid(row=3, column=0, columnspan=2)

# Define the view sales button
view_sales_button = tk.Button(window, text='View Sales', command=view_sales)
view_sales_button.grid(row=4, column=0, columnspan=2)

# Define the clear button
clear_button = tk.Button(window, text='Clear', command=clear_fields)
clear_button.grid(row=5, column=0, columnspan=2)


# Start the GUI event loop
window.mainloop()
