import random
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from RPA.creators.database.database_creator import DatabaseConnection, database, get_all_database_customers, \
    fake_face, insert_customer, fill_customer_database
from RPA.creators.runners.web_function_wrapper import web_delete_all_files, \
    web_create_new_consumption, web_create_database
from creators.database.id_table_creator import get_all_consumption_by_id

flask_app = Flask(__name__)
flask_app.secret_key = b'\x8eJ|P7\x8c\xe6X\xb3\x9c\xaf\x17C\xbaz\x17\xbb\xc81`_\xe3\xac\xc2'


@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja2")


@flask_app.route("/admin/create_database")
def view_create_database():
    fill_customer_database(10)
    return render_template("admin.jinja2")


@flask_app.route("/admin/delete_all_files")
def view_delete_all_files():
    web_delete_all_files()
    return render_template("admin.jinja2")


@flask_app.route("/admin/create_new_consumption")
def view_create_new_consumption():
    web_create_new_consumption()
    return render_template("admin.jinja2")


@flask_app.route("/admin/", methods=["GET"])
def view_admin():
    if "logged" not in session:
        return redirect(url_for("view_login"))
    customers = get_all_database_customers()
    return render_template("admin.jinja2", customers=customers)


@flask_app.route("/admin/<id>/")
def view_customer(id):
    with DatabaseConnection(database) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM customers WHERE id=(?)', [id])
        customer = cursor.fetchone()
        consumptions = get_all_consumption_by_id(id)
        if customer:
            return render_template("customer.jinja2", customer=customer, consumptions=consumptions)
    return render_template("customer_not_found.jinja2", id=id)


@flask_app.route("/login/", methods=["GET"])
def view_login():
    return render_template("login.jinja2")


@flask_app.route("/login/", methods=["POST"])
def login_user():
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "admin":
        session["logged"] = True
        return redirect(url_for("view_admin"))
    else:
        return redirect(url_for("view_login"))


@flask_app.route("/add_customer/", methods=['GET', 'POST'])
def add_customer():
    if request.method == "POST":
        first_name = request.form["username"]
        last_name = request.form["surname"]
        email = request.form["email"]
        address = request.form["address"]
        consumption = int(request.form["consumption"])
        tariff = int(request.form["tariff"])
        if first_name != "" and last_name != "" and email != "":
            faces = fake_face()
            face = faces[random.randrange(30)]
            random_num = random.randrange(100, 999999)
            id = "sx" + str(random_num)
            insert_customer(id, first_name, last_name, address, email, consumption, tariff, face)
            print(get_all_database_customers())
            with DatabaseConnection(database) as connection:
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM customers WHERE id=(?)', [id])
                customer = cursor.fetchone()
                if customer:
                    return render_template("customer.jinja2", customer=customer)
        else:
            return render_template("add_customer.jinja2")

    else:
        return render_template("add_customer.jinja2")


@flask_app.route("/logout/", methods=["POST"])
def logout_user():
    session.pop("logged")
    return redirect(url_for("view_welcome_page"))


if __name__ == "__main__":
    debug = True
    host = "0.0.0.0"
    flask_app.run(host, debug=debug)
