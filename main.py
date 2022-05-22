from pathlib import Path

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
#month = 3


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

chrome_path = "./chromedriver.exe"

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

# # # ===================================================================================================================
# # # ===================================================================================================================
# # # ===================================================================================================================
# # #
# # # START of "login"
# # #
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
# # #
# # # END of "login"
# # #
# # # ===================================================================================================================
# # # ===================================================================================================================
# # # ===================================================================================================================
# # #
# # # START of "collecting links"
# # #
browser.implicitly_wait(1.5)
url_new = 'https://reinersuite.nrha.com/#/app/events/my-events'
browser.get(url_new)
time.sleep(2)

tab_event_finder_xp = '//*[@id="summary-tab"]'
tab_event_finder = browser.find_element(By.XPATH, tab_event_finder_xp).click()

# choose year
#
date_y = int(input('Select year! For example: 2022 : '))

# choose month
#
date_m = int(input('Select month! For example: 1 (JANUARY will be parsed) : '))
# date_m = 1 # TEST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

date_from_xp = '//*[@id="q-datepicker_3"]'
date_from = browser.find_element(By.XPATH, date_from_xp)
date_from.clear()

if date_m < 10:
    date_from.send_keys(f'0{date_m}/01/{date_y}')
else:
    date_from.send_keys(f'{date_m}/01/{date_y}')

time.sleep(0.5)
date_from.send_keys(Keys.RETURN)
time.sleep(0.5)
# ------------------------------------------------------
#days = monthrange(current_year, date_m)[1]
days = monthrange(date_y, date_m)[1]
# ------------------------------------------------------
date_to_xp = '//*[@id="q-datepicker_5"]'
date_to = browser.find_element(By.XPATH, date_to_xp)

if date_m < 10:
    # date_to.send_keys(f'04/{days}/2022') # TEST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    date_to.send_keys(f'{date_m}/{days}/{date_y}')
else:
    # date_to.send_keys(f'04/{days}/2022') # TEST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    date_to.send_keys(f'{date_m}/{days}/{date_y}')

time.sleep(0.5)
date_to.send_keys(Keys.RETURN)
time.sleep(1)

btn_search_xp = '//*[@id="finder"]/event-find/div/div/section/div/form/fieldset/div[2]/input[1]'
btn_search = browser.find_element(By.XPATH, btn_search_xp).click()

# clear file...
with open('urls.txt', 'w+', encoding='utf-8') as file:
    file.write('')

for p_ in range(2, 30):
    pag_xp = f'//*[@id="finder"]/div/div/table/tfoot/tr/td/mfbootstrappaginator/mfpaginator/ul[1]/li[{p_}]/a'
    print(pag_xp)
    if p_ > 2:
        try:
            pag = browser.find_element(By.XPATH, pag_xp).click()
        except:
            pass

    lnk_p_count = 0
    for i in range(1, 11):

        lnk_p_count += 1

        a_s = f'#finder > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(1) > a'
        a_ = browser.find_elements(By.CSS_SELECTOR, a_s)

        link = [elem.get_attribute('href') for elem in a_]

        if not link:
            print('EMPTY...')
            lnk_p_count = 555
            break
        else:
            print(f'{lnk_p_count} --- > {link}')
            time.sleep(0.3)
            # write links to file
            with open('urls.txt', 'a', encoding='utf-8') as file:
                for url in link:
                    file.write(f'{url}\n')
    if lnk_p_count == 555:
        break
    print(f'\n==========================================\n')


#
# END of "collecting links"
#
# ===================================================================================================================
# ===================================================================================================================
# ===================================================================================================================


# breakpoint()


def gear_time():
    gear_xp = '//*[@id="app"]/nav[2]/div/div[2]/ul[1]/li/a/i'
    start_time = time.time()
    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, gear_xp)))
    except:
        pass
    finish_time = time.time() - start_time
    print(f'GEAR: {finish_time}')

def results_time():
    results_xp = '//*[@id="content"]/div/div/div/div/div/section/div/div[2]/ul/li[2]/a'
    start_time = time.time()
    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, results_xp)))
    except:
        pass
    finish_time = time.time() - start_time
    print(f'RESULTS_time: {finish_time}')



