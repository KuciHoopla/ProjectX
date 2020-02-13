import time

from PIL import Image
from selenium import webdriver
from RPA.creators.variables.variables import chromedriver_path, printscreen


def gmail_check():
    driver = webdriver.Chrome(chromedriver_path)
    driver.get('https://mail.google.com/')
    driver.find_element_by_id("identifierId").send_keys("invoice.rpa.2020@gmail.com")
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(10)
    driver.find_element_by_class_name("A37UZe").click()
    driver.find_element_by_class_name("whsOnd").send_keys("Automationproject2020")
    driver.find_element_by_id("passwordNext").click()
    time.sleep(3)
    driver.save_screenshot(printscreen)
    # Image.open(printscreen).show()
    driver.find_element_by_class_name("T-Jo").click()
    driver.find_element_by_class_name("asa").click()
    time.sleep(3)
    driver.close()

