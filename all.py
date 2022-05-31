from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox

import json

link_ = ''
opt_ = ''
pg_options = (1, 2, 3, 4, 5)

# link_ = 'https://reinersuite.nrha.com/#/app/events/event-results/72268'
# link_ = 'https://reinersuite.nrha.com/#/app/events/event-results/72236'


class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon=r"resources/feather.ico"):
        self.root = Tk()
        self.root.title(title)

        self.entry_top = Entry(self.root, width=100, fg='blue', font=("Verdana", 12), relief=SUNKEN, bd=5,state=DISABLED)
        self.entry_top.pack()

        label1 = Label(self.root, text=f"NRHA\n", fg="#eee", bg="#aaa", font="Arial 20", padx=75)  # , pady=100)
        label1.place(relx=.7)  # , rely=.5, anchor='w')
        # label1.pack()

        self.radio_ = ''

        #var = IntVar(self.root, "1")
        self.var = IntVar()
        Radiobutton(self.root, text="ALL events in ONE month", variable=self.var, value=1, command=self.viewSelected).pack(anchor='w')  #   .grid(row=0, column=1)
        Radiobutton(self.root, text="ALL tables in ONE event", variable=self.var, value=2, command=self.viewSelected).pack(anchor='w')
        Radiobutton(self.root, text="ONE table in ONE event", variable=self.var, value=3, command=self.viewSelected).pack(anchor='w')
        #
        # ---------------------------------------------------
        #
        with open('config.json', 'r', encoding='utf-8') as set_:
            set_data = json.load(set_)

        year_from = set_data['year_from']
        year_to = set_data['year_to']

        # must be active, disabled, or normal
        self.scale_y = Scale(self.root, from_=year_from, to=year_to,
                                orient=HORIZONTAL)  # , state='disabled'

        self.scale_m = Scale(self.root, from_=1, to=12,
                                orient=HORIZONTAL)
        #
        # --------------------------------------------
        #
        self.btn_get = Button(self.root, text="Get Options!", width=10, command=self.get_link)
        self.btn_parse = Button(self.root, text="Parse!", width=10, command=self.parse)
        #
        # --------------------------------------------
        #
        self.lbl_lnk = Label(text='Enter link:', padx=5, pady=5)
        self.entry = Entry(self.root, width=80, fg='blue', font=("Verdana", 12), relief=SUNKEN, bd=5)

        global pg_options
        self.numbers = Combobox(self.root, values=pg_options, state="readonly", width=100)

    def viewSelected(self):

        choice = self.var.get()
        if choice == 1:
            radio_ = "A"

        elif choice == 2:
            radio_ = "B"

        elif choice == 3:
            radio_ = "C"
        else:
            radio_ = "Invalid selection"
        self.en_(radio_)

    def en_(self, radio):
        # self.spinbox.pack()
        if radio == 'A':
            #print(f'+ + + RB is: {radio}')
            self.scale_y.pack()
            self.scale_m.pack()

            self.lbl_lnk.forget()
            self.lbl_lnk.update()
            self.entry.forget()
            self.entry.update()
            self.btn_get.forget()
            self.btn_get.update()
            self.numbers.forget()
            self.numbers.update()
        elif radio == 'B':
            self.lbl_lnk.pack()
            self.entry.pack()

            self.scale_y.forget()
            self.scale_y.update()
            self.scale_m.forget()
            self.scale_m.update()
            self.numbers.forget()
            self.numbers.update()
            self.btn_get.forget()
            self.btn_get.update()

        elif radio == 'C':
            self.lbl_lnk.pack()
            self.entry.pack()
            self.btn_get.pack()
            self.numbers.pack()
            self.numbers.bind("<<ComboboxSelected>>", self.changed)

            self.scale_y.forget()
            self.scale_y.update()
            self.scale_m.forget()
            self.scale_m.update()

        self.btn_parse.forget()
        self.btn_parse.update()
        if radio != '':
            self.btn_parse.pack()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        text_var = StringVar(value="Text")
        # self.entry.pack()
        # Button(self.root, text="Go!..", width=10, command=self.get_link).pack()

        # self.numbers.pack()
        # self.numbers.bind("<<ComboboxSelected>>", self.changed)

        # if self.radio_ == 'A':
        #     btn_parse = Button(self.root, text="Parse!", width=10, command=self.parse).pack()
        btn_quit = Button(self.root, text="Quit", width=10, command=self.exit)
        btn_quit.place(relx=.005)#.pack()

    def changed(self, event):
        global opt_
        index = self.numbers.get()
        opt_ = index

    def get_link(self):
        global link_
        link_ = self.entry.get()
        pg_lnk(link_)

    def parse(self):
        value = self.numbers.get()
        index = self.numbers.current()
        pg_opt(value)

    def exit(self):
        choice = mb.askyesno("Quit", "Do you want to quit?")
        if choice:
            self.root.destroy()


def pg_lnk(lnk):
    pass


def pg_opt(val):
    pass


if __name__ == "__main__":
    window = Window(500, 500, "TKINTER")
    window.run()
