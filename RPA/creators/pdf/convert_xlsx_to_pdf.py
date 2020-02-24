import asyncio

import pythoncom
import win32com.client as client

from RPA.creators.variables.variables import excel_path, pdfs_folder
from creators.consumption.consumption_creator import get_json_with_new_consumption
from creators.database.database_invoices import get_all_invoices, add_invoice_file, add_invoice_number
from creators.database.database_reporter import insert_report
from creators.directory_check.directory_check import get_list_of_jsons
from creators.variables.variables import jsons_folder
from mail.send_mail import open_server
from mail.send_mail import send_mail


def convert_xlsx_to_pdf():
    pythoncom.CoInitialize()
    sender_email = "invoice.rpa.2020@gmail.com"

    async def send_email(sender_email, email, text):
        server.sendmail(sender_email, email, text)

    server = open_server()
    xl_App = client.Dispatch("Excel.Application")
    books = xl_App.Workbooks.Open(excel_path)
    json_path = get_list_of_jsons()[-1]
    data_from_json_with_new_consumption = get_json_with_new_consumption(f"{jsons_folder}\\{json_path}")
    customers = data_from_json_with_new_consumption
    global counter
    counter = 1000
    number_of_customers = len(customers)
    for customer in customers:
        try:
            get_all_invoices()
        except:
            add_invoice_file(counter + 1)
            add_invoice_number(counter)
        counter = int(get_all_invoices()[-1].get("number"))
        number = f'2020-{counter}'
        pdf_path = f'{pdfs_folder}\\invoice{number}.pdf'
        id = customer["id"]
        email = customer["email"]
        ws = books.Worksheets[id]
        ws.Visible = 1
        ws.ExportAsFixedFormat(0, pdf_path)
        insert_report(passed=f"Invoice no. {number} was created",
                      invoice=f'invoice{number}.pdf',
                      customer_id=id)
        text = send_mail(pdf_path, email, number)
        loop = asyncio.get_event_loop()
        tasks = [asyncio.ensure_future(send_email(sender_email, email, text))]
        insert_report(passed=f"Email with invoice no. {number} sent", customer_id=id)
        add_invoice_file(counter + 1)
        add_invoice_number(number)
    loop.run_until_complete(asyncio.wait(tasks))
    server.quit()
    books.Close(True)
    insert_report(passed=f"{number_of_customers} sheets from xlsx converted to pdfs")
    xl_App.Quit()






