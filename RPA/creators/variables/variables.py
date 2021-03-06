import os
from datetime import datetime, timezone


date = datetime.now(timezone.utc)
date = date.strftime('%Y-%m-%d-%H-%M-%S')


resources_folder = "C:\\Users\\JanKucera\\PycharmProjects\\Project\\RPA\\creators\\resources\\"
static_foler = "C:\\Users\\JanKucera\\PycharmProjects\\Project\\Web_gui\\static\\"

photos_folder = f'{resources_folder}\\photos'

excel_path = f'{resources_folder}\\template.xlsx'
pdfs_folder = f'{static_foler}\\photos\\pdfs'
jsons_folder = f'{resources_folder}\\jsons'
new_consumption_folder = f'{resources_folder}\\new_consumption'
chromedriver_path = f'{resources_folder}\\chromedriver\\chromedriver.exe'
geckodriver_path = f'{resources_folder}\\chromedriver\\geckodriver.exe'


faces_urls = f'{resources_folder}\\faces_url.json'
customers_json = f'{resources_folder}\\customers_file.json'
files_addressbook = f'{resources_folder}\\files_addressbook.json'
consumption_json = f'{new_consumption_folder}\\consumption-{date}.json'
customers_database = f'{resources_folder}\\customers.db'
bckg_picture = f"{photos_folder}\\bckg.png"
printscreens = f"{static_foler}\\photos\\printscreens"
invoices_path = f"{resources_folder}\\invoices.txt"
invoices_number_path = f"{resources_folder}\\invoices_numbers.txt"







