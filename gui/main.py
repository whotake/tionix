# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import sys
import tkMessageBox

from gui.interface import GUI_FRAMES
from gui.settings import ERROR_FILE
from gui.frames.main_frame import SampleApp

logging.basicConfig(filename=ERROR_FILE, level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)


def error_handler(exc_type, exc_value, exc_traceback):
    logger.error("Uncaught exception",
                 exc_info=(exc_type, exc_value, exc_traceback))
    tkMessageBox.showerror('Ошибка', 'Данные записаны в лог')


sys.excepthook = error_handler

if __name__ == "__main__":
    app = SampleApp(GUI_FRAMES, default_frame='StartPage')
    app.mainloop()
