from tkinter import *


# Create window object
app = Tk()

# Order
order = IntVar()
order_label = Label(app, text="Order_id", font=("bold", 14), pady=20)
order_label.grid(row=0, column=0, sticky=W)
order_display = Entry(app, state="readonly", textvariable=order)
order_display.grid(row=0, column=1)

app.title("Order Manager")
app.geometry("700x350")

# start program
app.mainloop()
