import os
from RPA.creators.variables.variables import invoices_path, invoices_number_path
from creators.database.database_reporter import insert_report

invoices_path = invoices_path
invoices_number_path = invoices_number_path


def add_invoice_file(number):
    try:
        with open(invoices_path, 'a') as file:
            file.write(f'{number}\n')

    except:
        os.path.isfile(invoices_path)
        print("file exist")


def get_all_invoices():
    try:
        with open(invoices_path, 'r') as file:
            lines = [line.strip().split(',') for line in file.readlines()]
        return [
            {'number': line[0]}
            for line in lines
        ]
    except:
        add_invoice_file(1000)


def add_invoice_number(number):
    try:
        with open(invoices_number_path, 'a') as file:
            file.write(f'{number}\n')

    except:
        os.path.isfile(invoices_number_path)
        print("file exist")


def get_all_invoices_numbers():
    try:
        with open(invoices_number_path, 'r') as file:
            lines = file.read()

        return lines
    except:
        insert_report(defect="no invoices")







