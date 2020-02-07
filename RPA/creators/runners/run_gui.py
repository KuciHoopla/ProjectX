import os
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *
from BkgrFrame import BkgrFrame
from RPA.creators.consumption.consumption_creator import create_new_consumption
from RPA.creators.customers.customers_creator import create_customers_file, customers_json, filling_json, \
    get_all_json_customers
from RPA.creators.database.database_creator import create_customers_table, fill_database_from_json, \
    update_customer_consumption_from_json_data, get_all_database_customers, customers_database
from RPA.creators.database.database_invoices import get_all_invoices_numbers, invoices_path, invoices_number_path
from RPA.creators.pdf.create_pdf import create_pdf
from RPA.creators.variables.variables import printscreen
from RPA.gmail_check.gmail_check import gmail_check


def create_customer_data():
    try:
        customers = get_all_database_customers()
        for customer in customers:
            id = customer["id"]
            first_name = customer["first_name"]
            last_name = customer["last_name"]
            consumption = customer["consumption"]
            tariff = customer["tariff"]
            email = customer["email"]
            return id, first_name, last_name, consumption, tariff, email

    except:
        print("no data")


def gui_runner():
    # execution window:
    window = Tk()
    window.geometry('1200x900')
    window.title("Invoice RPA")
    window.configure(background='#66b3ff')
    btns_frame = Frame(window)
    style_of_buttons = Style()
    style_of_buttons.configure('W.TButton', width=23, relief=GROOVE, activebackground="Red", borderwidth='4')
    number_of_customers = 0

    def func_create_customers_json(button, number):
        global number_of_customers
        print(entry_of_number.get())
        try:
            number_of_customers = int(entry_of_number.get())
            create_customers_file(customers_json)
            filling_json(number_of_customers)
            entry_of_number.delete(0, END)
            button.config(state=DISABLED)
            entry_of_number.config(state=DISABLED)
            print(get_all_json_customers())
        except:
            entry_of_number.delete(0, END)
            messagebox.showinfo("Alert", "Must be a number")

    def fill_printscreen_frame():
        bkrgframe = BkgrFrame(window, printscreen, 700, 600)
        bkrgframe.pack()

    def func_create_customers_table(button):
        button.config(state=DISABLED)
        create_customers_table()
        fill_database_from_json()
        get_data_to_frame()

    def delete_database():
        try:
            os.remove(customers_database)
            os.remove(customers_json)
            os.remove(invoices_path)
            os.remove(invoices_number_path)
            os.remove(printscreen)
            customers_frame.delete(1.0, END)
            invoices_frame.delete(1.0, END)
            btn_create_customers_json.config(state=ACTIVE)
            btn_create_customers_table.config(state=ACTIVE)
            entry_of_number.config(state=ACTIVE)
            print(""" 
            __________________________________________________
                          Process successful.
                          All data deleted!
            __________________________________________________""")
        except:
            print("no database")

    label_enter_number_of_customers = Label(btns_frame, text="Enter number of customers:")
    entry_of_number = Entry(btns_frame, textvariable=number_of_customers)
    btn_create_customers_json = Button(btns_frame, text="Generate customers json",
                                       style='W.TButton',
                                       command=lambda: func_create_customers_json(btn_create_customers_json,
                                                                                  number_of_customers))

    btn_create_customers_table = Button(btns_frame, text="Create customer table",
                                        style='W.TButton',
                                        command=lambda: [func_create_customers_table(btn_create_customers_table),
                                                         print(get_all_database_customers())])

    btn_create_new_consumption = Button(btns_frame, text="Create new consumption",
                                        style='W.TButton',
                                        command=lambda: [create_new_consumption(),
                                                         update_customer_consumption_from_json_data(),
                                                         customers_frame.delete(1.0, END),
                                                         get_data_to_frame(),
                                                         print(get_all_database_customers())])

    btn_send_invoice_to_customer_email = Button(btns_frame, text="Send email with invoice",
                                                style='W.TButton',
                                                command=lambda: create_pdf())

    btn_get_invoices_numbers = Button(btns_frame, text="Get invoices numbers",
                                      style='W.TButton',
                                      command=lambda: [invoices_frame.delete(1.0, END),
                                                       fill_invoices_numbers_table(btn_get_invoices_numbers)])

    btn_check_gmail = Button(btns_frame, text="Check Gmail",
                             style='W.TButton',
                             command=lambda: [gmail_check(), fill_printscreen_frame()])

    btn_delete_all_data = Button(btns_frame, text="Delete all data",
                                 style='W.TButton',
                                 command=lambda: delete_database())

    def fill_invoices_numbers_table(button):
        invoices_frame.insert(INSERT,
                              f"""                
Invoices numbers : 
{get_all_invoices_numbers()}
                """)

    def get_len_of_database():
        try:
            length = len(get_all_database_customers())
            return length
        except:
            return 0

    def get_data_to_frame():
        customers_frame.delete(1.0, END)
        sum_of_sustomers = get_len_of_database()
        customers_frame.insert(INSERT,
                               f"""                
                            Customers:  {sum_of_sustomers}       
                          ____________________
________________________________________________________________________
            """)

        try:
            customers = get_all_database_customers()
            for customer in customers:
                id = customer["id"]
                first_name = customer["first_name"]
                last_name = customer["last_name"]
                consumption = customer["consumption"]
                tariff = customer["tariff"]
                email = customer["email"]
                customers_frame.insert(INSERT, f""" 
id:{id} | {first_name} | {last_name} | {email} | {consumption} | {tariff}
________________________________________________________________________
                """)

        except:
            print("no data")

    customer_table_label = Label(window, text="Customer table")


    customers_frame = ScrolledText(
        master=window,
        wrap=WORD,
        width=72,
        height=10
    )

    invoices_label = Label(window, text="Invoices table")
    printscreen_label = Label(window, text="Email printscreen")


    invoices_frame = ScrolledText(
        master=window,
        wrap=WORD,
        width=32,
        height=10
    )
    get_data_to_frame()


    #left side
    btns_frame.pack(side=LEFT)
    label_enter_number_of_customers.grid(column=1, row=0, pady=5, padx=10)
    entry_of_number.grid(column=1, row=1, pady=1, padx=5)
    btn_create_customers_json.grid(column=1, row=3, pady=3, padx=20)
    btn_create_customers_table.grid(column=1, row=4, pady=3, padx=5)
    btn_send_invoice_to_customer_email.grid(column=1, row=5, pady=3, padx=5)
    btn_get_invoices_numbers.grid(column=1, row=6, pady=3, padx=5)
    btn_create_new_consumption.grid(column=1, row=7, pady=3, padx=5)
    btn_check_gmail.grid(column=1, row=8, pady=3, padx=5)
    btn_delete_all_data.grid(column=1, row=9, pady=3, padx=5)

    customer_table_label.pack()
    customers_frame.pack()
    invoices_label.pack()
    invoices_frame.pack()
    printscreen_label.pack()


    window.mainloop()

