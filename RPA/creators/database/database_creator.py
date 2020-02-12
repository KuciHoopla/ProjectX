from RPA.creators.customers.customers_creator import *
from RPA.creators.database.database_connection import *
from RPA.creators.variables.variables import customers_database

database = customers_database


def create_customers_table():
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS customers('
                       'id text primary key,'
                       'first_name text,'
                       'last_name text,'
                       'address text,'
                       'email text, '
                       'consumption integer, '
                       'tariff integer, face text)')


def get_all_database_customers():
    try:
        with DatabaseConnection(database) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM customers')
            customers = [{'id': row[0],
                          'first_name': row[1],
                          'last_name': row[2],
                          'address': row[3],
                          'email': row[4],
                          'consumption': row[5],
                          'tariff': row[6],
                          'face': row[7]} for row in cursor.fetchall()]

        return customers
    except:
        create_customers_table()


def insert_customer(id, first_name, last_name, address, email, consumption, tariff, face):
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        new_id = id
        cursor.execute('INSERT INTO customers VALUES(?,?,?,?,?,?,?,?)', (new_id, first_name, last_name,
                                                                       address, email,
                                                                       consumption, tariff, face))


def update_customer_consumption_manually(new_consumption, id):
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE customers SET consumption=? WHERE id=?', (new_consumption, id))


def update_customer_consumption_from_json_data():
    consumption_data = get_new_consumption_json(get_last_name_of_consumption_file())
    for data in consumption_data:
        id = data.get("id")
        consumption = data.get("consumption")
        update_customer_consumption_manually(consumption, id)


def delete_customer(id):
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM customers WHERE id=?', (id,))


def fill_database_from_json():
    try:
        with open(customers_json, 'r') as file:
            customers = json.load(file)
            for customer in customers:
                id = customer.get("id")
                first_name = customer.get("first_name")
                last_name = customer.get("last_name")
                address = customer.get("address")
                email = customer.get("email")
                consumption = customer.get("consumption")
                tariff = customer.get("tariff")
                face = customer.get("face")
                insert_customer(id, first_name, last_name, address, email, consumption, tariff, face)
    except:
        return print("error")


def fill_customer_database(number_of_customers):
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
            insert_customer(id, first_name, last_name, address, email, consumption, tariff, face)
            i += 1


