import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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

# import datetime
from datetime import datetime
from calendar import monthrange
current_year = datetime.now().year



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


# # ===================================================================================================================
# # ===================================================================================================================
# # ===================================================================================================================
# #
# # START of "collecting links"
# #
browser.implicitly_wait(1.5)
browser.get(url)
time.sleep(2)


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

gear_xp = '//*[@id="app"]/nav[2]/div/div[2]/ul[1]/li/a/i'
start_time = time.time()
try:
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, gear_xp)))
except:
    pass
finish_time = time.time() - start_time
print(finish_time)

# browser.implicitly_wait(1.5)
# url_new = 'https://reinersuite.nrha.com/#/app/events/my-events'
# browser.get(url_new)
# time.sleep(2)
#
# tab_event_finder_xp = '//*[@id="summary-tab"]'
# tab_event_finder = browser.find_element(By.XPATH, tab_event_finder_xp).click()
#
# # choose month
# #
# date_m = int(input('Select month! For example: 1 (JANUARY will be parsed) : '))
# # date_m = 1 # TEST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# date_from_xp = '//*[@id="q-datepicker_3"]'
# date_from = browser.find_element(By.XPATH, date_from_xp)
# date_from.clear()
#
# if date_m < 10:
#     date_from.send_keys(f'0{date_m}/01/2022')
# else:
#     date_from.send_keys(f'{date_m}/01/2022')
#
# time.sleep(0.5)
# date_from.send_keys(Keys.RETURN)
# time.sleep(0.5)
# # ------------------------------------------------------
# days = monthrange(current_year, month)[1]
# # ------------------------------------------------------
# date_to_xp = '//*[@id="q-datepicker_5"]'
# date_to = browser.find_element(By.XPATH, date_to_xp)
#
# if date_m < 10:
#     # date_to.send_keys(f'04/{days}/2022') # TEST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     date_to.send_keys(f'{date_m}/{days}/2022')
# else:
#     # date_to.send_keys(f'04/{days}/2022') # TEST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     date_to.send_keys(f'{date_m}/{days}/2022')
#
# time.sleep(0.5)
# date_to.send_keys(Keys.RETURN)
# time.sleep(1)
#
# btn_search_xp = '//*[@id="finder"]/event-find/div/div/section/div/form/fieldset/div[2]/input[1]'
# btn_search = browser.find_element(By.XPATH, btn_search_xp).click()
#
# # clear file...
# with open('urls.txt', 'w+', encoding='utf-8') as file:
#     file.write('')
#
# for p_ in range(2, 100):
#     pag_xp = f'//*[@id="finder"]/div/div/table/tfoot/tr/td/mfbootstrappaginator/mfpaginator/ul[1]/li[{p_}]/a'
#     print(pag_xp)
#     if p_ > 2:
#         try:
#             pag = browser.find_element(By.XPATH, pag_xp).click()
#         except:
#             breakpoint()
#
#
#     for i in range(1, 11):
#         # print(f'TRY: {i} X-PATH')
#         # for j in range(10):  # adjust integer value for need
#         #     try:
#         #         tit_ = driver.find_element(By.XPATH, f'//*[@id="exhibitor-directory"]/div/div/div/div[2]/div[3]/div/ul/div[{i}]/div/div[2]/div/div[1]/div[1]/div[1]/a/h3')  # )).click()
#         #         break
#         #     except:
#         #         driver.execute_script("window.scrollBy(0, 20000)")
#         #     print(j)
#         #     time.sleep(1)
#
#         # time.sleep(0.5)
#
#
#         a_s = f'#finder > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(1) > a'
#         a_ = browser.find_elements(By.CSS_SELECTOR, a_s)
#
#         link = [elem.get_attribute('href') for elem in a_]
#
#         print(link)
#
#         # write links to file
#         with open('urls.txt', 'a', encoding='utf-8') as file:
#             for url in link:
#                 file.write(f'{url}\n')
#     print(f'\n==========================================\n')
# #
# # END of "collecting links"
# #
# # ===================================================================================================================
# # ===================================================================================================================
# # ===================================================================================================================



