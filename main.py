from tkinter import *
from tkinter import ttk
from pages.AdminLogin import AdminPage

from pages.Base import Base
from pages.UserLogin import UserLogin
from utils.constants import *

def gotoLoginPage():
    user = UserLogin()

def gotoAdminLogin():
    admin = AdminPage()
    admin.loadLoginPage()
    # admin.window.mainloop()
    admin.loadUI()

def main():
    app = Base()
    root = app.window
    app.startSQLServer()
    label = Label(root, text='Book Management System', font='lucida 25 bold', bg='#ECF2FF')
    label.pack()
    adminButton = Button(root, text="Admin", command=gotoAdminLogin, bg=button_bg_color, fg='white', width=20, height=3, font='lucida 17 bold')
    userButton = Button(root, text="User", command=gotoLoginPage, bg=button_bg_color, fg='white', width=20, height=3, font='lucida 17 bold')
    adminButton.pack(pady=15)
    userButton.pack()
    # adminButton.grid(row=3, column=2)
    # userButton.grid(row=3, column=5)

    # To run the application
    root.mainloop()

if __name__ == '__main__':
    main()