import os

from RPA.creators.customers.customers_creator import *
from RPA.creators.database.database_connection import *
from RPA.creators.variables.variables import customers_database
invoices_path = r"..\RPA\creators\resources\invoices.txt"
invoices_number_path = r"..\RPA\creators\resources\invoices_numbers.txt"


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
    with open(invoices_number_path, 'r') as file:
        lines = file.read()

    return lines







