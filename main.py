import tkinter as tk
import csv
import datetime


def save_purchase():
    # Get customer and product details from entry fields
    customer_name = entry_customer_name.get()
    product_name = entry_product_name.get()
    product_code = entry_product_code.get()
    product_price = float(entry_product_price.get())
    product_amount = int(entry_product_amount.get())

    # Calculate total price
    total_price = product_price * product_amount

    # Get current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Prepare data for CSV file
    purchase_data = [current_timestamp, customer_name, product_code, product_name, product_price, product_amount, total_price]

    # Open CSV file in append mode
    with open('purchases.csv', 'a', newline='') as csvfile:
        # Create CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write purchase data to CSV file
        csv_writer.writerow(purchase_data)

    # Clear entry fields after saving
    entry_customer_name.delete(0, tk.END)
    entry_product_code.delete(0, tk.END)
    entry_product_name.delete(0, tk.END)
    entry_product_price.delete(0, tk.END)
    entry_product_amount.delete(0, tk.END)

# Create Tkinter window
window = tk.Tk()
window.title('Sales Management System')
px = window.geometry()

# Create labels and entry fields for customer details
label_customer_name = tk.Label(window, text="Customer Name:")
entry_customer_name = tk.Entry(window)

label_customer_name.grid(row=0, column=0)
entry_customer_name.grid(row=0, column=1)

# Create labels and entry fields for product information
label_product_code = tk.Label(window, text="Product Code:")
entry_product_code = tk.Entry(window)

label_product_code.grid(row=1, column=0)
entry_product_code.grid(row=1, column=1)

label_product_name = tk.Label(window, text="Product Name:")
entry_product_name = tk.Entry(window)

label_product_name.grid(row=2, column=0)
entry_product_name.grid(row=2, column=1)

label_product_price = tk.Label(window, text="Product Price:")
entry_product_price = tk.Entry(window)

label_product_price.grid(row=3, column=0)
entry_product_price.grid(row=3, column=1)

label_product_amount = tk.Label(window, text="Product Quantity:")
entry_product_amount = tk.Entry(window)

label_product_amount.grid(row=4, column=0)
entry_product_amount.grid(row=4, column=1)

# Create button to save purchase data
button_save = tk.Button(window, text="Save Purchase", command=save_purchase)
button_save.grid(row=5, column=1)
# Run the Tkinter main loop
window.mainloop() 
print(px)
