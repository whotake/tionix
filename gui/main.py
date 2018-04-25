# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import sys

from gui.interface import GUI_FRAMES
from gui.error import ERROR_APP_FRAMES
from gui.settings import ERROR_FILE
from gui.frames.main_frame import SampleApp

logging.basicConfig(filename=ERROR_FILE, level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)


def error_handler(exc_type, exc_value, exc_traceback):
    logger.error("Uncaught exception",
                 exc_info=(exc_type, exc_value, exc_traceback))
    error_app = SampleApp(ERROR_APP_FRAMES, default_frame='ErrorPage')
    error_app.mainloop()

sys.excepthook = error_handler

if __name__ == "__main__":
    app = SampleApp(GUI_FRAMES, default_frame='StartPage')
    app.mainloop()
