import time
from datetime import datetime, timezone

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from RPA.creators.variables.variables import printscreens, geckodriver_path
from creators.database.database_reporter import insert_report


def gmail_check():
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d-%H:%M")
    options = Options()
    options.headless = True
    # options.add_argument('start-maximized')
    driver = webdriver.Firefox(executable_path=geckodriver_path, firefox_options=options)
    try:
        driver.get('https://mail.google.com/')
        driver.find_element_by_id("identifierId").send_keys("invoice.rpa.2020@gmail.com")
        time.sleep(1)
        driver.find_element_by_id("identifierNext").click()
        time.sleep(1)
        driver.implicitly_wait(10)
        driver.find_element_by_class_name("MQL3Ob").click()
        driver.find_element_by_class_name("whsOnd").send_keys("Automationproject2020")
        driver.find_element_by_id("passwordNext").click()
        time.sleep(3)
        driver.save_screenshot(f'{printscreens}\\{date}.png')
        # Image.open(printscreen).show()
        driver.find_element_by_class_name("T-Jo").click()
        driver.find_element_by_class_name("asa").click()
        time.sleep(5)
        insert_report(passed="printscreen created")

    except:
        insert_report(defect="problem to check gmail, it will try again")
        driver.close()
        gmail_check()

    finally:
        driver.close()


