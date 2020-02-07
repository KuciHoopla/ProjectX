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


def automat_run():
    # execution window:
    window = Tk()
    window.geometry('800x900')
    window.title("Invoice RPA")
    window.configure(background='#66b3ff')
    btns_frame = Frame(window)
    style_of_buttons = Style()
    style_of_buttons.configure('W.TButton', width=23, relief=GROOVE, activebackground="Red", borderwidth='4')


    def fill_printscreen_frame():
        bkrgframe = BkgrFrame(window, printscreen, 700, 600)
        bkrgframe.pack()

    btn_run_automat = Button(btns_frame, text="Run automat",
                                       style='W.TButton',
                                       command=lambda: [print(get_all_database_customers()),
                                                        update_customer_consumption_from_json_data(),
                                                        customers_frame.delete(1.0, END),
                                                        get_data_to_frame(),
                                                        print(get_all_database_customers()),
                                                        create_pdf(),
                                                        invoices_frame.delete(1.0, END),
                                                        fill_invoices_numbers_table(),
                                                        gmail_check(), fill_printscreen_frame()])

    def fill_invoices_numbers_table():
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
    btn_run_automat.grid(column=1, row=0, pady=3, padx=20)

    customer_table_label.pack()
    customers_frame.pack()
    invoices_label.pack()
    invoices_frame.pack()
    printscreen_label.pack()

    window.mainloop()


automat_run()

# create_new_consumption()