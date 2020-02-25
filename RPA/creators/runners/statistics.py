import os

from creators.database.database_creator import get_all_database_customers
from creators.database.database_reporter import get_all_reports
from creators.variables.variables import static_foler


def number_of_customers():
    customers = get_all_database_customers()
    number = len(customers)
    return number


def number_of_passed_actions():
    reports = get_all_reports()
    passed_tags = []
    for report in reports:
        passed_tag = report["passed"]
        if len(passed_tag) > 1:
            passed_tags.append(passed_tag)

    number = len(passed_tags)
    return number


def number_of_defects():
    reports = get_all_reports()
    passed_tags = []
    for report in reports:
        passed_tag = report["defect"]
        if len(passed_tag) > 1:
            passed_tags.append(passed_tag)

    number = len(passed_tags)
    return number


def number_of_created_invoices():
    invoices = os.listdir(f'{static_foler}\\photos\\pdfs')
    number = len(invoices)
    return number


def number_of_created_screenshots():
    screenshots = os.listdir(f'{static_foler}\\photos\\printscreens')
    number = len(screenshots)
    return number




