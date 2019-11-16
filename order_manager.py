from tkinter import *
from tkcalendar import Calendar, DateEntry
import pendulum as pd


# general settings
app = Tk()
app.title("Order Manager")
app.geometry("1024x768")
app.columnconfigure((1, 3, 5), weight=1)
app.columnconfigure((0, 2, 4), weight=1)

# date setup
tz = pd.timezone("Europe/Astrakhan")
now = pd.now(tz)
formatted_now = now.format("D MMM YYYY")
current_year = pd.now().year

# order_id ROW 0
order = IntVar()
order_label = Label(app, text="Order_id")
order_label.grid(row=0, column=0)
order_display = Entry(app, state="readonly", textvariable=order)
order_display.grid(row=0, column=1, sticky=W)

# created_date
created_date = StringVar()
created_date_label = Label(app, text="Created date")
created_date_label.grid(row=0, column=3)
created_date_display = Entry(
    app,
    state="readonly",
    textvariable=created_date,
    # justify=CENTER,
    # width=12
)
created_date.set(formatted_now)
created_date_display.grid(row=0, column=4)

# place for 'updated date' field

# deadline date picker
deadline_label = Label(app, text="Set deadline")
deadline_label.grid(row=0, column=5)
cal = DateEntry(
    app,
    # background='darkblue',
    foreground="white",
    borderwidth=1,
    year=current_year,
)
cal.grid(row=0, column=6, sticky=W)

# supplier ROW 1
supplier = StringVar()
supplier_label = Label(app, text="Supplier")
supplier_label.grid(row=1, column=0)
supplier_display = Entry(app, textvariable=supplier)
supplier_display.grid(row=1, column=1, columnspan=2, sticky="EW")

# shipper
shipper = StringVar()
shipper_label = Label(app, text="Shipper")
shipper_label.grid(row=1, column=3)
shipper_display = Entry(app, textvariable=shipper)
shipper_display.grid(row=1, column=4)

# customer
customer = StringVar()
customer_label = Label(app, text="Customer")
customer_label.grid(row=1, column=5)
customer_display = Entry(app, textvariable=customer)
customer_display.grid(row=1, column=6, columnspan=2, sticky="EW")

# sku field ROW 2-3
sku = IntVar()
sku_label = Label(app, text="sku")
sku_label.grid(row=2, column=0, sticky=W)
sku_display = Entry(app, textvariable=sku)
sku_display.grid(row=3, column=0, sticky="EW")

# item_name
item_name = StringVar()
item_name_label = Label(app, text="Item name")
item_name_label.grid(row=2, column=1, sticky=W)
item_name_display = Entry(app, textvariable=item_name)
item_name_display.grid(row=3, column=1, columnspan=5, sticky="EW")

# quantity
quantity = IntVar()
quantity_label = Label(app, text="quantity")
quantity_label.grid(row=2, column=6, sticky=W)
quantity_display = Entry(app, textvariable=quantity)
quantity_display.grid(row=3, column=6)

# price
price = DoubleVar()
price_label = Label(app, text="price")
price_label.grid(row=2, column=7, sticky=W)
price_display = Entry(app, textvariable=price)
price_display.grid(row=3, column=7)

# comment field ROW 4
comment = StringVar()
comment_label = Label(app, text="Comment")
comment_label.grid(row=4, column=0)
comment_display = Entry(app, textvariable=comment)
comment_display.grid(row=4, column=1, columnspan=6, sticky="EW")

# is active
is_active = BooleanVar()


def check_box_repr():
    print(f"var value is: {is_active.get()}")


is_active_check = Checkbutton(
    app, text="is order active?", variable=is_active, command=check_box_repr
)
is_active_check.grid(row=4, column=7)

# Order list ROW 5
order_list = Listbox(app, height=8, width=50)
order_list.grid()

# start program
app.mainloop()
