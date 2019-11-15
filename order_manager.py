from tkinter import *
from tkcalendar import Calendar, DateEntry
import pendulum as pd


# general settings
app = Tk()
app.title("Order Manager")
app.geometry("1024x768")
app.columnconfigure((1, 3, 5), weight=2)
app.columnconfigure((0, 2, 4), weight=1)


# date setup
tz = pd.timezone("Europe/Astrakhan")
now = pd.now(tz)
formatted_now = now.format('D MMM YYYY')
current_year = pd.now().year

# order_id ROW 0
order = IntVar()
order_label = Label(app, text="Order_id", bg="green", fg="white")
order_label.grid(row=0, column=0)
order_display = Entry(app, state="readonly", textvariable=order)
order_display.grid(row=0, column=1)

# created_date
created_date = StringVar()
created_date_label = Label(app, text="Created date", bg="green", fg="white")
created_date_label.grid(row=0, column=2)
created_date_display = Entry(
    app,
    state="readonly",
    textvariable=created_date,
    # justify=CENTER,
    # width=12
)
created_date.set(formatted_now)
created_date_display.grid(row=0, column=3)

# place for 'updated date' field

# deadline date picker
deadline_label = Label(app, text="Set deadline", bg="green", fg="white")
deadline_label.grid(row=0, column=4)
cal = DateEntry(
    app,
    # background='darkblue',
    foreground='white',
    borderwidth=1,
    year=current_year
)
cal.grid(row=0, column=5)

# supplier ROW 1
supplier = StringVar()
supplier_label = Label(app, text="Supplier", bg="green", fg="white")
supplier_label.grid(row=1, column=0)
supplier_display = Entry(app, textvariable=supplier)
supplier_display.grid(row=1, column=1)

# shipper
shipper = StringVar()
shipper_label = Label(app, text="Shipper", bg="green", fg="white")
shipper_label.grid(row=1, column=2)
shipper_display = Entry(app, textvariable=shipper)
shipper_display.grid(row=1, column=3)

# customer
customer = StringVar()
customer_label = Label(app, text="Customer", bg="green", fg="white")
customer_label.grid(row=1, column=4)
customer_display = Entry(app, textvariable=customer)
customer_display.grid(row=1, column=5)

# sku field ROW 2-3
sku = IntVar()
sku_label = Label(app, text="sku", bg="green", fg="white")
sku_label.grid(row=2, column=0, sticky=W)
sku_display = Entry(app, textvariable=sku)
sku_display.grid(row=3, column=0)

# item_name
item_name = StringVar()
item_name_label = Label(app, text="Item name", bg="green", fg="white")
item_name_label.grid(row=2, column=1, sticky=W)
item_name_display = Entry(app, textvariable=item_name)
item_name_display.grid(row=3, column=1, columnspan=5, sticky="EW")

# quantity
quantity = IntVar()
quantity_label = Label(app, text="quantity", bg="green", fg="white")
quantity_label.grid(row=2, column=6, sticky=W)
quantity_display = Entry(app, textvariable=quantity)
quantity_display.grid(row=3, column=6)

# price
price = DoubleVar()
price_label = Label(app, text="price", bg="green", fg="white")
price_label.grid(row=2, column=7, sticky=W)
price_display = Entry(app, textvariable=price)
price_display.grid(row=3, column=7)

# comment field ROW 4
comment = StringVar()
comment_label = Label(app, text="Comment", bg="green", fg="white")
comment_label.grid(row=4, column=0)
comment_display = Entry(app, textvariable=comment)
comment_display.grid(row=4, column=1, columnspan=6, sticky="EW")

# is active
is_active = BooleanVar()
def check_box_repr():
    print(f"var value is: {is_active.get()}")
is_active_check = Checkbutton(
    app,
    text="is order active?",
    variable=is_active,
    command=check_box_repr
)
is_active_check.grid(row=4, column=7)


# start program
app.mainloop()
