# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import Tkinter as tk
import tkMessageBox

from gui.settings import ERROR_FILE


class ErrorListPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Лог ошибок", font=controller.title_font)
        label.grid()

        self.text_field = tk.Text(self)
        self.text_field.grid(row=1)
        self.insert_data()
        scroll = tk.Scrollbar(self, command=self.text_field.yview)
        self.text_field.configure(yscrollcommand=scroll.set)
        self.text_field.config(state='disabled')
        tk.Button(self, text='Назад',
                  command=lambda: controller.show_frame("StartPage")
                  ).grid(row=2)

    def insert_data(self):
        data = ''

        try:
            with open(ERROR_FILE, 'r') as err_log:
                data = err_log.read()

            err_log.close()
        except IOError:
            tkMessageBox.showerror("Ошибка", "Файл лога не существует")

        self.text_field.insert('end', data)
