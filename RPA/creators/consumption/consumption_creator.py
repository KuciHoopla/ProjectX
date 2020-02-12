from random import random
from RPA.creators.customers.customers_creator import *
from RPA.creators.customers.customers_creator import _save_all
from RPA.creators.variables.variables import consumption_json

last_consumption_file_name = ""


def create_new_consumption():
    global last_consumption_file_name
    create_customers_file(consumption_json)
    create_customers_file(files_addressbook)
    last_consumption_file_name = consumption_json
    customers = get_all_json_customers()
    new_data = []
    for customer in customers:
        id = customer.get("id")
        consumption = random.randrange(200, 2000)
        new_data.append({
            "id": id,
            "consumption": consumption})
    _save_all(last_consumption_file_name, new_data)
    add_file_name_to_addressbook(last_consumption_file_name)




