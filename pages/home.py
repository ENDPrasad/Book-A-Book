from tkinter import *

from pages.Base import Base


class HomePage():
    def __init__(self, adminDetails) -> None:
        # super(self).__init__(self)
        self.window = Base().window
        self.window.title('Book Management System')
        self.adminDetails = adminDetails
        print(self.adminDetails)
        label = Label(self.window, text='Hello '+ self.adminDetails[0][0])
        label.pack()
    


    # To run the Admin page
    def loadUI(self):
        self.window.mainloop()

        
        