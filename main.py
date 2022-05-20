import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium.Java
import time
from random import randrange
from fake_useragent import UserAgent

# from random import randrange
ua = UserAgent()
ua = ua.random

import requests
from bs4 import BeautifulSoup
import lxml
import json
import time

# import xlsxwriter

url = 'https://reinersuite.nrha.com/#/login'


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

with open('config.json', 'r', encoding='utf-8') as set_:
    set_data = json.load(set_)

set_email = set_data['set_email']
set_pass = set_data['set_pass']

print('start...')

# 1
#
# options = webdriver.FirefoxOptions()
# options.set_preference("general.useragent.override", f"{ua}")
# options.set_preference("dom.webnotifications.enabled", False);
#
# s = Service('geckodriver.exe')
#
# driver = webdriver.Firefox(service=s, options=options)


# #HERE IT FINDS THE PATH
# if getattr(sys, 'frozen', False):
#     application_path = os.path.dirname(sys.executable)
# else:
#     try:
#         app_full_path = os.path.realpath(__file__)
#         application_path = os.path.dirname(app_full_path)
#     except NameError:
#         application_path = os.getcwd()
#
# #Here we create the variable that is going to be used to all the functions for the path
# path = os.path.join(application_path)

chrome_path = ("./chromedriver.exe")

options = webdriver.ChromeOptions()
options.headless = False
options.add_argument("--incognito")
options.add_argument("start-maximized")
#
options.add_argument('--disable-blink-features=AutomationControlled')
#
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=options, executable_path=chrome_path)



browser.implicitly_wait(1.5)
browser.get(url)

time.sleep(2)
source_html = browser.page_source


# checkbox_xp = '//*[@id="checkbox1"]'
# start_time = time.time()
# try:
#     WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, checkbox_xp))).click()
# except:
#     pass
# finish_time = time.time() - start_time

email_xp = '//*[@id="content"]/div/div/section/div[2]/form/div[1]/div[1]/input'
in_email = browser.find_element(By.XPATH, email_xp)
in_email.send_keys(set_email)
time.sleep(1.1)

pass_xp = '//*[@id="content"]/div/div/section/div[2]/form/div[1]/div[2]/input'
in_pass = browser.find_element(By.XPATH, pass_xp)
in_pass.send_keys(set_pass)
time.sleep(1.2)

checkbox_xp = '//*[@id="content"]/div/div/section/div/form/div[2]/div/label'
checkbox = browser.find_element(By.XPATH, checkbox_xp).click()
time.sleep(0.7)

btn_login_xp = '//*[@id="content"]/div/div/section/div/form/div[3]/div/button'
btn_login = browser.find_element(By.XPATH, btn_login_xp).click()
time.sleep(0.9)



breakpoint()


# time.sleep(5)
# browser.close()
# browser.quit()
