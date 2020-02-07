import os

from RPA.creators.consumption.consumption_creator import create_new_consumption
from RPA.creators.database.database_creator import create_customers_table, create_customers_file, customers_json, \
    filling_json, fill_database_from_json, update_customer_consumption_from_json_data
from RPA.creators.variables.variables import customers_database


def web_create_database(customers):
    create_customers_table()
    create_customers_file(customers_json)
    filling_json(customers)
    fill_database_from_json()


def web_delete_all_files():
    try:
        os.remove(customers_database)
        os.remove(customers_json)
    except:
        print("no database")


def web_create_new_consumption():
    create_new_consumption(),
    update_customer_consumption_from_json_data()






