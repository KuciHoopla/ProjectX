from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *

from BkgrFrame import BkgrFrame
from RPA.creators.database.database_creator import get_all_database_customers
from RPA.creators.database.database_invoices import get_all_invoices_numbers
from RPA.creators.pdf.create_pdf import create_pdf
from RPA.creators.variables.variables import printscreen
from RPA.gmail_check.gmail_check import gmail_check
from creators.database.id_table_creator import add_customers_consumption
from creators.directory_check.directory_check import get_list_of_jsons

jsons_directory_len_old = 0


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
    window.geometry('900x900')
    window.title("Invoice RPA")
    window.configure(background='#66b3ff')
    style_of_buttons = Style()
    style_of_buttons.configure('W.TButton', width=23, relief=GROOVE, activebackground="Red", borderwidth='4')

    def fill_printscreen_frame():
        bkrgframe = BkgrFrame(window, printscreen, 700, 600)
        bkrgframe.pack()

    def fill_invoices_numbers_table():
        invoices_frame.insert(INSERT,
                              f"""                
Invoices numbers : 
{get_all_invoices_numbers()}
                """)
        invoices_frame.pack()

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

    customer_table_label.pack()
    customers_frame.pack()
    invoices_label.pack()
    invoices_frame.pack()
    printscreen_label.pack()

    def refresh():
        global jsons_directory_len_old
        jsons_directory_len = get_list_of_jsons()
        customers_frame.delete(1.0, END)
        invoices_frame.delete(1.0, END)
        get_data_to_frame()
        fill_invoices_numbers_table()
        fill_printscreen_frame()
        if jsons_directory_len > jsons_directory_len_old:
            create_pdf()
            # gmail_check()
            jsons_directory_len_old = jsons_directory_len
        else:
            print("no new data")
            print(get_all_database_customers())
            print(get_all_database_customers())

        window.after(10000, refresh)

    window.after(10000, refresh)

    window.mainloop()


automat_run()

