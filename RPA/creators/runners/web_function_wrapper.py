import os
from RPA.creators.variables.variables import customers_database, resources_folder, static_foler
from shutil import rmtree


def web_delete_all_files():
    try:
        os.remove(customers_database)
    except:
        print("web delete all files fail = no database")

    try:
        os.remove(f"{resources_folder}\\template.xlsx")
    except:
        print("web delete all files fail = no template.xlsx")

    try:
        os.remove(f"{resources_folder}\\invoices_numbers.txt")
    except:
        print("web delete all files fail = no invoices_numbers.txt")

    try:
        os.remove(f"{resources_folder}\\invoices.txt")
    except:
        print("web delete all files fail = no invoices.txt")

    try:
        os.remove(f"{resources_folder}\\photos\\printscreen.png")
    except:
        print("web delete all files fail = no printscreen.png")

    try:
        os.remove(f"{resources_folder}\\reporter.txt")
    except:
        print("web delete all files fail = no reporter.txt")

    try:
        rmtree(f"{resources_folder}\\jsons")
        os.mkdir(f"{resources_folder}\\jsons")
    except:
        print("web delete all files fail = ")

    try:
        rmtree(f"{static_foler}\\photos\\pdfs")
        os.mkdir(f"{static_foler}\\photos\\pdfs")
    except:
        print("web delete all files fail = no pdfs directory")


    try:
        rmtree(f"{static_foler}\\photos\\printscreens")
        os.mkdir(f"{static_foler}\\photos\\printscreens")
    except:
        print("web delete all files fail = no printscreens directory")









