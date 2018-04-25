# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import Tkinter as tk


class ErrorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text="Возникла ошибка", font=controller.title_font).pack()

        add_button = tk.Button(self, text="Посмотреть лог ошибок",
                               command=lambda: controller.show_frame(
                                   "ErrorListPage"))

        add_button.pack(pady=3)
