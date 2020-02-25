import random
import time

from creators.database.database_reporter import insert_report
from creators.directory_check.directory_check import get_list_of_jsons
from creators.excel.excel_invoice_creator import invoice_creator
from creators.pdf.convert_xlsx_to_pdf import convert_xlsx_to_pdf
from creators.runners.selenium_runner import selenium_add_customer, selenium_add_new_consumption, \
    selenium_create_database
from gmail_check.gmail_check import gmail_check

jsons_directory_len_old = 0


def command_line_runner():
    selenium_create_database()
    while True:
        random_num = random.randrange(1, 4)
        global jsons_directory_len_old
        jsons_directory_len = len(get_list_of_jsons())

        if jsons_directory_len > jsons_directory_len_old:
            insert_report(passed="JSON detected")
            invoice_creator()
            convert_xlsx_to_pdf()
            gmail_check()
            jsons_directory_len_old = jsons_directory_len
        else:
            pass
        selenium_add_customer(random_num)
        time.sleep(10)
        selenium_add_new_consumption()


command_line_runner()













