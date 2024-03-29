from functools import partial
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pages.Base import Base
from pages.db import Database
from pages.admin.home import HomePage
from utils.constants import *


class AdminPage():
    def __init__(self) -> None:
        # super(self).__init__(self)
        self.window = Base().window
        self.window.title('Admin Login Page')
        self.db = Database()
    
    # Login to check credentials are correct or not and then
    # need to log the admin in
    def login(self, userName, password):
        userAvailable = self.db.checkAdminExists(userName.get())
        if len(userAvailable) == 0:
            messagebox.askokcancel('Error!', message='User not registered!!')
        else:
            adminDetails = self.db.loginAdmin(userName.get(), password.get())
            if len(adminDetails) == 0:
                messagebox.askokcancel('Error!', message='Either username or password is wrong!!')
            else:
                print('Admin Details:', adminDetails)
                self.window.destroy()
                home = HomePage(adminDetails)
                # home.loadDashboard()
                # home.loadUI()

    def changePassword(self, email, newPassword):
        pass

    def forgotPassword(self):
        self.window = Base().window
        self.window.title('Forgot Password Page')
        labelFrame = LabelFrame(self.window, text='Forgot Password', bg=labelFrameBG, fg='white', highlightbackground='white', font='lucida 12 bold', relief='solid', padx=20)
        labelFrame.pack(expand=True, fill=X)
        userLabel = Label(labelFrame, text='Email:', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        userLabel.pack(pady=3)
        userName = ttk.Entry(labelFrame, width=30)
        userName.pack(pady=3)
        passLabel = Label(labelFrame, text='New Password:', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        passLabel.pack(pady=3)
        password = ttk.Entry(labelFrame, width=30, show="*")
        password.pack(pady=3)
        submit = Button(labelFrame, text='Submit', command=partial(self.changePassword, userName, password),fg='white', bg=button_bg_color, font='Lucida 12 bold')
        submit.pack(pady=3)


    # To load Login page
    def loadLoginPage(self):
        labelFrame = LabelFrame(self.window, text='Admin Login', bg=labelFrameBG, fg='white', highlightbackground='white', font='lucida 12 bold', relief='solid', padx=20)
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

        # Forgot Password
        forgotPass = Label(labelFrame, text='Forgot Password', font='Lucida 12 bold', bg=labelFrameBG, fg='white')
        forgotPass.pack()
        forgotPass.bind("<Button-2>", self.forgotPassword)

    # To load register page
    def loadRegisterPage(self, url):

        def successMessage():
            if nameField.get() == '' or mailField.get() == '' or passwordField.get() == '' or conatactField.get() == '':
                messagebox.askokcancel(title= 'Error!', message='Required fields missing?')
            elif not (passwordField.get().isalnum()):
                messagebox.askokcancel(title= 'Error!', message='Password should contain uppercase and numeric characters!')
            else:
                self.db.addNewAdmin(nameField.get(), mailField.get(), passwordField.get(), conatactField.get(), zipCodeField.get())
                messagebox.showinfo(title='Success', message='Registered successfully!!')
                self.window.destroy()
                # self.makeTopLevel()
                # Label(labelFrame, text='Registered Successfully!!', bg=labelFrameBG, font='Lucida 15 bold').grid(row=5, column=1)
    
        # self.window.destroy()
        
        self.window = Base().window
        self.window.title('Admin Register Page')
        labelFrame = LabelFrame(self.window, text='Admin Login', bg=labelFrameBG, fg='white', highlightbackground='white', font='lucida 12 bold', relief='solid', padx=20)
        labelFrame.pack(expand=True, fill=X)
        name = Label(labelFrame ,text = "Full Name", bg=labelFrameBG).grid(row = 0,column = 0)
        mail = Label(labelFrame ,text = "Email Id", bg=labelFrameBG).grid(row = 1,column = 0)
        password = Label(labelFrame ,text = "Password", bg=labelFrameBG).grid(row = 2,column = 0)
        contact = Label(labelFrame ,text = "Contact Number", bg=labelFrameBG).grid(row = 3,column = 0)
        zipCode = Label(labelFrame ,text = "Zip Code", bg=labelFrameBG).grid(row = 4,column = 0)
        nameField = Entry(labelFrame)
        nameField.grid(row = 0,column = 1)
        mailField = Entry(labelFrame)
        mailField.grid(row = 1,column = 1)
        passwordField = Entry(labelFrame)
        passwordField.grid(row = 2,column = 1)
        conatactField = Entry(labelFrame)
        conatactField.grid(row = 3,column = 1)
        zipCodeField = Entry(labelFrame)
        zipCodeField.grid(row = 4,column = 1)
        register = ttk.Button(labelFrame ,text="Register", command=successMessage).grid(row=5,column=0)
        
        # self.window.grab_set()
        # self.window.attributes("-topmost", True)
        self.loadUI()

    def makeTopLevel(self):
        self.window.attributes("-topmost", True)
    
    # To run the Admin page
    def loadUI(self):
        # self.window.grab_set()
        self.window.mainloop()
    
    def addNewUser(self):
        pass

    def UserExists(self):
        pass
        
# admin=AdminPage()
# admin.loadLoginPage()