from RPA.creators.database.database_creator import get_all_database_customers
from RPA.creators.database.database_invoices import add_invoice_file, get_all_invoices, add_invoice_number
from RPA.creators.excel.excel_invoice_creator import invoice_creator
from RPA.creators.pdf.convert_xlsx_to_pdf import convert_xlsx_to_pdf
from RPA.mail.send_mail import send_mail
from RPA.creators.variables.variables import pdfs_folder, jsons_folder
from creators.consumption.consumption_creator import get_json_with_new_consumption
from creators.directory_check.directory_check import get_list_of_jsons


def create_pdf():
    try:
        json_path = get_list_of_jsons()[-1]
        data_from_json_with_new_consumption = get_json_with_new_consumption(f"{jsons_folder}\\{json_path}")
        global counter
        counter = 1000
        customers = data_from_json_with_new_consumption
        for customer in customers:
            id = customer["id"]
            first_name = customer["first_name"]
            last_name = customer["last_name"]
            address = customer["address"]
            consumption = customer["consumption"]
            tariff = customer["tariff"]
            email = customer["email"]
            try:
                get_all_invoices()
            except:
                add_invoice_file(counter + 1)
                add_invoice_number(counter)
            counter = int(get_all_invoices()[-1].get("number"))
            number = f'2020-{counter}'
            invoice_creator(id, first_name, last_name, address, consumption, tariff)
            pdf_path = f'{pdfs_folder}\\invoice{number}.pdf'
            convert_xlsx_to_pdf()
            print(f"Invoice no. {number} was created")
            send_mail(pdf_path, email, number)
            print(f"Email with invoice no. {number} sent")
            add_invoice_file(counter+1)
            add_invoice_number(number)
    except:
        print("create pdf problem")

