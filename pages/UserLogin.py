from tkinter import Tk

from pages.Base import Base


class UserLogin():
    def __init__(self) -> None:
        # super(self).__init__(self)
        self.window = Base().window
        self.window.title('User Login Page')

    # To run the login page
    def loadUI(self):
        self.window.mainloop()

        
        