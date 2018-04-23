# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import Tkinter as tk


class RecordsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        data = self.retrieve_data()

        label = tk.Label(self, text="Записи", font=controller.title_font)
        label.grid()

        text_field = tk.Text(self)
        text_field.grid(row=1)
        scroll = tk.Scrollbar(self, command=text_field.yview)
        text_field.configure(yscrollcommand=scroll.set)
        text_field.insert('end', data)
        text_field.config(state='disabled')

        tk.Button(self, text='На главную', command=lambda: controller.show_frame("StartPage")).grid(row=6)

    def retrieve_data(self):
        return '1'