def refrash_time():
    refresh_time_xp = '//*[@id="content"]/event-results/div/section[2]/div/div/div[2]/button'
    start_time = time.time()
    try:
        WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element(By.XPATH, refresh_time_xp))
    except:
        pass
    finish_time = time.time() - start_time
    print(f'DATA_TO_DAY_time: {finish_time}')


def data_today_time():
    # refresh_time_xp = '//*[@id="content"]/event-results/div/section[2]/div/div/div[2]/button'
    data_today_xp = '//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[1]/div/span'
    start_time = time.time()
    try:
        WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element(By.XPATH, data_today_xp)) # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, data_today_xp)))
    except:
        pass
    finish_time = time.time() - start_time
    print(f'DATA_TO_DAY_time: {finish_time}')

def links_with_no_results(url):
    with open('links_with_no_results.txt', 'a', encoding='utf-8') as file:
                file.write(f'{url}\n')



with open('urls.txt') as file:
    url_list = [line.strip() for line in file.readlines()]

url_count = len(url_list)
print(url_count)

browser.implicitly_wait(1.5)

for url in url_list:

    rows_ = []
    browser.get(url)
    time.sleep(0.3)
    browser.get(url)



    #time.sleep(3)
    results_time()

    # find "Results"
    res_bool = False
    results_xp = '//*[@id="content"]/div/div/div/div/div/section/div/div[2]/ul/li[2]/a'
    try:
        results = browser.find_element(By.XPATH, results_xp).click()
        res_bool = True
    except:
        links_with_no_results(url)

    if res_bool:
        refrash_time()
        time.sleep(0.5)
        # mm/dd/yyyy
        data_xp = '//*[@id="content"]/event-results/div/section[1]/div/div/event-info/div/div/section/div/div[2]/div[1]/p'
        data_ = browser.find_element(By.XPATH, data_xp).text
        data = datetime.strptime(data_, '%m/%d/%Y').strftime('%Y%m%d')

        name_count = 0
        name_xp = '//*[@id="content"]/event-results/div/section[1]/div/div/event-info/div/div/section/div/div[1]/div[1]/p[1]/a'
        try:
            name = browser.find_element(By.XPATH, name_xp).text
            print('YES!!!')
            name_count = 1
        except:
            pass

        if name_count == 0:
            name_xp = '//*[@id="content"]/event-results/div/section[1]/div/div/event-info/div/div/section/div/div[1]/div[1]/p[1]'
            name = (browser.find_element(By.XPATH, name_xp).text.split(":")[-1]).strip()
            print(name)

        # path_name = f"./out/{data}_{name}"
        #
        # # directory
        # Path(path_name).mkdir(parents=True, exist_ok=True)
        # print(f'PATH: {path_name}')
        # print('-----------------------')
        #
        # # write link to file
        # with open(f'{path_name}/___url.txt', 'a', encoding='utf-8') as file:
        #     file.write(f'{url}\n')

        select_box = Select(browser.find_element(By.NAME, 'selectedClass'))
        options = [x.text for x in select_box.options]

        pos_num = 1

        for pos in options:
            # select_box = Select(browser.find_element(By.NAME, 'selectedClass'))
            # select_box.selectByVisibleText(pos)
            print(pos)

            select_box.select_by_visible_text(pos)

            data_today_time()

            number_xp = '//*[@id="content"]/event-results/div/section[1]/div/div/event-info/div/div/section/div/div[1]/div[1]/p[2]'
            number = (browser.find_element(By.XPATH, number_xp).text.split(':')[-1]).strip()

            title_xp = '//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[2]/div/h4[1]'
            start_time = time.time()
            try:
                WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, title_xp)))
            except:
                pass
            finish_time = time.time() - start_time
            print(finish_time)

            title = browser.find_element(By.XPATH, title_xp).text
            print(title)

            items_ = []
            items_add = []

            gr_yo_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/thead/tr/th[7]'
            gr_yo_txt = browser.find_element(By.XPATH, gr_yo_xp).text

            print(f'TEXT: {gr_yo_txt}')

            for tr_ in range(1, 100):
                tr_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[1]'

                try:
                    browser.find_element(By.XPATH, tr_xp)
                except:
                    break

                # NEW items to file
                # PLACING	BACK#	HORSE	RIDER	OWNER	SCORE	EARNINGS(USD)
                pl_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[1]'
                ba_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[2]'
                ho_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[3]'
                ri_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[4]'
                ow_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[5]'
                sc_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[6]'


                green_bool = False

                if gr_yo_txt == 'GREEN':
                    gr_yo = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[7]'
                    ea_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[8]'
                    items_.append(
                        {
                            "PLACING": browser.find_element(By.XPATH, pl_xp).text,
                            "BACK#": browser.find_element(By.XPATH, ba_xp).text,
                            "HORSE": browser.find_element(By.XPATH, ho_xp).text,
                            "RIDER": browser.find_element(By.XPATH, ri_xp).text,
                            "OWNER": browser.find_element(By.XPATH, ow_xp).text,
                            "SCORE": browser.find_element(By.XPATH, sc_xp).text,
                            "GREEN": browser.find_element(By.XPATH, gr_yo).text,
                            "EARNINGS(USD)": browser.find_element(By.XPATH, ea_xp).text
                        }
                    )
                elif gr_yo_txt == 'YOUTH':
                    gr_yo = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[7]'
                    ea_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[8]'
                    items_.append(
                        {
                            "PLACING": browser.find_element(By.XPATH, pl_xp).text,
                            "BACK#": browser.find_element(By.XPATH, ba_xp).text,
                            "HORSE": browser.find_element(By.XPATH, ho_xp).text,
                            "RIDER": browser.find_element(By.XPATH, ri_xp).text,
                            "OWNER": browser.find_element(By.XPATH, ow_xp).text,
                            "SCORE": browser.find_element(By.XPATH, sc_xp).text,
                            "YOUTH": browser.find_element(By.XPATH, gr_yo).text,
                            "EARNINGS(USD)": browser.find_element(By.XPATH, ea_xp).text
                        }
                    )
                else:
                    ea_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[7]'
                    items_.append(
                        {
                            "PLACING": browser.find_element(By.XPATH, pl_xp).text,
                            "BACK#": browser.find_element(By.XPATH, ba_xp).text,
                            "HORSE": browser.find_element(By.XPATH, ho_xp).text,
                            "RIDER": browser.find_element(By.XPATH, ri_xp).text,
                            "OWNER": browser.find_element(By.XPATH, ow_xp).text,
                            "SCORE": browser.find_element(By.XPATH, sc_xp).text,
                            "NONE": 'NONE',
                            "EARNINGS(USD)": browser.find_element(By.XPATH, ea_xp).text
                        }
                    )

            print(items_)
            #file_name_ = f'{pos_num}_{title}'.replace("\\", "").replace("/", "")
            file_name_ = f'{data}_{number}_{pos_num}_{title}'.replace("\\", "").replace("/", "")

            '{path_name}/___url.txt'

            #file_name = f'{path_name}/{file_name_}.json'
            file_name = f'./out/{file_name_}.json'

            with open(file_name, 'w+', encoding='utf-8') as file:
                json.dump(items_, file, indent=4, ensure_ascii=False)

            print(f'{data}_{number}_{title}\n\n')

            pos_num += 1

        print('*****************************************')


