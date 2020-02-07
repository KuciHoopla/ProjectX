import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from RPA.creators.variables.variables import chromedriver_path


def fake_face():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver_path)

    driver.get('https://www.pexels.com/search/portrait/')
    driver.execute_script("window.scrollTo(0, 8000)")
    faces = driver.find_elements_by_css_selector("img.photo-item__img")
    faces_url = []
    for face in faces:
        face = face.get_attribute("src")
        faces_url.append(face)
    print(faces_url)
    print(len(faces_url))
    driver.close()
    return faces_url

