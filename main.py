from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import json
import time
import tkinter as tk
from fake_useragent import UserAgent
from datetime import datetime
from calendar import monthrange
from pathlib import Path

ua = UserAgent()
ua = ua.random


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.spinbox = tk.Spinbox(self, from_=1, to=12)
        self.scale_y = tk.Scale(self, from_=2021, to=2022,
                                orient=tk.HORIZONTAL)

        self.scale_m = tk.Scale(self, from_=6, to=12,
                                orient=tk.HORIZONTAL)

        self.btn = tk.Button(self, text="Parse!..",
                             command=self.print_values)

        # self.spinbox.pack()
        self.scale_y.pack()
        self.scale_m.pack()
        self.btn.pack()

    def print_values(self):
        # print("Spinbox: {}".format(self.spinbox.get()))
        date_y = self.scale_y.get()
        date_m = self.scale_m.get()
        print("Year: {}".format(self.scale_y.get()))
        print("Month: {}".format(self.scale_m.get()))
        # self.btn["state"] = "disabled"
        self.btn.forget()
        self.btn.update()
        _my(date_y, date_m)


# # # ================================================================================================================
# # # ================================================================================================================

def _my(date_y, date_m):
    url = 'https://reinersuite.nrha.com/#/login'

    with open('config.json', 'r', encoding='utf-8') as set_:
        set_data = json.load(set_)

    set_email = set_data['set_email']
    set_pass = set_data['set_pass']

    print('start...')

    # # # START of "Init..."
    # # #
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
    # # #
    # # # END of "Init..."

    # # # ===========================================================================================================
    # # # ===========================================================================================================

    # # # START of "login..."
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
    # # # END of "login..."

    # # # ===========================================================================================================
    # # # ===========================================================================================================

    # # # # START of "Collecting links..."
    # # # #
    # browser.implicitly_wait(1.5)
    # url_new = 'https://reinersuite.nrha.com/#/app/events/my-events'
    # browser.get(url_new)
    # time.sleep(2)
    #
    # tab_event_finder_xp = '//*[@id="summary-tab"]'
    # tab_event_finder = browser.find_element(By.XPATH, tab_event_finder_xp).click()
    #
    # date_from_xp = '//*[@id="q-datepicker_3"]'
    # date_from = browser.find_element(By.XPATH, date_from_xp)
    # date_from.clear()
    #
    # if date_m < 10:
    #     date_from.send_keys(f'0{date_m}/01/{date_y}')
    # else:
    #     date_from.send_keys(f'{date_m}/01/{date_y}')
    #
    # time.sleep(0.5)
    # date_from.send_keys(Keys.RETURN)
    # time.sleep(0.5)
    # # ------------------------------------------------------
    # days = monthrange(date_y, date_m)[1]
    # # ------------------------------------------------------
    # date_to_xp = '//*[@id="q-datepicker_5"]'
    # date_to = browser.find_element(By.XPATH, date_to_xp)
    #
    # if date_m < 10:
    #     date_to.send_keys(f'{date_m}/{days}/{date_y}')
    # else:
    #     date_to.send_keys(f'{date_m}/{days}/{date_y}')
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
    # for p_ in range(2, 30):
    #     pag_xp = f'//*[@id="finder"]/div/div/table/tfoot/tr/td/mfbootstrappaginator/mfpaginator/ul[1]/li[{p_}]/a'
    #     print(pag_xp)
    #     time.sleep(0.3)
    #     if p_ > 2:
    #         try:
    #             pag = browser.find_element(By.XPATH, pag_xp).click()
    #         except:
    #             pass
    #
    #     lnk_p_count = 0
    #     for i in range(1, 11):
    #
    #         lnk_p_count += 1
    #
    #         a_s = f'#finder > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(1) > a'
    #         a_ = browser.find_elements(By.CSS_SELECTOR, a_s)
    #
    #         link = [elem.get_attribute('href') for elem in a_]
    #
    #         if not link:
    #             print('EMPTY...')
    #             lnk_p_count = 555
    #             print(f'\n==========================================\n')
    #             break
    #         else:
    #             print(f'{lnk_p_count} --- > {link}')
    #             time.sleep(0.3)
    #             # write links to file
    #             with open('urls.txt', 'a', encoding='utf-8') as file:
    #                 for url in link:
    #                     file.write(f'{url}\n')
    #     if lnk_p_count == 555:
    #         break
    #
    # # # #
    # # # # END of "Collecting links..."

    # ===============================================================================================================
    # ===============================================================================================================

    # # # START of "Parsing data..."
    # # #

    # def gear_time():
    #     gear_xp = '//*[@id="app"]/nav[2]/div/div[2]/ul[1]/li/a/i'
    #     start_time = time.time()
    #     try:
    #         WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, gear_xp)))
    #     except:
    #         pass
    #     finish_time = time.time() - start_time
    #     print(f'GEAR: {finish_time}')
    #
    # def results_time():
    #     results_xp = '//*[@id="content"]/div/div/div/div/div/section/div/div[2]/ul/li[2]/a'
    #     start_time = time.time()
    #     try:
    #         WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, results_xp)))
    #     except:
    #         pass
    #     finish_time = time.time() - start_time
    #     print(f'RESULTS_time: {finish_time}')
    #
    # def refrash_time():
    #     refresh_time_xp = '//*[@id="content"]/event-results/div/section[2]/div/div/div[2]/button'
    #     start_time = time.time()
    #     try:
    #         WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element(By.XPATH, refresh_time_xp))
    #     except:
    #         pass
    #     finish_time = time.time() - start_time
    #     print(f'REFRASH_time: {finish_time}')
    #
    #
    #     # '//*[@id="content"]/event-results/div/section[2]/div/div/div[1]/select'
    #
    # def data_today_time():
    #     # refresh_time_xp = '//*[@id="content"]/event-results/div/section[2]/div/div/div[2]/button'
    #     data_today_xp = '//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[1]/div/span'
    #     start_time = time.time()
    #     try:
    #         WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element(By.XPATH, data_today_xp))
    #     except:
    #         pass
    #     finish_time = time.time() - start_time
    #     print(f'DATA_TO_DAY_time: {finish_time}')

    def links_with_no_results(url):
        with open('links_with_no_results.txt', 'a', encoding='utf-8') as file:
            file.write(f'{url}\n')

    with open('urls.txt') as file:
        url_list = [line.strip() for line in file.readlines()]

    url_count = len(url_list)
    print(url_count)

    browser.implicitly_wait(1.5)

    for url in url_list:
        ### !!!!!!!!!!!!!!!!!!!!!
        browser.get(url)
        time.sleep(0.5)
        browser.get(url)

        # time.sleep(3)
        #results_time()
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))

        # find "Results"
        res_bool = False
        results_xp = '//*[@id="content"]/div/div/div/div/div/section/div/div[2]/ul/li[2]/a'
        try:
            results = browser.find_element(By.XPATH, results_xp).click()
            res_bool = True
        except:
            links_with_no_results(url)

        if res_bool:
            #refrash_time()
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))
            time.sleep(3)
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

            select_box = Select(browser.find_element(By.NAME, 'selectedClass'))
            options = [x.text for x in select_box.options]

            pos_num = 0

            file_count = 0
            file_pres_count = 0

            number_xp = '//*[@id="content"]/event-results/div/section[1]/div/div/event-info/div/div/section/div/div[1]/div[1]/p[2]'
            number = (browser.find_element(By.XPATH, number_xp).text.split(':')[-1]).strip()


            for pos in options:

                #element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))

                #data_today_time()

                file_count += 1
                pos_num += 1

                print(f'FILE_COUNT = {file_count}')
                #file_name_ = f'{data}_{number}_{pos_num}_{title}'.replace("\\", "").replace("/", "")
                file_name_ = f'{data}_{number}_{pos}'.replace("#", "").replace(" ", "").replace("\\", "").replace("/", "")

                file_name = f'./out/202106/{file_name_}.json'

                fle = Path(file_name)
                print(f'Download file: {fle}...')

                download_bool = False

                if fle.is_file():
                    file_pres_count += 1
                    print(f'{file_pres_count} File present! Let`s skip...\n')
                    pass
                else:
                    print(f'File NO present! Downloding...\n')
                    download_bool = True

                if download_bool:
                    # print(f'Option is: {pos}')
                    select_box.select_by_visible_text(pos)
                    title_xp = '//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[2]/div/h4[1]'
                    start_time = time.time()
                    try:
                        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, title_xp)))
                    except:
                        pass
                    finish_time = time.time() - start_time
                    print(f'Data load time: {finish_time} sec\n')
                    # title = browser.find_element(By.XPATH, title_xp).text
                    # print(title)

                    items_ = []

                    gr_yo_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/thead/tr/th[7]'
                    gr_yo_txt = browser.find_element(By.XPATH, gr_yo_xp).text

                    #print(f'TEXT: {gr_yo_txt}')

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

                    #print(items_)
                    # file_name_ = f'{data}_{number}_{pos_num}_{title}'.replace("\\", "").replace("/", "")
                    # file_name = f'./out/{file_name_}.json'

                    with open(file_name, 'w+', encoding='utf-8') as file:
                        json.dump(items_, file, indent=4, ensure_ascii=False)

                    print('- - - - - - - - - - - - - - - - - - saved!!!\n')


                    #print(f'{data}_{number}_{title}\n\n')



            print('*****************************************')

    browser.close()
    browser.quit()

    app.btn["state"] = "normal"
    app.btn.pack()
    app.btn.update()


if __name__ == "__main__":
    app = App()
    # tk.Button(app, text="Quit", command=app.quit).pack()
    app.mainloop()
