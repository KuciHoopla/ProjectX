import os

from RPA.creators.runners.command_line import description_ask_for_number, ask_for_number, \
    description_ask_for_creating_pdfs_and_send, ask_for_creating_pdfs_and_send
from RPA.creators.variables.variables import customers_database, customers_json, printscreen
from RPA.gmail_check.gmail_check import gmail_check


def launch():
    print(description_ask_for_number)
    ask_for_number()
    print(description_ask_for_creating_pdfs_and_send)
    ask_for_creating_pdfs_and_send()
    gmail_check()
    os.remove(customers_database)
    os.remove(customers_json)
    print("""
    __________________________________________________
    
    Process successful.
    All data deleted!
    __________________________________________________""")
















