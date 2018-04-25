# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import Tkinter as tk
import tkMessageBox

import requests

from gui.api import create_person


class AddRecordPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="New record page", font=controller.title_font)
        label.grid()

        tk.Label(self, text='Имя').grid(row=1)
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.grid(row=1, column=1)

        tk.Label(self, text='Фамилия').grid(row=2)
        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.grid(row=2, column=1)

        tk.Label(self, text='Отчество').grid(row=3)
        self.middle_name_entry = tk.Entry(self)
        self.middle_name_entry.grid(row=3, column=1)

        tk.Label(self, text='Дата рождения').grid(row=4)
        self.dob_entry = tk.Entry(self)
        self.dob_entry.grid(row=4, column=1)

        tk.Button(self, text='Отмена', command=lambda: controller.show_frame("StartPage")).grid(row=6)
        tk.Button(self, text='Сохранить', command=self.create_record).grid(row=6, column=1)

    def create_record(self):
        data = {
            'first_name': self.first_name_entry.get(),
            'last_name': self.last_name_entry.get(),
            'middle_name': self.last_name_entry.get(),
            'date_of_birth': self.dob_entry.get()
        }

        response = self.make_api_call(data)

        if response.status_code == requests.codes.created:
            tkMessageBox.showinfo("Успешно", "Объект создан")
        else:
            tkMessageBox.showerror("Ошибка", "Что-то пошло не так")

        self.controller.show_frame("StartPage")

    def make_api_call(self, data):
        return create_person(data)
