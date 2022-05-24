# import sqlite3
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# import json
# import time
# import tkinter as tk
# from fake_useragent import UserAgent
# from datetime import datetime
# from calendar import monthrange
# import os
#
# ua = UserAgent()
# ua = ua.random
#
# scriptDir = os.path.dirname(os.path.realpath(__file__))
# db_connection = sqlite3.connect(scriptDir + r'/rss.sqlite')
# db = db_connection.cursor()
#
# db.execute("""CREATE TABLE IF NOT EXISTS feeds(
#     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     feed_link_sha TEXT(64),
#     feed_link TEXT,
#     feed_sha TEXT(64)
#    );
# """)
# db_connection.commit()
#
# db.execute("""CREATE TABLE IF NOT EXISTS items(
#    item_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#    item_title TEXT,
#    item_published TEXT,
#    feed_id INTEGER,
#    FOREIGN KEY (feed_id)  REFERENCES feeds (id) ON DELETE CASCADE);
# """)
# db_connection.commit()
#
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         # self.spinbox = tk.Spinbox(self, from_=1, to=12)
#         self.scale_y = tk.Scale(self, from_=1975, to=2022,
#                                 orient=tk.HORIZONTAL)
#
#         self.scale_m = tk.Scale(self, from_=1, to=12,
#                                 orient=tk.HORIZONTAL)
#
#         self.btn = tk.Button(self, text="Parse!..",
#                              command=self.print_values)
#
#         # self.spinbox.pack()
#         self.scale_y.pack()
#         self.scale_m.pack()
#         self.btn.pack()
#
#     def print_values(self):
#         # print("Spinbox: {}".format(self.spinbox.get()))
#         date_y = self.scale_y.get()
#         date_m = self.scale_m.get()
#         print("Year: {}".format(self.scale_y.get()))
#         print("Month: {}".format(self.scale_m.get()))
#         # self.btn["state"] = "disabled"
#         self.btn.forget()
#         self.btn.update()
#         _my(date_y, date_m)
#
#
# # # # ================================================================================================================
# # # # ================================================================================================================
#
# def _my(date_y, date_m):
#     url = 'https://reinersuite.nrha.com/#/login'
#
#     with open('config.json', 'r', encoding='utf-8') as set_:
#         set_data = json.load(set_)
#
#     set_email = set_data['set_email']
#     set_pass = set_data['set_pass']
#
#     print('start...')
#
#     # # # START of "Init..."
#     # # #
#     chrome_path = "./chromedriver.exe"
#
#     options = webdriver.ChromeOptions()
#     options.headless = False
#     options.add_argument("--incognito")
#     options.add_argument("start-maximized")
#     #
#     options.add_argument('--disable-blink-features=AutomationControlled')
#     #
#     options.add_experimental_option("excludeSwitches", ["enable-logging"])
#     options.add_experimental_option('useAutomationExtension', False)
#     browser = webdriver.Chrome(options=options, executable_path=chrome_path)
#     # # #
#     # # # END of "Init..."
#
#     # # # ===========================================================================================================
#     # # # ===========================================================================================================
#
#     # # # START of "login..."
#     # # #
#     browser.implicitly_wait(1.5)
#     browser.get(url)
#     time.sleep(2)
#
#     email_xp = '//*[@id="content"]/div/div/section/div[2]/form/div[1]/div[1]/input'
#     in_email = browser.find_element(By.XPATH, email_xp)
#     in_email.send_keys(set_email)
#     time.sleep(1.1)
#
#     pass_xp = '//*[@id="content"]/div/div/section/div[2]/form/div[1]/div[2]/input'
#     in_pass = browser.find_element(By.XPATH, pass_xp)
#     in_pass.send_keys(set_pass)
#     time.sleep(1.2)
#
#     checkbox_xp = '//*[@id="content"]/div/div/section/div/form/div[2]/div/label'
#     checkbox = browser.find_element(By.XPATH, checkbox_xp).click()
#     time.sleep(0.7)
#
#     btn_login_xp = '//*[@id="content"]/div/div/section/div/form/div[3]/div/button'
#     btn_login = browser.find_element(By.XPATH, btn_login_xp).click()
#     time.sleep(0.9)
#
#     gear_xp = '//*[@id="app"]/nav[2]/div/div[2]/ul[1]/li/a/i'
#     start_time = time.time()
#     try:
#         WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, gear_xp)))
#     except:
#         pass
#     finish_time = time.time() - start_time
#     print(finish_time)
#     # # #
#     # # # END of "login..."
#
#     # # # ===========================================================================================================
#     # # # ===========================================================================================================
#
#     # # # START of "Collecting links..."
#     # # #
#     browser.implicitly_wait(1.5)
#     url_new = 'https://reinersuite.nrha.com/#/app/events/my-events'
#     browser.get(url_new)
#     time.sleep(2)
#
#     tab_event_finder_xp = '//*[@id="summary-tab"]'
#     tab_event_finder = browser.find_element(By.XPATH, tab_event_finder_xp).click()
#
#     date_from_xp = '//*[@id="q-datepicker_3"]'
#     date_from = browser.find_element(By.XPATH, date_from_xp)
#     date_from.clear()
#
#     if date_m < 10:
#         date_from.send_keys(f'0{date_m}/01/{date_y}')
#     else:
#         date_from.send_keys(f'{date_m}/01/{date_y}')
#
#     time.sleep(0.5)
#     date_from.send_keys(Keys.RETURN)
#     time.sleep(0.5)
#     # ------------------------------------------------------
#     days = monthrange(date_y, date_m)[1]
#     # ------------------------------------------------------
#     date_to_xp = '//*[@id="q-datepicker_5"]'
#     date_to = browser.find_element(By.XPATH, date_to_xp)
#
#     if date_m < 10:
#         date_to.send_keys(f'{date_m}/{days}/{date_y}')
#     else:
#         date_to.send_keys(f'{date_m}/{days}/{date_y}')
#
#     time.sleep(0.5)
#     date_to.send_keys(Keys.RETURN)
#     time.sleep(1)
#
#     btn_search_xp = '//*[@id="finder"]/event-find/div/div/section/div/form/fieldset/div[2]/input[1]'
#     btn_search = browser.find_element(By.XPATH, btn_search_xp).click()
#
#     # clear file...
#     with open('urls.txt', 'w+', encoding='utf-8') as file:
#         file.write('')
#
#     for p_ in range(2, 30):
#         pag_xp = f'//*[@id="finder"]/div/div/table/tfoot/tr/td/mfbootstrappaginator/mfpaginator/ul[1]/li[{p_}]/a'
#         print(pag_xp)
#         time.sleep(0.3)
#         if p_ > 2:
#             try:
#                 pag = browser.find_element(By.XPATH, pag_xp).click()
#             except:
#                 pass
#
#         lnk_p_count = 0
#         for i in range(1, 11):
#
#             lnk_p_count += 1
#
#             a_s = f'#finder > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(1) > a'
#             a_ = browser.find_elements(By.CSS_SELECTOR, a_s)
#
#             link = [elem.get_attribute('href') for elem in a_]
#
#             if not link:
#                 print('EMPTY...')
#                 lnk_p_count = 555
#                 print(f'\n==========================================\n')
#                 break
#             else:
#                 print(f'{lnk_p_count} --- > {link}')
#                 time.sleep(0.3)
#                 # write links to file
#                 with open('urls.txt', 'a', encoding='utf-8') as file:
#                     for url in link:
#                         file.write(f'{url}\n')
#         if lnk_p_count == 555:
#             break
#
#     # # #
#     # # # END of "Collecting links..."
#
#     # ===============================================================================================================
#     # ===============================================================================================================