# читаю ССЫЛКИ из ранее созданного файла
# !!! ОБРЕЗАЮ СИМВОЛ ПЕРЕНОСА СТРОКИ !!!
with open('urls.txt') as file:
    url_list = [line.strip() for line in file.readlines()]

# СЧЁТЧИК количества ЛОТОВ(ссылок)
url_count = len(url_list)
print(url_count)

browser.implicitly_wait(1.5)



for url in url_list:

    rows_ = []
    browser.get(url)
    time.sleep(2)

    results_xp = '//*[@id="content"]/div/div/div/div/div/section/div/div[2]/ul/li[2]/a'
    results = browser.find_element(By.XPATH, results_xp).click()
    time.sleep(0.5)

    select_box = Select(browser.find_element(By.NAME, 'selectedClass'))
    options = [x.text for x in select_box.options]

    for pos in options:
        # select_box = Select(browser.find_element(By.NAME, 'selectedClass'))
        # select_box.selectByVisibleText(pos)
        print(pos)


        select_box.select_by_visible_text(pos)


        number_xp = '//*[@id="content"]/event-results/div/section[1]/div/div/event-info/div/div/section/div/div[1]/div[1]/p[2]'
        number = (browser.find_element(By.XPATH, number_xp).text.split(':')[-1]).strip()
        print(number)

        # mm/dd/yyyy
        data_xp = '//*[@id="content"]/event-results/div/section[1]/div/div/event-info/div/div/section/div/div[2]/div[1]/p'
        data_ = browser.find_element(By.XPATH, data_xp).text
        data = datetime.strptime(data_, '%m/%d/%Y').strftime('%Y%m%d')

        name_xp = '//*[@id="content"]/event-results/div/section[1]/div/div/event-info/div/div/section/div/div[1]/div[1]/p[1]/a'
        name = browser.find_element(By.XPATH, name_xp).text

        title_xp = '//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[2]/div/h4[1]'
        title = browser.find_element(By.XPATH, title_xp).text


        for tr_ in range(1, 100):
            tr_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]'
            print(f'TR: {tr_}')
            try:
                browser.find_element(By.XPATH, tr_xp)
            except:
                break

            # NEW items to file
            items_ = []
            tr_new = []
            # PLACING	BACK#	HORSE	RIDER	OWNER	SCORE	EARNINGS(USD)
            xp_ = '//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[1]/td['
            for h in range(1, 8):
                elem_xp = f'{xp_}{h}]'
                tr_new.append(browser.find_element(By.XPATH, elem_xp).text)

            items_.append({
                "PLACING": tr_new[0],
                "BACK#": tr_new[1],
                "HORSE": tr_new[2],
                "RIDER": tr_new[3],
                "OWNER": tr_new[4],
                "SCORE": tr_new[5],
                "EARNINGS(USD)": tr_new[6]}
            )

        with open(f'{data}_{number}_{title}.json', 'a', encoding='utf-8') as file:
            json.dump(items_, file, indent=4, ensure_ascii=False)


        print(f'{data}_{number}')


        breakpoint()
        #select_box.selectByIndex(1)
    # print(options)



    print('*****************************************')


browser.close()
browser.quit()






#***************************************************
#
source_html = browser.page_source
time.sleep(0.7)
browser.close()
browser.quit()

with requests.Session() as session:
    # response = session.get(url=url, headers=headers)
    soup = BeautifulSoup(source_html, 'lxml')

print(soup)
pagination = soup.find('ul', class_='pagination').text.strip()
print(pagination)
#
#***************************************************





def main():
    pass

if __name__ == '__main__':
    main()

# time.sleep(5)
# browser.close()
# browser.quit()
