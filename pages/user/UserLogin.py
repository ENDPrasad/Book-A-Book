from functools import partial
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from pages.Base import Base
from pages.db import Database
from pages.admin.home import *
from pages.user.userHome import UserHomePage
from utils.constants import *


class UserLogin():
    def __init__(self) -> None:
        # super(self).__init__(self)
        self.window = Base().window
        self.window.title('User Login Page')
        self.db = Database()

    # Login to check credentials are correct or not and then
    # need to log the admin in
    def login(self, userName, password):
        userAvailable = self.db.checkUserExists(userName.get())
        if len(userAvailable) == 0:
            messagebox.askokcancel('Error!', message='User not registerd!!')
        else:
            userDetails = self.db.loginUser(userName.get(), password.get())
            if len(userDetails) == 0:
                messagebox.askokcancel('Error!', message='Either username or password is wrong!!')
            else:
                self.window.destroy()
                home = UserHomePage(userDetails)
                # home.loadDashboard()
                # home.loadUI()

    # To load Login page
    def loadLoginPage(self):
        labelFrame = LabelFrame(self.window, text='User Login', bg=labelFrameBG, fg='white', highlightbackground='white', font='lucida 12 bold', relief='solid', padx=20)
        labelFrame.pack(expand=True, fill=X)
        userLabel = Label(labelFrame, text='User name:', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        userLabel.pack(pady=3)
        userName = ttk.Entry(labelFrame, width=30)
        userName.pack(pady=3)
        passLabel = Label(labelFrame, text='Password:', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        passLabel.pack(pady=3)
        password = ttk.Entry(labelFrame, width=30, show="*")
        password.pack(pady=3)
        submit = Button(labelFrame, text='Login', command=partial(self.login, userName, password),fg='white', bg=button_bg_color, font='Lucida 12 bold')
        submit.pack(pady=3)

        message = Label(labelFrame, text='Not a user?', font='Lucida 10', bg=labelFrameBG)
        message.pack()
        register = Label(labelFrame, text='Register', font='Lucida 12 bold', bg=labelFrameBG, fg='blue')
        register.pack()
        register.bind("<Button-1>", self.loadRegisterPage)

    # To load register page
    def loadRegisterPage(self, url):

        def successMessage():
            if nameField.get() == '' or mailField.get() == '' or passwordField == '' or conatactField == '':
                messagebox.askokcancel(title= 'Error!', message='Required fields missing?')
            else:
                self.db.addNewUser(nameField.get(), mailField.get(), passwordField.get(), conatactField.get())
                messagebox.showinfo(title='Success', message='Registered successfully!!')
                self.window.destroy()
                # self.makeTopLevel()
                # Label(labelFrame, text='Registered Successfully!!', bg=labelFrameBG, font='Lucida 15 bold').grid(row=5, column=1)
    
        # self.window.destroy()
        
        self.window = Base().window
        self.window.title('User Register Page')
        labelFrame = LabelFrame(self.window, text='User Login', bg=labelFrameBG, fg='white', highlightbackground='white', font='lucida 12 bold', relief='solid', padx=20)
        labelFrame.pack(expand=True, fill=X)
        name = Label(labelFrame ,text = "Full Name", bg=labelFrameBG).grid(row = 0,column = 0)
        mail = Label(labelFrame ,text = "Email Id", bg=labelFrameBG).grid(row = 1,column = 0)
        password = Label(labelFrame ,text = "password", bg=labelFrameBG).grid(row = 2,column = 0)
        contact = Label(labelFrame ,text = "Contact Number", bg=labelFrameBG).grid(row = 3,column = 0)
        nameField = Entry(labelFrame)
        nameField.grid(row = 0,column = 1)
        mailField = Entry(labelFrame)
        mailField.grid(row = 1,column = 1)
        passwordField = Entry(labelFrame)
        passwordField.grid(row = 2,column = 1)
        conatactField = Entry(labelFrame)
        conatactField.grid(row = 3,column = 1)
        register = ttk.Button(labelFrame ,text="Register", command=successMessage).grid(row=4,column=0)
        
        # self.window.grab_set()
        # self.window.attributes("-topmost", True)
        self.loadUI()


    # To run the login page
    def loadUI(self):
        self.window.mainloop()

        
        