# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import Tkinter as tk
import tkFont as tkfont

LARGE_FONT = ("Verdana", 12)


class SampleApp(tk.Tk):
    def __init__(self, frames, default_frame, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic"
        )

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in frames:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(default_frame)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
