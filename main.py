


import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from modules.connector import interface_db





def load_all_actors():
    st_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # get to the bottom of the current page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        # get the current height of it so you can know if something new was generated
        new_height = driver.execute_script("return document.body.scrollHeight")
        # If it has the same height, then it has nothing else to load. Quit
        if new_height == st_height:
            break;
        else:
            st_height = new_height







if __name__ == "__main__":

    your_email = os.environ['your_email']
    your_passwd = os.environ['your_passwd']
    root_url = "https://www.linkedin.com"
    db = "social.db"


    social_data = interface_db(db)

    

    #<gonna_get_out>
    create_actor = "CREATE TABLE IF NOT EXISTS actor ( \
    actor_id integer PRIMARY KEY AUTOINCREMENT,\
    actor_url text NOT NULL,\
    actor_name text default NULL\
    )"
    social_data.create_table(create_actor)

    #</gonna_get_out>

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get(root_url+'/login')
    time.sleep(3)


    email = driver.find_element(By.ID, "username")
    email.send_keys(your_email)
    passwd = driver.find_element(By.ID, "password")
    passwd.send_keys(your_passwd)
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()
    time.sleep(3)
    driver.get(root_url + '/feed/following')
    time.sleep(3)
    load_all_actors()

    profile_urls = driver.find_elements(By.CLASS_NAME, "follows-recommendation-card__avatar-link")

    # filters common accounts only and feed them to the sqlite
    profile_urls = [url.get_attribute('href') for url in profile_urls if url.get_attribute('href').__contains__("/in/")]
    for url in profile_urls:
        social_data.insertInto("actor", actor_url=url)




