import random
from RPA.creators.database.database_connection import *
from RPA.creators.variables.variables import customers_database
from creators.database.database_creator import get_all_database_customers
from datetime import datetime, timezone
database = customers_database


def create_table_personalised(customer_id):
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        customer_id = str(customer_id)
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {customer_id}('
                       'date text primary key,'
                       'consumption integer)')


def get_all_consumption_by_id(customer_id):
    try:
        with DatabaseConnection(database) as connection:
            cursor = connection.cursor()
            customer_id = str(customer_id)
            cursor.execute(f'SELECT * FROM {customer_id}')
            consumption_of_customer = [{'date': row[0],
                          'consumption': row[1]} for row in cursor.fetchall()]

        return consumption_of_customer
    except:
        create_table_personalised(customer_id)


def insert_consumption_to_customer(customer_id, consumption, date):
    try:
        with DatabaseConnection(database) as connection:
            cursor = connection.cursor()
            customer_id = str(customer_id)
            cursor.execute(f'INSERT INTO {customer_id} VALUES(?,?)', (date, consumption))
    except:
        create_table_personalised(customer_id)


def fill_customers_consumption():
    customers = get_all_database_customers()
    i = 0
    for customer in customers:
        id = customer["id"]
        i+=1
        j = 1
        for x in range(12):
            month = j
            date = f"{month}-01-2019"
            consumption = random.randrange(200, 2000)
            insert_consumption_to_customer(id, consumption, date)
            j += 1


def add_customers_consumption():
    customers = get_all_database_customers()
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d-%H-%M')
    print(stamp)
    for customer in customers:
        id = customer["id"]
        consumption = random.randrange(200, 2000)
        insert_consumption_to_customer(id, consumption, stamp)


def add_consumption_to_one_customer(id):
    j = 1
    for x in range(12):
        month = j
        date = f"{month}-01-2019"
        consumption = random.randrange(200, 2000)
        insert_consumption_to_customer(id, consumption, date)
        j += 1


