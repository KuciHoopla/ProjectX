import json
import random
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from RPA.creators.variables.variables import chromedriver_path, faces_urls


def create_file(file_name):
    if not Path(file_name).exists():
        with open(file_name, 'w') as file:
            json.dump([], file)


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
    create_file(faces_urls)
    with open(faces_urls, 'w') as file:
        json.dump(faces_url, file)
    print(faces_url)
    print(len(faces_url))
    driver.close()
    return faces_url


def get_random_face_url():
    with open(faces_urls, 'r') as file:
        urls = json.load(file)
        random_num = random.randrange(30)
        url = urls[random_num]
        return url

