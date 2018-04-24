# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import Tkinter as tk

from gui.api import retrieve_persons


class RecordsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        data = self.retrieve_data()

        label = tk.Label(self, text="Записи", font=controller.title_font)
        label.grid()

        self.text_field = tk.Text(self)
        self.text_field.grid(row=1)
        scroll = tk.Scrollbar(self, command=self.text_field.yview)
        self.text_field.configure(yscrollcommand=scroll.set)
        self.insert_data(data)
        self.text_field.config(state='disabled')

        tk.Button(self, text='На главную', command=lambda: controller.show_frame("StartPage")).grid(row=6)

    def retrieve_data(self):
        return retrieve_persons()

    def insert_data(self, data):
        for item in data:
            self.text_field.insert('end', self.get_formated(item))

    def get_formated(self, item):
        return 'Имя: {0}, Фамилия: {1}, Отчество: {2}, Дата рождения: {3} \n'.format(
            self.formated_value(item, 'first_name'),
            self.formated_value(item, 'last_name'),
            self.formated_value(item, 'middle_name'),
            self.formated_value(item, 'date_of_birth')
        )

    def formated_value(self, item, key):
        default_value = 'Не указано'

        return item.get(key) or default_value
