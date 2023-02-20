from tkinter import *

from pages.Base import Base


class UserHomePage():
    def __init__(self, userDetails) -> None:
        # super(self).__init__(self)
        self.window = Base().window
        self.window.title('Book Management System')
        self.userDetails = userDetails
        print(self.userDetails)
        label = Label(self.window, text='Hello '+ self.userDetails[0][0])
        label.pack()
    


    # To run the Admin page
    def loadUI(self):
        self.window.mainloop()

        
        