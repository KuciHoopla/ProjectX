from datetime import datetime, timezone, timedelta
from creators.variables.variables import resources_folder

reporter = f'{resources_folder}reporter.txt'


def insert_report(passed=None, defect=None, invoice=None, customer_id=None):
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




