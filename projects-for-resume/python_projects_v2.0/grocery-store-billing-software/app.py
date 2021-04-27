import tkinter as tk
from tkinter import *

import logging


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s : %(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level='DEBUG',
    filename='grocery_billing_software_logs.txt'
)

logger = logging.getLogger('test_logger')


if __name__ == '__main__':
    root = tk.Tk(className='Billing System')
    # set window size
    root.geometry("1080x720")

    logger.info("Set BackGround color of App Window")
    root['background'] = '#3e4040'

    # stops resizing app window
    logger.info("stops resizing app window")
    root.resizable(0, 0)
    root.mainloop()
