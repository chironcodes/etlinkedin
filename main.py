"""

"""


import os
from re import I
import time
from datetime import date
from random import uniform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup as bs

from modules.connector import InterfaceDB
from modules.user import User
from modules.functions import *


if __name__ == "__main__":
    desired = ['experience', 'education', 'licenses_and_certifications', 'courses']
    root_url = "https://www.linkedin.com"
    user = User(os.environ['your_email'], os.environ['your_passwd'])
    root_url = "https://www.linkedin.com"
    db = "social.db"
    social_data = InterfaceDB(db)
    initialize_sqlite(social_data)
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get(root_url+'/login')
    time.sleep(3)
    email = driver.find_element(By.ID, "username")
    email.send_keys(user.email)
    passwd = driver.find_element(By.ID, "password")
    passwd.send_keys(user.password)
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()
    time.sleep(3)
    driver.get(root_url + '/feed/following')
    time.sleep(3)
    load_all_actors(driver)
    profile_urls = driver.find_elements(By.CLASS_NAME, "follows-recommendation-card__avatar-link")
    profile_urls = [url.get_attribute('href').split("/in/")[1][:-1] for url in profile_urls if url.get_attribute('href').__contains__("/in/")]
    for url in profile_urls:       
        actor_url = root_url+"/in/"+url
        driver.get(actor_url)
        try:
            elem = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//*[@aria-label='Mais ações']"))
            )
        except Exception as e:
            print(str(e))
            time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        newHeight = driver.execute_script("return document.body.scrollHeight")
        profile = bs(driver.page_source.encode("utf-8"), "lxml")
        all_sections = profile.find_all("section", class_="artdeco-card ember-view break-words pb3 mt4")
        inserted_id = social_data.insert_into('actor', actor_url=actor_url)
        for section in all_sections:
            section_name = section.div.get("id")
            if(section_name in desired):
                print(section_name)
                scrap_me(social_data, section_name, inserted_id, section)