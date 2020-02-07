import time
from creators.customers.customers_creator import create_customers_file, filling_json, customers_json, \
    get_all_json_customers
from creators.database.database_creator import create_customers_table, fill_database_from_json, \
    get_all_database_customers
from creators.pdf.create_pdf import create_pdf

description_ask_for_number = """
Invoice RPA

This program:
 - create database of customers and consumption of energy. 
 - create PDF from data of database and send mails to customers
 ______________________________________________________________
"""
description_ask_for_creating_pdfs_and_send = """
Database was created. 
Do you want to create and send invoices?

y = yes
n = no
 ______________________________________________________________
"""


def ask_for_number():
    try:
        number = int(input("Please enter a number: "))
        if number > 0:
            create_customers_file(customers_json)
            print(f"Json created with {number} customers")
            filling_json(number)
            print(f"Json filled with {number} customers")
            print(get_all_json_customers())
            create_customers_table()
            fill_database_from_json()
            print("Database filled from json")
            print(get_all_database_customers())
        else:
            print('Please enter a number greater than zero!')
    except:
        print('Please enter a number!')


def ask_for_creating_pdfs_and_send():
    letter = input("Enter letter 'y' or 'n': ")
    if letter == 'y':
        create_pdf()
    elif letter == 'n':
        quit()
    else:
        print('Please enter "y" or "n"')
        ask_for_creating_pdfs_and_send()


