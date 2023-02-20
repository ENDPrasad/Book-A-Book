from tkinter import *

from utils.constants import *
import mysql.connector

class Base:
    def __init__(self):

        # Initializing the window
        self.window = Tk()
        self.window.title('Book Management System')
        # self.window.eval('tk::PlaceWindow . center')
        self.window.geometry(f'{screen_width}x{screen_height}+{screen_x}+{screen_y}')
        self.window.configure(
            background='#ECF2FF'
        )
        self.window.option_add('font', 'Lucida')
    
    