from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import pendulum as pd
from db import Database

db = Database("store.db")


# general settings
app = Tk()
app.title("Order Manager")
app.geometry("1024x768")
app.columnconfigure((1, 3, 5, 7), weight=1)
app.columnconfigure((0, 2, 4, 6), weight=1)

# date setup
tz = pd.timezone("Europe/Astrakhan")
now = pd.now(tz)
formatted_now = now.format("D MMM YYYY")
current_year = pd.now().year


# functions
def populate_list():
    order_list.delete(0, END)
    for row in db.fetch():
        order_list.insert(END, row)


def add_item():
    if (
        deadline.get() == ""
        or supplier.get() == ""
        or shipper.get() == ""
        or customer.get() == ""
        or sku.get() == ""
        or item_name.get() == ""
        or quantity.get() == ""
        or price.get() == ""
    ):
        messagebox.showerror("Required fields", "Please include all fields!")
        return
    db.insert(
        deadline.get(),
        supplier.get(),
        shipper.get(),
        customer.get(),
        sku.get(),
        item_name.get(),
        quantity.get(),
        price.get(),
    )
    order_list.delete(0, END)
    order_list.insert(
        END,
        (
            deadline.get(),
            supplier.get(),
            shipper.get(),
            customer.get(),
            sku.get(),
            item_name.get(),
            quantity.get(),
            price.get(),
        ),
    )
    populate_list()


def select_item(event):
    global selected_item
    index = order_list.curselection()[0]
    select_item = order_list.get(index)
    print(select_item)

    order_display.delete(0, END)
    order_display.insert(END, select_item[0])
    cal.delete(0, END)
    cal.insert(END, select_item[1])
    supplier_display.delete(0, END)
    supplier_display.insert(END, select_item[2])
    shipper_display.delete(0, END)
    shipper_display.insert(END, select_item[3])
    customer_display.delete(0, END)
    customer_display.insert(END, select_item[4])
    sku_display.delete(0, END)
    sku_display.insert(END, select_item[5])
    item_name_display.delete(0, END)
    item_name_display.insert(END, select_item[6])
    quantity_display.delete(0, END)
    quantity_display.insert(END, select_item[7])
    price_display.delete(0, END)
    price_display.insert(END, select_item[8])


def remove_order():
    print("Item has removed")


def update_order():
    print("Data has updated")


def clear_list():
    print("Clear")


# order_id ROW 0
order = IntVar()
order_label = Label(app, text="Order_id")
order_label.grid(row=0, column=0, sticky=W, pady=10, padx=10)
order_display = Entry(app, textvariable=order, justify=CENTER)
order_display.grid(row=0, column=1, sticky=W, padx=10)

# created_date
created_date = StringVar()
created_date_label = Label(app, text="Created date")
created_date_label.grid(row=0, column=3, sticky=W)
created_date_display = Entry(
    app,
    state="readonly",
    textvariable=created_date,
    justify=CENTER,
    # width=12
)
created_date.set(formatted_now)
created_date_display.grid(row=0, column=4)

# place for 'updated date' field

# deadline date picker
deadline_label = Label(app, text="Set deadline", width=10)
deadline_label.grid(row=0, column=6, sticky=W)
deadline = StringVar()
cal = DateEntry(
    app,
    # background='darkblue',
    foreground="white",
    borderwidth=1,
    year=current_year,
    justify=CENTER,
    textvariable=deadline,
    date_pattern="DD-mm-yyyy"
    # width=10,
)
cal.grid(row=0, column=7, sticky=W)

# supplier ROW 1-2
supplier = StringVar()
supplier_label = Label(app, text="Supplier")
supplier_label.grid(row=1, column=0, pady=10, sticky=W, padx=10)
supplier_display = Entry(app, textvariable=supplier)
supplier_display.grid(row=2, column=0, columnspan=2, sticky="EW", padx=10)

