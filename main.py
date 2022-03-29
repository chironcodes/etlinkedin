


import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from modules.connector import interface_db







if __name__ == "__main__":

    your_email = os.environ['your_email']
    your_passwd = os.environ['your_passwd']
    root_url = "https://www.linkedin.com"
    db = "social.db"


    social_info = interface_db(db)

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get(root_url + '/feed/following')
    time.sleep(3)


    email = driver.find_element(By.ID, "username")
    email.send_keys(your_email)
    passwd = driver.find_element(By.ID, "password")
    passwd.send_keys(your_passwd)
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()
    time.sleep(3)



