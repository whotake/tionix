# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import Tkinter as tk


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        generate_button = tk.Button(self, text="Сгенерировать список",
                                    command=self.generate_list)
        add_button = tk.Button(self, text="Добавить запись",
                               command=lambda: controller.show_frame(
                                   "AddRecordPage"))
        get_list_button = tk.Button(self, text='Получить данные',
                                    command=lambda: controller.show_frame(
                                        "RecordsPage"))

        generate_button.pack(pady=3)
        add_button.pack(pady=3)
        get_list_button.pack(pady=3)

    def generate_list(self):
        pass

    def get_list(self):
        pass
