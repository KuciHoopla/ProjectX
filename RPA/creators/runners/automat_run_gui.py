import os
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *
from creators.excel.excel_invoice_creator import invoice_creator
from creators.pdf.convert_xlsx_to_pdf import convert_xlsx_to_pdf
from creators.runners.BkgrFrame import BkgrFrame
from RPA.creators.database.database_creator import get_all_database_customers
from RPA.creators.database.database_invoices import get_all_invoices_numbers
from RPA.creators.variables.variables import printscreen, jsons_folder, resources_folder
from RPA.gmail_check.gmail_check import gmail_check
from creators.consumption.consumption_creator import get_json_with_new_consumption
from creators.directory_check.directory_check import get_list_of_jsons
from tkscrolledframe import ScrolledFrame

from creators.runners.reporter import run_reporter

jsons_directory_len_old = 0


def automat_run():

    # execution window:
    window = Tk()
    window.geometry('900x900')
    window.title("Invoice RPA")
    window.configure(background='#66b3ff')
    style_of_buttons = Style()
    style_of_buttons.configure('W.TButton', width=23, relief=GROOVE, activebackground="Red", borderwidth='4')

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
            json_path = get_list_of_jsons()[-1]
            data_from_json_with_new_consumption = get_json_with_new_consumption(f"{jsons_folder}\\{json_path}")
            customers = data_from_json_with_new_consumption
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
            run_reporter("no data detected to fill customer frame")


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
    printscreen_wrapper = Frame(window)
    printscreen_frame = ScrolledFrame(printscreen_wrapper)
    printscreen_frame.bind_arrow_keys(printscreen_wrapper)
    printscreen_frame.bind_scroll_wheel(printscreen_wrapper)
    inner_frame = printscreen_frame.display_widget(Frame)

    customer_table_label.pack()
    customers_frame.pack()
    invoices_label.pack()
    invoices_frame.pack()
    printscreen_label.pack()
    printscreen_wrapper.pack(side="bottom", expand=1, fill="both")
    printscreen_frame.pack(side="bottom", expand=1, fill="both")

    def refresh():
        global jsons_directory_len_old
        jsons_directory_len = len(get_list_of_jsons())
        customers_frame.delete(1.0, END)
        invoices_frame.delete(1.0, END)
        get_data_to_frame()
        fill_invoices_numbers_table()
        try:
            os.remove(f"{resources_folder}\\photos\\printscreen.png")
        except:
            pass
        if jsons_directory_len > jsons_directory_len_old:
            run_reporter("new consumption detected")
            invoice_creator()
            convert_xlsx_to_pdf()
            gmail_check()
            bkrgframe = BkgrFrame(inner_frame, printscreen, 900, 600)
            bkrgframe.grid()
            jsons_directory_len_old = jsons_directory_len
        else:
            pass

        window.after(3000, refresh)

    window.after(3000, refresh)
    window.mainloop()


automat_run()

