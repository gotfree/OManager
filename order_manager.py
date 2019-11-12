from tkinter import *


# Create window object
app = Tk()

# order_id
order = IntVar()
order_label = Label(app, text="Order_id", font=(12), pady=20)
order_label.grid(row=0, column=0, sticky=W)
order_display = Entry(app, state="readonly", textvariable=order, width=7)
order_display.grid(row=0, column=1)

# date fields

# supplier
supplier = StringVar()
supplier_label = Label(app, text="Supplier", font=(12))
supplier_label.grid(row=1, column=0, sticky=W)
supplier_display = Entry(app, textvariable=supplier)
supplier_display.grid(row=1, column=1)

# shipper
shipper = StringVar()
shipper_label = Label(app, text="Shipper", font=(12))
shipper_label.grid(row=1, column=2, sticky=W)
shipper_display = Entry(app, textvariable=shipper)
shipper_display.grid(row=1, column=3)

# customer
customer = StringVar()
customer_label = Label(app, text="Customer", font=(12))
customer_label.grid(row=1, column=4, sticky=W)
customer_display = Entry(app, textvariable=customer)
customer_display.grid(row=1, column=5)

app.title("Order Manager")
app.geometry("800x600")

# start program
app.mainloop()
