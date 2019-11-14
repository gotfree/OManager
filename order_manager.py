from tkinter import *
from tkcalendar import Calendar, DateEntry
import pendulum as pd


# Create window object
app = Tk()

# date setup
tz = pd.timezone("Europe/Astrakhan")
now = pd.now(tz)
formatted_now = now.format('D MMM YYYY')
current_year = pd.now().year

# order_id
order = IntVar()
order_label = Label(app, text="Order_id", font=(12), pady=20)
order_label.grid(row=0, column=0, sticky=W)
order_display = Entry(app, state="readonly", textvariable=order, width=7)
order_display.grid(row=0, column=1)

# created_date
created_date = StringVar()
created_date_label = Label(app, text="Created date", font=(12), pady=20)
created_date_label.grid(row=0, column=3, sticky=W)
created_date_display = Entry(
    app,
    state="readonly",
    textvariable=created_date,
    justify=CENTER,
    width=12)
created_date.set(formatted_now)
created_date_display.grid(row=0, column=4)

# place for 'updated date' field

# deadline date picker
deadline_label = Label(app, text="Set deadline", font=(12))
deadline_label.grid(row=0, column=5)
cal = DateEntry(app, width=12, background='darkblue',
                    foreground='white', borderwidth=2, year=current_year)
cal.grid(row=0, column=6)

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
is_active_check.grid(row=2, column=0)

# general settings
app.title("Order Manager")
app.geometry("800x600")


# start program
app.mainloop()
