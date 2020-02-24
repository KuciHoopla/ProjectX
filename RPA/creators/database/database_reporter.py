from datetime import datetime, timezone, timedelta
from creators.variables.variables import resources_folder

reporter = f'{resources_folder}reporter.txt'


def insert_report(passed="", defect="", invoice="", customer_id=""):
    with open(reporter, 'a') as file:
        date = datetime.now(timezone.utc).strftime('%H:%M:%S %Y-%m-%d')
        file.write(f'{date}, {passed}, {defect}, {invoice}, {customer_id} \n')
    print(f"""
{date}
passed: {passed}
defect: {defect}
invoice: {invoice}
customer id: {customer_id}""")


def get_all_reports():
    try:
        with open(reporter, 'r') as file:
            lines = [line.strip().split(',') for line in file.readlines()]

        return [
            {'date': line[0], 'passed': line[1], 'defect': line[2], 'invoice': line[3], 'customer_id': line[4]}
            for line in lines
        ]

    except:
        insert_report()


def get_names_of_invoices():
    reports = get_all_reports()
    invoices = []
    for report in reports:
        invoice = report["invoice"]
        if len(invoice) > 5:
            invoices.append(invoice)
    return invoices


def get_number_of_invoices():
    invoices = get_names_of_invoices()
    invoices_len = len(invoices)
    return invoices_len


