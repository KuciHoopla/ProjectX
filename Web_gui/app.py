import os
import random

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from creators.variables.variables import static_foler
from RPA.creators.database.database_creator import DatabaseConnection, database, get_all_database_customers, \
    insert_customer, fill_customer_database
from RPA.creators.runners.web_function_wrapper import web_delete_all_files
from creators.consumption.consumption_creator import create_json_of_new_consumption
from creators.database.database_reporter import insert_report, get_all_reports
from creators.database.id_table_creator import get_all_consumption_by_id, fill_customers_consumption, \
    add_consumption_to_one_customer, add_customers_consumption
from gmail_check.fake_face import get_random_face_url

flask_app = Flask(__name__)
flask_app.secret_key = b'\x8eJ|P7\x8c\xe6X\xb3\x9c\xaf\x17C\xbaz\x17\xbb\xc81`_\xe3\xac\xc2'


@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja2")


@flask_app.route("/admin/create_database")
def view_create_database():
    fill_customer_database(10)
    fill_customers_consumption()
    insert_report(passed="database created from website")
    return render_template("admin.jinja2")


@flask_app.route("/admin/delete_all_files")
def view_delete_all_files():
    web_delete_all_files()
    insert_report(passed="all data deleted by click on website")
    return render_template("admin.jinja2")


@flask_app.route("/admin/create_new_consumption")
def view_create_new_consumption():
    add_customers_consumption()
    create_json_of_new_consumption()
    insert_report(passed="consumption created from website")
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
        insert_report(passed="admin signed in")
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
        tariff = int(request.form["tariff"])
        consumption = 0
        if first_name != "" and last_name != "" and email != "":
            face = get_random_face_url()
            random_num = random.randrange(100, 999999)
            id = "sx" + str(random_num)
            insert_customer(id, first_name, last_name, address, email, consumption, tariff, face)

            with DatabaseConnection(database) as connection:
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM customers WHERE id=(?)', [id])
                customer = cursor.fetchone()
                # add_consumption_to_one_customer(id)
                if customer:
                    insert_report(passed=f"customer id: {id} created")
                    return render_template("customer.jinja2", customer=customer)
        else:
            return render_template("add_customer.jinja2")

    else:
        return render_template("add_customer.jinja2")


@flask_app.route("/logout/", methods=["POST"])
def logout_user():
    session.pop("logged")
    insert_report(passed=f"admin logged-out")
    return redirect(url_for("view_welcome_page"))


@flask_app.route("/tags/")
def view_reporter_tags():
    reports = get_all_reports()
    return render_template("reporter_tags.jinja2", reports=reports)


@flask_app.route("/reporter/")
def view_reporter_overview():
    reports = get_all_reports()
    return render_template("reporter_overview.jinja2", reports=reports)


@flask_app.route("/invoices/")
def view_reporter_invoices():
    paths = []
    try:
        invoices = os.listdir(f'{static_foler}\\photos\\pdfs')
        for invoice in invoices:
            path = f"photos/pdfs/{invoice}"
            paths.append(path)
    except:
        pass
    return render_template("reporter_invoices.jinja2", paths=paths)


@flask_app.route("/screenshots/")
def view_reporter_screenshots():
    paths = []
    try:
        screenshots = os.listdir(f'{static_foler}\\photos\\printscreens')
        for shot in screenshots:
            path = f"photos/printscreens/{shot}"
            paths.append(path)
    except:
        pass

    return render_template("reporter_screenshots.jinja2", paths=paths)


if __name__ == "__main__":
    debug = True
    host = "0.0.0.0"
    flask_app.run(host, debug=debug)

