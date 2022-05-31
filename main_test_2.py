from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import json
import time
from fake_useragent import UserAgent
from datetime import datetime
from pathlib import Path

ua = UserAgent()
ua = ua.random

import pickle

from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox


link_ = ''
opt_ = ''
pg_options = (1, 2, 3, 4, 5)


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon=r"resources/feather.ico"):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        # self.root.resizable(resizable[0], resizable[1])
        # if icon:
        #     self.root.iconbitmap(icon)

        self.entry = Entry(self.root, width=100, fg='blue', font=("Verdana", 12), relief=SUNKEN, bd=5)

        global pg_options
        self.numbers = Combobox(self.root, values=pg_options, state="readonly", width=100)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        text_var = StringVar(value="Text")
        #Entry(self.root, width=100, fg='blue', font=("Verdana", 12), relief=SUNKEN, bd=5, textvariable=text_var).pack()
        self.entry.pack()
        Button(self.root, text="Go!..", width=10, command=self.get_link).pack()


        # Button(self.root, text="Get...", width=10, command=self.parse).pack()
        #Combobox(self.root, values=("one", "two", "three"), justify=CENTER).pack()
        self.numbers.pack()
        self.numbers.bind("<<ComboboxSelected>>", self.changed)


        Button(self.root, text="Parse!", width=10, command=self.parse).pack()
        Button(self.root, text="Quit", width=10, command=self.exit).pack()

    def changed(self, event):
        global opt_
        index = self.numbers.get()
        #mb.showinfo("Info", f"Changed value, index: {index}")
        opt_ = index

    def get_link(self):
        global link_
        link_ = self.entry.get()
        pg_lnk(link_)

    def parse(self):
        value = self.numbers.get()
        index = self.numbers.current()
        #mb.showinfo("Get info", f"Index: {index}, value: {value}")
        pg_opt(value)

    def exit(self):
        choice = mb.askyesno("Quit", "Do you want to quit?")
        if choice:
            self.root.destroy()

    # def create_child(self, width, height, title="Child", resizable=(False, False), icon=None):
    #     ChildWindow(self.root, width, height, title, resizable, icon)


# link_ = 'https://reinersuite.nrha.com/#/app/events/event-results/72268'

# # # ================================================================================================================
# # # ================================================================================================================
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

# # cookies
# pickle.dump(browser.get_cookie(), open(f"cookies_reinersuite", "wb"))

browser.implicitly_wait(1.5)
# # #
# # # END of "login..."

# # # ===========================================================================================================
# # # ===========================================================================================================


def pg_lnk(link_):
    print(f'URL: {link_}')

    # # # START of "Parsing data..."

    url = link_

    ### !!!!!!!!!!!!!!!!!!!!!
    browser.get(url)
    time.sleep(1)
    browser.get(url)
    time.sleep(1)
    browser.get(url)

    time.sleep(3)

    global pg_options

    select_box = Select(browser.find_element(By.NAME, 'selectedClass'))
    pg_options = [x.text for x in select_box.options]

    # link_ = 'https://reinersuite.nrha.com/#/app/events/event-results/72268'

    window.numbers["values"] = pg_options
    window.numbers.update()
    window.numbers.pack()


def pg_opt(opt_):
    print(f'OPTION: {opt_}')

    pos = opt_

    data_xp = '//*[@id="content"]/event-results/div/section[1]/div/div/event-info/div/div/section/div/div[2]/div[1]/p'
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

    pos_num = 0

    number_xp = '//*[@id="content"]/event-results/div/section[1]/div/div/event-info/div/div/section/div/div[1]/div[1]/p[2]'
    number = (browser.find_element(By.XPATH, number_xp).text.split(':')[-1]).strip()

    # ! ! ! ! ! Find "NOMINATOR" & "NOMINATOR PAYOUT"
    #
    nominator_xp = f'//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[4]/div/table/thead/tr/th[7]'
    nominator_txt = browser.find_element(By.XPATH, nominator_xp).text

    if nominator_txt == 'NOMINATOR':
        add_col = 2
    else:
        add_col = 0


    file_name_ = f'{data}_{number}_{pos}'\
        .replace("#", "")\
        .replace(" ", "")\
        .replace("\\", "")\
        .replace("/", "")\
        .replace('"', '=')\
        .replace("*", "")

    file_name = f'./test2/{file_name_}.json'

    fle = Path(file_name)
    print(f'Download file: {fle}...')

    download_bool = False

    if fle.is_file():
        print(f'File present! Let`s skip...\n')
        pass
    else:
        print(f'File NO present! Downloding...\n')
        download_bool = True

    # link_ = 'https://reinersuite.nrha.com/#/app/events/event-results/72268'

    select_box = Select(browser.find_element(By.NAME, 'selectedClass'))
    #options = [x.text for x in select_box.options]
    select_box.select_by_visible_text(pos)

    if download_bool:
        # print(f'Option is: {pos}')
        select_box.select_by_visible_text(pos)
        title_xp = '//*[@id="content"]/event-results/div/section[3]/div[2]/div[2]/div/div[2]/div/h4[1]'
        start_time = time.time()
        try:
            WebDriverWait(browser, 100).until(EC.element_to_be_clickable((By.XPATH, title_xp)))
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


        with open(file_name, 'w+', encoding='utf-8') as file:
            json.dump(items_, file, indent=4, ensure_ascii=False)

        print('- - - - - - - - - - - - - - - - - - saved!!!\n')

    print(f'* * * * *   END of {number}   * * * * *\n')

    print(f'! ! ! ! !  Job completed successfully! Enter a new link for processing...  ! ! ! ! !')
    # browser.close()
    # browser.quit()


if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    window.run()