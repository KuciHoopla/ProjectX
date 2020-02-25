from datetime import datetime, timezone
from random import random
from RPA.creators.customers.customers_creator import *
from RPA.creators.customers.customers_creator import _save_all
from RPA.creators.variables.variables import consumption_json, jsons_folder
from creators.database.database_creator import get_all_database_customers
from creators.database.id_table_creator import get_all_consumption_by_id, get_last_consumption_by_id

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


def create_json_of_new_consumption():
    customers = get_all_database_customers()
    customers_with_consumption = []
    for customer in customers:
        id = customer["id"]
        first_name = customer["first_name"]
        last_name = customer["last_name"]
        email = customer["email"]
        address = customer["address"]
        consumption = get_last_consumption_by_id(id)
        tariff = customer["tariff"]
        customers_with_consumption.append({
        "id": id,
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "email": email,
        "consumption": consumption,
        "tariff": tariff})
    print(customers_with_consumption)
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d-%H-%M-%S')
    file_path = f"{jsons_folder}\\{stamp}.json"
    with open(file_path, 'w') as file:
        json.dump(customers_with_consumption, file)


def get_json_with_new_consumption(json_path):
    with open(json_path, 'r') as file:
        return json.load(file)