# shipper
shipper = StringVar()
shipper_label = Label(app, text="Shipper")
shipper_label.grid(row=1, column=2, columnspan=4, sticky=W, padx=(135, 0))
shipper_display = Entry(app, textvariable=shipper)
shipper_display.grid(row=2, column=2, columnspan=4, sticky="EW", padx=135)

# customer
customer = StringVar()
customer_label = Label(app, text="Customer")
customer_label.grid(row=1, column=6, sticky=W, padx=(0, 10))
customer_display = Entry(app, textvariable=customer)
customer_display.grid(row=2, column=6, columnspan=2, sticky="EW", padx=(0, 10))

# sku field ROW 3-4
sku = IntVar()
sku_label = Label(app, text="sku")
sku_label.grid(row=3, column=0, sticky=W, pady=5, padx=(10, 0))
sku_display = Entry(app, textvariable=sku)
sku_display.grid(row=4, column=0, sticky="EW", padx=(10, 0))

# item_name
item_name = StringVar()
item_name_label = Label(app, text="Item name")
item_name_label.grid(row=3, column=1, sticky=W)
item_name_display = Entry(app, textvariable=item_name)
item_name_display.grid(row=4, column=1, columnspan=5, sticky="EW")

# quantity
quantity = IntVar()
quantity_label = Label(app, text="quantity")
quantity_label.grid(row=3, column=6, sticky=W)
quantity_display = Entry(app, textvariable=quantity)
quantity_display.grid(row=4, column=6)

# price
price = DoubleVar()
price_label = Label(app, text="price")
price_label.grid(row=3, column=7, sticky=W, padx=(0, 10))
price_display = Entry(app, textvariable=price)
price_display.grid(row=4, column=7, padx=(0, 10))

# comment field ROW 5
comment = StringVar()
comment_label = Label(app, text="Comment")
comment_label.grid(row=5, column=0, pady=10)
comment_display = Entry(app, textvariable=comment)
comment_display.grid(row=5, column=1, columnspan=6, sticky="EW")

# is active
is_active = BooleanVar()


def check_box_repr():
    print(f"var value is: {is_active.get()}")


is_active_check = Checkbutton(
    app, text="is active?", variable=is_active, command=check_box_repr
)
is_active_check.grid(row=5, column=7, padx=(0, 10))

# Order list ROW 6
order_list = Listbox(app, height=26)
order_list.grid(row=6, column=0, columnspan=8, sticky="NSEW", padx=10)
# scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=6, column=7, sticky="NSE")
# set scroll to listbox
order_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=order_list.yview)
# bind select
order_list.bind("<<ListboxSelect>>", select_item)

# Buttons ROW 7
add_btn = Button(app, text="Add Order", width=20, command=add_item)
add_btn.grid(row=7, column=2, pady=20)

remove_btn = Button(app, text="Remove Order", width=20, command=remove_order)
remove_btn.grid(row=7, column=3)

update_btn = Button(app, text="Update Order", width=20, command=update_order)
update_btn.grid(row=7, column=4)

clear_btn = Button(app, text="Clear input", width=20, command=clear_list)
clear_btn.grid(row=7, column=5)

# ROW 8
created_date_label = Label(app, text="0", bg="white")
created_date_label.grid(row=8, column=0, sticky=NSEW)
created_date_label = Label(app, text="1", bg="green")
created_date_label.grid(row=8, column=1, sticky=NSEW)
created_date_label = Label(app, text="2", bg="white")
created_date_label.grid(row=8, column=2, sticky=NSEW)
created_date_label = Label(app, text="3", bg="green")
created_date_label.grid(row=8, column=3, sticky=NSEW)
created_date_label = Label(app, text="4", bg="white")
created_date_label.grid(row=8, column=4, sticky=NSEW)
created_date_label = Label(app, text="5", bg="green")
created_date_label.grid(row=8, column=5, sticky=NSEW)
created_date_label = Label(app, text="6", bg="white")
created_date_label.grid(row=8, column=6, sticky=NSEW)
created_date_label = Label(app, text="7", bg="green")
created_date_label.grid(row=8, column=7, sticky=NSEW)

# populate data
populate_list()

# start program
app.mainloop()
