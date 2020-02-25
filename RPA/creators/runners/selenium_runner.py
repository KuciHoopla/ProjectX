import random
import time
import names
from faker import Faker
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from RPA.creators.variables.variables import chromedriver_path, geckodriver_path
from creators.database.database_reporter import insert_report


def selenium_add_customer(quantity):
    i = 0
    options = Options()
    options.headless = True
    # options.add_argument('start-maximized')
    driver = webdriver.Firefox(executable_path=geckodriver_path, options=options)
    driver.get('http://localhost:5000/')
    driver.find_element_by_id("admin_link").click()
    driver.find_element_by_id("inputEmail3").send_keys("admin")
    driver.find_element_by_id("inputPassword3").send_keys("admin")
    driver.find_element_by_class_name("btn-primary").click()
    while i < quantity:
        i += 1
        fake = Faker()
        username = names.get_first_name()
        surname = names.get_last_name()
        street = fake.address().replace('\n', '')
        num = random.randrange(5)
        email = "invoice.rpa.2020@gmail.com"

        try:
            driver.find_element_by_id("btn_add_customer").click()
            driver.find_element_by_id("inputEmail3").send_keys(username)
            driver.find_element_by_id("inputSurname").send_keys(surname)
            driver.find_element_by_id("inputAddress").send_keys(street)
            driver.find_element_by_id("inputEmail").send_keys(email)
            select = Select(driver.find_element_by_id("Tariff"))
            select.select_by_index(num)
            driver.implicitly_wait(5)
            driver.find_element_by_class_name("btn-primary").click()
            driver.find_element_by_id("admin_link").click()
        except:
            insert_report(defect="problem to add customer")
    driver.find_element_by_id("log_out").click()
    insert_report(passed=f"{quantity} new customers were added to database")
    driver.quit()


def selenium_add_new_consumption():
    options = Options()
    options.headless = True
    # options.add_argument('start-maximized')
    driver = webdriver.Firefox(executable_path=geckodriver_path, firefox_options=options)
    driver.get('http://localhost:5000/')
    driver.find_element_by_id("admin_link").click()
    driver.find_element_by_id("inputEmail3").send_keys("admin")
    driver.find_element_by_id("inputPassword3").send_keys("admin")
    driver.find_element_by_class_name("btn-primary").click()
    try:
        time.sleep(1)
        driver.find_element_by_id("admin_link").click()
        driver.find_element_by_id("btn_create_new_consumption").click()
        driver.find_element_by_id("log_out").click()
        driver.quit()
        insert_report(passed=f"new consumption created")
    except:
        insert_report(defect=f"problem to create new consumption it will try again")
        selenium_add_new_consumption()


def selenium_refresh_page():
    options = Options()
    driver = webdriver.Firefox(executable_path=geckodriver_path, options=options)
    driver.set_window_size(1200, 1000)
    driver.get('http://localhost:5000/')
    driver.find_element_by_id("admin_link").click()
    driver.find_element_by_id("inputEmail3").send_keys("admin")
    driver.find_element_by_id("inputPassword3").send_keys("admin")
    driver.find_element_by_class_name("btn-primary").click()
    while True:
        driver.refresh()
        time.sleep(10)


def selenium_create_database():
    options = Options()
    options.headless = True
    # options.add_argument('start-maximized')
    driver = webdriver.Firefox(executable_path=geckodriver_path, firefox_options=options)
    driver.get('http://localhost:5000/')
    driver.find_element_by_id("admin_link").click()
    driver.find_element_by_id("inputEmail3").send_keys("admin")
    driver.find_element_by_id("inputPassword3").send_keys("admin")
    driver.find_element_by_class_name("btn-primary").click()
    try:
        time.sleep(1)
        driver.find_element_by_id("admin_link").click()
        driver.find_element_by_id("btn_create").click()
        driver.find_element_by_id("log_out").click()
        driver.quit()
        insert_report(passed=f"database created")
    except:
        insert_report(defect=f"database exist")


