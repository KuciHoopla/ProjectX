import random
from datetime import datetime, timezone, timedelta

import xlsxwriter

from RPA.creators.variables.variables import photos_folder, excel_path, printscreen, jsons_folder
from creators.consumption.consumption_creator import get_json_with_new_consumption
from creators.directory_check.directory_check import get_list_of_jsons
from creators.runners.reporter import run_reporter


def invoice_creator():
    def get_price_kw(tariff):
        if tariff == 1:
            price_kw = 0.12
        elif tariff == 2:
            price_kw = 0.14
        elif tariff == 3:
            price_kw = 0.16
        elif tariff == 4:
            price_kw = 0.18
        elif tariff == 5:
            price_kw = 0.2
        return price_kw

    writer = xlsxwriter.Workbook(excel_path)
    logo = f'{photos_folder}\\logosmall.png'
    json_path = get_list_of_jsons()[-1]
    data_from_json_with_new_consumption = get_json_with_new_consumption(f"{jsons_folder}\\{json_path}")
    customers = data_from_json_with_new_consumption
    number_of_customers = len(customers)

    for customer in customers:
        id = customer["id"]
        first_name = customer["first_name"]
        last_name = customer["last_name"]
        address = customer["address"]
        consumption = customer["consumption"]
        tariff = customer["tariff"]
        invoice_no = f"2020{random.randrange(100, 999999)}"
        worksheet = writer.add_worksheet(name=id)
        footer = '&LDate: &D' + '&R Energy Kft, Berlin'
        worksheet.set_header('&L&G', {'image_left': logo})
        worksheet.hide_gridlines(3)
        date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        due_date = (datetime.now(timezone.utc) + timedelta(days=14)).strftime('%Y-%m-%d')
        customer_id = id
        price_kw = get_price_kw(tariff)
        total_consumption_price = price_kw * consumption
        total_distribution_price = price_kw * 12

        worksheet.set_column('A:E', 15)
        worksheet.set_row(18, 15)
        d2_format = writer.add_format()
        d2_format.set_font_size(25)
        worksheet.write('E2', "INVOICE", d2_format)
        table_format = writer.add_format()
        table_format.set_align("right")
        text_format = writer.add_format()
        text_format.set_bg_color("#e6f7ff")

        worksheet.write('E21', f'{round((total_distribution_price + total_consumption_price), 2)}€', table_format)
        worksheet.write('E22', f'{round((total_consumption_price), 2)}€', table_format)
        worksheet.write('E23', f'{20}%', table_format)
        worksheet.write('E24', f'{round((total_consumption_price * 0.2), 2)}€', table_format)
        worksheet.write('E25',
                        f'{round((total_distribution_price + total_consumption_price) + (total_consumption_price * 0.2), 2)}'
                        f'€', table_format)
        worksheet.write('D21', f'Subtotal: ')
        worksheet.write('D22', f'Taxable: ')
        worksheet.write('D23', f'Tax rate: ')
        worksheet.write('D24', f'Due: ')
        worksheet.write('D25', f'Total price: ')

        worksheet.write('A2', 'Suplier:')
        worksheet.write('A3', f'Energy Kft', text_format)
        worksheet.write('A4', f'Walking street 32', text_format)
        worksheet.write('A5', f'Berlin', text_format)
        worksheet.write('A6', f'Germany', text_format)

        worksheet.write('A11', f'Customer:')
        worksheet.write('A12', f'Name:', text_format)
        worksheet.write('A13', f'Last name:', text_format)
        worksheet.write('A14', f'Address:', text_format)

        worksheet.write('B12', f'{first_name}', text_format)
        worksheet.write('B13', f'{last_name}', text_format)
        worksheet.write('B14', f'{address}', text_format)
        worksheet.write('C12', f'', text_format)
        worksheet.write('C13', f'', text_format)
        worksheet.write('C14', f'', text_format)

        worksheet.write('D6', f'Date:', text_format)
        worksheet.write('D7', f'Invoice no.:', text_format)
        worksheet.write('D8', f'Customer ID:', text_format)
        worksheet.write('D9', f'Due date:', text_format)
        worksheet.write('E6', f'{date}', text_format)
        worksheet.write('E7', f'{invoice_no}', text_format)
        worksheet.write('E8', f'{customer_id}', text_format)
        worksheet.write('E9', f'{due_date}', text_format)

        data = [
            ['Consumption', tariff, price_kw, consumption, total_consumption_price],
            ['Distribution', 12, price_kw, 0, total_distribution_price],

        ]

        worksheet.add_table('A18:E20', {'data': data,
                                        'columns': [{'header': 'Product'},
                                                    {'header': 'Tariff'},
                                                    {'header': 'Price kw/h'},
                                                    {'header': 'Consumption'},
                                                    {'header': 'Amount'},
                                                    ]})

        worksheet.write('A33', f'1. Total payment due in 14 days', text_format)
        worksheet.write('A34', f'2. Please include the invoice number on your check', text_format)
        worksheet.write('B34', f'', text_format)
        worksheet.write('B33', f'', text_format)
        worksheet.write('C34', f'', text_format)
        worksheet.write('C33', f'', text_format)

        worksheet.insert_textbox('A38', 'Thank you for choosing Energy Kft. to supply your home energy.To ensure you get'
                                        'our best service, please keep your contact and account details up - todate. If'
                                        'you need to make any changes, you can do it online with MyAccount at'
                                        ' www.energykft.com / myaccount - sme', {'width': 580, 'height': 100})

        worksheet.set_footer(footer)

    run_reporter(f"xlsx file was created with {number_of_customers} sheets ")

    writer.close()