browser.close()
browser.quit()






# #***************************************************
# #
# source_html = browser.page_source
# time.sleep(0.7)
# browser.close()
# browser.quit()
#
# with requests.Session() as session:
#     # response = session.get(url=url, headers=headers)
#     soup = BeautifulSoup(source_html, 'lxml')
#
# print(soup)
# pagination = soup.find('ul', class_='pagination').text.strip()
# print(pagination)
# #
# #***************************************************





def main():
    pass

if __name__ == '__main__':
    main()

# time.sleep(5)
# browser.close()
# browser.quit()

"""

https://reinersuite.nrha.com/#/app/events/menu/72387
https://reinersuite.nrha.com/#/app/events/menu/72463
https://reinersuite.nrha.com/#/app/events/menu/72450
https://reinersuite.nrha.com/#/app/events/menu/72479
https://reinersuite.nrha.com/#/app/events/menu/72466
https://reinersuite.nrha.com/#/app/events/menu/72447
https://reinersuite.nrha.com/#/app/events/menu/72272
https://reinersuite.nrha.com/#/app/events/menu/72481
https://reinersuite.nrha.com/#/app/events/menu/72480

https://reinersuite.nrha.com/#/app/events/menu/72468
https://reinersuite.nrha.com/#/app/events/menu/72483
https://reinersuite.nrha.com/#/app/events/menu/72473
https://reinersuite.nrha.com/#/app/events/menu/72459
https://reinersuite.nrha.com/#/app/events/menu/72493
https://reinersuite.nrha.com/#/app/events/menu/72490
https://reinersuite.nrha.com/#/app/events/menu/72488
https://reinersuite.nrha.com/#/app/events/menu/72497
https://reinersuite.nrha.com/#/app/events/menu/72464
https://reinersuite.nrha.com/#/app/events/menu/72462
https://reinersuite.nrha.com/#/app/events/menu/72460
https://reinersuite.nrha.com/#/app/events/menu/72458
https://reinersuite.nrha.com/#/app/events/menu/72501

https://reinersuite.nrha.com/#/app/events/menu/72456
https://reinersuite.nrha.com/#/app/events/menu/72467
https://reinersuite.nrha.com/#/app/events/menu/72471
https://reinersuite.nrha.com/#/app/events/menu/72472
https://reinersuite.nrha.com/#/app/events/menu/72461
https://reinersuite.nrha.com/#/app/events/menu/72474
https://reinersuite.nrha.com/#/app/events/menu/72517
https://reinersuite.nrha.com/#/app/events/menu/72526
https://reinersuite.nrha.com/#/app/events/menu/72482
https://reinersuite.nrha.com/#/app/events/menu/72486
https://reinersuite.nrha.com/#/app/events/menu/72512
https://reinersuite.nrha.com/#/app/events/menu/72477
https://reinersuite.nrha.com/#/app/events/menu/72485
https://reinersuite.nrha.com/#/app/events/menu/72571
https://reinersuite.nrha.com/#/app/events/menu/72487
https://reinersuite.nrha.com/#/app/events/menu/72465
https://reinersuite.nrha.com/#/app/events/menu/72504
https://reinersuite.nrha.com/#/app/events/menu/72590
https://reinersuite.nrha.com/#/app/events/menu/72503
https://reinersuite.nrha.com/#/app/events/menu/72491
https://reinersuite.nrha.com/#/app/events/menu/72489
https://reinersuite.nrha.com/#/app/events/menu/72470
https://reinersuite.nrha.com/#/app/events/menu/72516
https://reinersuite.nrha.com/#/app/events/menu/72559
https://reinersuite.nrha.com/#/app/events/menu/71933 !!! No "Results"
https://reinersuite.nrha.com/#/app/events/menu/72448
https://reinersuite.nrha.com/#/app/events/menu/72475
https://reinersuite.nrha.com/#/app/events/menu/72494

https://reinersuite.nrha.com/#/app/events/menu/71933
https://reinersuite.nrha.com/#/app/events/menu/72448
https://reinersuite.nrha.com/#/app/events/menu/72475
https://reinersuite.nrha.com/#/app/events/menu/72494
https://reinersuite.nrha.com/#/app/events/menu/72514
https://reinersuite.nrha.com/#/app/events/menu/72500
https://reinersuite.nrha.com/#/app/events/menu/72554
https://reinersuite.nrha.com/#/app/events/menu/72535
https://reinersuite.nrha.com/#/app/events/menu/72542
https://reinersuite.nrha.com/#/app/events/menu/72513
https://reinersuite.nrha.com/#/app/events/menu/72509
https://reinersuite.nrha.com/#/app/events/menu/72593
https://reinersuite.nrha.com/#/app/events/menu/72531
https://reinersuite.nrha.com/#/app/events/menu/72451
https://reinersuite.nrha.com/#/app/events/menu/72525
https://reinersuite.nrha.com/#/app/events/menu/72511
https://reinersuite.nrha.com/#/app/events/menu/72495
https://reinersuite.nrha.com/#/app/events/menu/72587
https://reinersuite.nrha.com/#/app/events/menu/72521
https://reinersuite.nrha.com/#/app/events/menu/72519
https://reinersuite.nrha.com/#/app/events/menu/72484
https://reinersuite.nrha.com/#/app/events/menu/72564
https://reinersuite.nrha.com/#/app/events/menu/72518
https://reinersuite.nrha.com/#/app/events/menu/72523
https://reinersuite.nrha.com/#/app/events/menu/72496
https://reinersuite.nrha.com/#/app/events/menu/72602
https://reinersuite.nrha.com/#/app/events/menu/72570
https://reinersuite.nrha.com/#/app/events/menu/72522
https://reinersuite.nrha.com/#/app/events/menu/72502
https://reinersuite.nrha.com/#/app/events/menu/72492
https://reinersuite.nrha.com/#/app/events/menu/72537
https://reinersuite.nrha.com/#/app/events/menu/72580
https://reinersuite.nrha.com/#/app/events/menu/72569
https://reinersuite.nrha.com/#/app/events/menu/72577
https://reinersuite.nrha.com/#/app/events/menu/72568
https://reinersuite.nrha.com/#/app/events/menu/72567
https://reinersuite.nrha.com/#/app/events/menu/72608
https://reinersuite.nrha.com/#/app/events/menu/72549

https://reinersuite.nrha.com/#/app/events/menu/72537
https://reinersuite.nrha.com/#/app/events/menu/72580
https://reinersuite.nrha.com/#/app/events/menu/72569
https://reinersuite.nrha.com/#/app/events/menu/72577
https://reinersuite.nrha.com/#/app/events/menu/72568
https://reinersuite.nrha.com/#/app/events/menu/72567
https://reinersuite.nrha.com/#/app/events/menu/72544
https://reinersuite.nrha.com/#/app/events/menu/72155
https://reinersuite.nrha.com/#/app/events/menu/72625
https://reinersuite.nrha.com/#/app/events/menu/72624
https://reinersuite.nrha.com/#/app/events/menu/72589
https://reinersuite.nrha.com/#/app/events/menu/72588
https://reinersuite.nrha.com/#/app/events/menu/72586
https://reinersuite.nrha.com/#/app/events/menu/72583
https://reinersuite.nrha.com/#/app/events/menu/72545
https://reinersuite.nrha.com/#/app/events/menu/72524
https://reinersuite.nrha.com/#/app/events/menu/72538
https://reinersuite.nrha.com/#/app/events/menu/72499
https://reinersuite.nrha.com/#/app/events/menu/72515
https://reinersuite.nrha.com/#/app/events/menu/72510
https://reinersuite.nrha.com/#/app/events/menu/72498
https://reinersuite.nrha.com/#/app/events/menu/72626
https://reinersuite.nrha.com/#/app/events/menu/72551
https://reinersuite.nrha.com/#/app/events/menu/72520
https://reinersuite.nrha.com/#/app/events/menu/72619
https://reinersuite.nrha.com/#/app/events/menu/72596
https://reinersuite.nrha.com/#/app/events/menu/72560
https://reinersuite.nrha.com/#/app/events/menu/72636
https://reinersuite.nrha.com/#/app/events/menu/72536
https://reinersuite.nrha.com/#/app/events/menu/72594
https://reinersuite.nrha.com/#/app/events/menu/72530
https://reinersuite.nrha.com/#/app/events/menu/72584
https://reinersuite.nrha.com/#/app/events/menu/72566
https://reinersuite.nrha.com/#/app/events/menu/72550
https://reinersuite.nrha.com/#/app/events/menu/72599
https://reinersuite.nrha.com/#/app/events/menu/72607
https://reinersuite.nrha.com/#/app/events/menu/72601
https://reinersuite.nrha.com/#/app/events/menu/72565
https://reinersuite.nrha.com/#/app/events/menu/72534
https://reinersuite.nrha.com/#/app/events/menu/72555
https://reinersuite.nrha.com/#/app/events/menu/72615
https://reinersuite.nrha.com/#/app/events/menu/72613

"""