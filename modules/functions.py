import os
from re import I
import time
from datetime import date
from random import uniform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup as bs


def load_all_actors(driver):
    """Triggers all actors by scrolling down untill everything loads."""
    st_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == st_height:
            break
        else:
            st_height = new_height


def slow_down(increment_by: int = 0):
    """Cooldown for 0.5 to 2.3 by default."""
    time.sleep(uniform((increment_by+0.5), (increment_by+2.3)))


def initialize_sqlite(social_data):
    files = [file for file in os.listdir("./ddl") if file.__contains__('sql')]
    for file in files:
        with open(f'./ddl/{file}') as sql:
            print()
            sql = sql.read()
            print(sql)
            social_data.create_table(sql)


def treat_date(date_string: str):
    """About function comment."""
    today = date.today()
    print(date_string)
    mes = {'jan': '.01', 'fev': '.02', 'mar': '.03',
           'abr': '.04', 'mai': '.05', 'jun': '.06',
           'jul': '.07', 'ago': '.08', 'set': '.09',
           'out': '.10', 'nov': '.11', 'dez': '.12'}
    try:
        exp_beg = date_string.split("-")[0][:-1]
        exp_beg = exp_beg.split(" ")[2]+mes[exp_beg.split(" ")[0]]
        exp_end = date_string.split("-")[1][:]
        if exp_end.__contains__("o momento"):
            current_year = today.strftime("%Y")
            current_month = today.strftime("%m")
            exp_end = current_year + "." + current_month
        else:
            exp_end = exp_end[1:].split(" ")[2]+mes[exp_end[1:].split(" ")[0]]
    except Exception as e:
        print(str(e))
        return " "," "
    else:
        return exp_beg, exp_end


def scrap_me(social_data, table: str, actor_id: int, section):
    """About function comment."""
    count = 0
    cards = section.select("li.artdeco-list__item")
    for card in cards:
        count = count+1
        if (len(card.find_all(attrs={"tabindex": "-1"})) > 1):
            exp_company = card.find_all(attrs={"aria-hidden": "true"})[0].text

            if table == 'experience':
                all_exp_name = card.select("div.display-flex>span.mr1, t-bold")
                exp_company = all_exp_name[0].span.text
                list_exp_name = [
                    (i.contents[1].text) for i in all_exp_name[1:]
                ]
                all_exp_date = card.select("div>*>span:nth-of-type(1).t-14 ,t-normal, t-black--light")
                list_exp_date = [
                    (i.contents[1].text) for i in all_exp_date[1:]
                ]
                for exp_name, exp_date in zip(list_exp_name, list_exp_date):
                    exp_beg, exp_end = treat_date(exp_date)
                    social_data.insert_into(table, actor_id=actor_id,
                                           exp_name=exp_name, exp_company=exp_company,
                                           exp_beg=exp_beg, exp_end=exp_end)
            elif table == 'education':
                print(" 33rr....you reached a list of ", table, " adding content for actor_id ", id, " ... you shouldn'be here, tho...")
            elif table == 'licenses_and_certifications':
                print(" 33rr....you reached a list of ", table, " adding content for actor_id ", id, " ... you shouldn'be here, tho...")
            elif table == 'courses':
                print(" 33rr....you reached a list of ", table, " adding content for actor_id ", id, " ... you shouldn'be here, tho...")
            elif table == 'skills':
                print(" 33rr....you reached a list of ", table, " adding content for actor_id ", id, " ... you shouldn'be here, tho...")

        else:
            if table == 'experience':
                try:
                    exp_name = card.select("span.mr1, t-bold")[0].span.text
                except Exception as e:
                    exp_name = " "
                try:
                    exp_company = card.select("span.t-14, t-normal")[0].span.text
                except Exception as e:
                    exp_company = " "
                try:
                    exp_date = card.select("span.t-14, t-normal")[1].span.text
                except Exception as e:
                    exp_date = " "

                exp_beg, exp_end = treat_date(exp_date)
                social_data.insert_into('experience', actor_id=actor_id,
                                       exp_name=exp_name, exp_company=exp_company,
                                       exp_beg=exp_beg, exp_end=exp_end)

            elif table == 'education':
                try:
                    edu_company = card.select("span.mr1, t-bold")[0].span.text
                except Exception as e:
                    edu_company = " "
                try:
                    edu_title = card.select("span.t-14, t-normal")[0].span.text
                except Exception as e:
                    edu_title = " "
                try:
                    exp_date = card.select("span.t-14, t-normal")[1].span.text
                except Exception as e:
                    exp_date = " "

                edu_beg, edu_end = treat_date(exp_date)
                social_data.insert_into('education', actor_id=actor_id,
                                       edu_company=edu_company, edu_title=edu_title,
                                       edu_beg=edu_beg, edu_end=edu_end)

            elif table == 'licenses_and_certifications':
                mes = {'jan': '.01', 'fev': '.02', 'mar': '.03', 'abr': '.04',
                       'mai': '.05', 'jun': '.06', 'jul': '.07', 'ago': '.08',
                       'set': '.09', 'out': '.10', 'nov': '.11', 'dez': '.12'}
                try:
                    lice_name = card.select("span.mr1, t-bold")[0].span.text
                except Exception as e:
                    lice_name = " "
                try:
                    lice_company = card.select("span.t-14, t-normal")[0].span.text
                except Exception as e:
                    lice_company = " "
                try:
                    lice_when = card.select("span.t-14, t-normal")[1].span.text
                except Exception as e:
                    lice_when = " "

                if (len(lice_when) > 10):
                    lice_when = lice_when.split("·")[0][11:]
                    lice_when = lice_when.split(" ")[2]+mes[lice_when.split(" ")[0]]
                else:
                    lice_when = ""
                social_data.insert_into('li_and_cert', actor_id=actor_id,
                                       lice_name=lice_name, lice_company=lice_company,
                                       lice_when=lice_when)

            elif table == 'courses':
                try:
                    course_name = card.select("span.mr1, t-bold")[0].span.text
                except Exception as e:
                    course_name = " "
                social_data.insert_into('course', actor_id=actor_id,
                                       course_name=course_name)
