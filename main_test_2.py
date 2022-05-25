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

link_ = ''

import tkinter as tk


class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.link = tk.Entry(self)
        self.parsing_btn = tk.Button(self, text="Parse!..",
                                   command=self.print_parsing)
        self.clear_btn = tk.Button(self, text="Clear",
                                   command=self.clear_form)
        self.link.pack()
        self.parsing_btn.pack(fill=tk.BOTH)
        self.clear_btn.pack(fill=tk.BOTH)

    def print_parsing(self):
        global link_
        link_ = self.link.get()
        print(f"Link entered: {link_}")
        self.parsing_btn.forget()
        self.parsing_btn.update()
        self.clear_btn.forget()
        self.clear_btn.update()
        app.destroy()
        _my_(link_)

    def clear_form(self):
        self.link.delete(0, tk.END)
        self.link.focus_set()

class OptionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.link = tk.Entry(self)
        self.parsing_btn = tk.Button(self, text="Parse!..",
                                   command=self.print_parsing)
        self.clear_btn = tk.Button(self, text="Clear",
                                   command=self.clear_form)
        self.link.pack()
        self.parsing_btn.pack(fill=tk.BOTH)
        self.clear_btn.pack(fill=tk.BOTH)

    def print_parsing(self):
        global opt_
        link_ = self.link.get()
        print(f"Opt entered: {link_}")
        self.parsing_btn.forget()
        self.parsing_btn.update()
        self.clear_btn.forget()
        self.clear_btn.update()
        _my(opt_)

    def clear_form(self):
        self.link.delete(0, tk.END)
        self.link.focus_set()


def _my_(link_):
    print(f'LINK: {link_}')
    # app2 = OptionApp()
    # app2.mainloop()

app = LoginApp()
app.mainloop()


# link_ = 'https://reinersuite.nrha.com/#/app/events/event-results/72268'
# opt_ = 'Entry Level - NRHA Derby Show I - 10001 - Green Reiner 2 - Go# 1'#'NRHA Derby - 6210 - Level 4 Open-Aged Event - Go# 1 - $205,000.00'

#





opt_ = ''


# # # ================================================================================================================
# # # ================================================================================================================

def _my(opt_):
    print(f'OPTION: {opt_}')


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

    # # # START of "Parsing data..."
    # # #


    browser.implicitly_wait(1.5)

    file_count = 0

    url = link_

    ### !!!!!!!!!!!!!!!!!!!!!
    browser.get(url)
    time.sleep(2)
    browser.get(url)
    time.sleep(2)
    browser.get(url)

    data_xp = '//*[@id="content"]/event-results/div/section[1]/div/div/event-info/div/div/section/div/div[2]/div[1]/p'
    # start_time = time.time()
    # try:
    #     WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, data_xp)))
    #     #WebDriverWait(browser, 60).until(EC.text_to_be_present_in_element(By.XPATH, data_xp))
    # except:
    #     pass
    # finish_time = time.time() - start_time
    # print(f'DATA_START_time: {finish_time}')



    #   WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element(By.XPATH, refresh_time_xp))

    # timestamp = WebDriverWait(browser, 30).until(
    #     EC.presence_of_element_located(By.XPATH, data_xp)
    #
    # )
    # try:
    #     timestamp = WebDriverWait(browser, 180).until(EC.presence_of_element_located(
    #         (By.XPATH, data_xp)))
    #     print(f'timestamp = {timestamp.text.split(" ")[0]}')
    # finally:
    #     pass

    time.sleep(10)

    # mm/dd/yyyy
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

    number_xp = '//*[@id="content"]/event-results/div/section[1]/div/div/event-info/div/div/section/div/div[1]/div[1]/p[2]'
    number = (browser.find_element(By.XPATH, number_xp).text.split(':')[-1]).strip()

    pos = opt_

    # element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "html")))

    # data_today_time()

    file_count += 1
    pos_num += 1

    print(f'FILE_COUNT = {file_count}')
    # file_name_ = f'{data}_{number}_{pos_num}_{title}'.replace("\\", "").replace("/", "")
    file_name_ = f'{data}_{number}_{pos}'.replace("#", "").replace(" ", "").replace("\\", "").replace("/", "")

    file_name = f'./test/{file_name_}.json'

    fle = Path(file_name)
    print(f'Download file: {fle}...')

    download_bool = False

    if fle.is_file():
        print(f'File present! Let`s skip...\n')
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
            WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.XPATH, title_xp)))
        except:
            pass
        finish_time = time.time() - start_time
        print(f'Data load time: {finish_time} sec\n')
        # title = browser.find_element(By.XPATH, title_xp).text
        # print(title)

        items_ = []

        gr_yo_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/thead/tr/th[7]'
        gr_yo_txt = browser.find_element(By.XPATH, gr_yo_xp).text

        add_col = 0
        if gr_yo_txt == 'NOMINATOR':
            add_col = 2

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
                # ! ! ! ! ! Find "NOMINATOR" & "NOMINATOR PAYOUT"
                #
                nom_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/thead/tr/th[8]'
                nom_txt = browser.find_element(By.XPATH, nom_xp).text
                if nom_txt == 'NOMINATOR':
                    add_col = 2
                else:
                    add_col = 0
                gr_yo = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[7]'
                ea_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[{8 + add_col}]'
                print(f'ea_xp: {ea_xp}')
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
                # ! ! ! ! ! Find "NOMINATOR" & "NOMINATOR PAYOUT"
                #
                nom_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/thead/tr/th[8]'
                nom_txt = browser.find_element(By.XPATH, nom_xp).text
                if nom_txt == 'NOMINATOR':
                    add_col = 2
                else:
                    add_col = 0
                gr_yo = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[7]'
                ea_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[{8 + add_col}]'
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
                ea_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/tbody/tr[{tr_}]/td[{7 + add_col}]'
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

        # print(items_)
        # file_name_ = f'{data}_{number}_{pos_num}_{title}'.replace("\\", "").replace("/", "")
        # file_name = f'./out/{file_name_}.json'

        with open(file_name, 'w+', encoding='utf-8') as file:
            json.dump(items_, file, indent=4, ensure_ascii=False)

        print('- - - - - - - - - - - - - - - - - - saved!!!\n')

    print(f'* * * * *   END of {number}   * * * * *\n')

    print(f'! ! ! ! !  Job completed successfully! Enter a new link for processing...  ! ! ! ! !')
    browser.close()
    browser.quit()


    # app.parsing_btn["state"] = "normal"
    # app.parsing_btn.pack()
    # app.parsing_btn.update()
    # app.clear_btn.pack()
    # app.clear_btn.update()




if __name__ == "__main__":
    pass
    app2 = LoginApp()
    app2.mainloop()
