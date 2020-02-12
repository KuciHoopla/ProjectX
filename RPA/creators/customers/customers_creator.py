import json
import names
from faker import Faker
from faker.generator import random
from pathlib import Path

from RPA.creators.variables.variables import customers_json, files_addressbook
from RPA.gmail_check.fake_face import fake_face

fake = Faker()


def create_customers_file(file_name):
    if not Path(file_name).exists():
        with open(file_name, 'w') as file:
            json.dump([], file)  # initialize file as empty list


def get_all_json_customers():
    with open(customers_json, 'r') as file:
        return json.load(file)


def get_all_files():
    with open(files_addressbook, 'r') as file:
        return json.load(file)


def get_new_consumption_json(last_file):
    with open(last_file, 'r') as file:
        return json.load(file)


def _save_all(file, customers):
    with open(file, 'w') as file:
        json.dump(customers, file)


def insert_customers(id, name, last_name, address, email, consumption, tariff,face):
    customers = get_all_json_customers()
    customers.append({
        "id": id,
        "first_name": name,
        "last_name": last_name,
        "address": address,
        "email": email,
        "consumption": consumption,
        "tariff": tariff,
        "face": face})
    _save_all(customers_json, customers)


def filling_json(number_of_customers):
    if len(get_all_json_customers()) < 1:
        i = 0
        faces = fake_face()
        while i < number_of_customers:
            first_name = names.get_first_name()
            last_name = names.get_last_name()
            address = fake.address()
            email = 'invoice.rpa.2020@gmail.com'
            # Automationproject2020
            random_num = random.randrange(100, 999999)
            id = "sx16" + str(random_num)
            consumption = random.randrange(200, 2000)
            tariff = random.randrange(1, 5)
            face = faces[random.randrange(30)]
            insert_customers(id, first_name, last_name, address, email, consumption, tariff, face)
            i += 1


def add_file_name_to_addressbook(last_file_name):
    if not Path(files_addressbook).exists():
        create_customers_file(files_addressbook)
    files = get_all_files()
    files.append(last_file_name)
    _save_all(files_addressbook, files)


def get_last_name_of_consumption_file():
    if not Path(files_addressbook).exists():
        create_customers_file(files_addressbook)
    files = get_all_files()
    last_file_name = files[-1]
    return last_file_name
