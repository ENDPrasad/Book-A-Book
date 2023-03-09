from tkinter import *
from pages.Base import Base

# from pages.Base import Base
from utils.constants import *


class UserHomePage():
    def __init__(self, userDetails) -> None:
        # super(self).__init__(self)
        self.window = Base().window
        self.window.title('Book Management System')
        self.userDetails = userDetails
        print(self.userDetails)
        label = Label(self.window, text='Hello '+ self.userDetails[0][0])
        label.pack()
    
    def loadDashboard(self):
        topFrame = Frame(self.window, bg=button_bg_color)
        topFrame.pack(fill=X, expand=True, anchor=N)
        profile = Button(topFrame, text='Profile', width=5, height=2, command=self.viewProfile)
        profile.pack(anchor=E)

    # Profile Page
    def viewProfile(self):
        pass

    # To run the Admin page
    def loadUI(self):
        self.window.mainloop()

        
        
# user = UserHomePage([['Prasad']])
# user.loadDashboard()
# user.loadUI()