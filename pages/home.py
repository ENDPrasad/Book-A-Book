from tkinter import Tk

from pages.Base import Base


class HomePage():
    def __init__(self) -> None:
        # super(self).__init__(self)
        self.window = Base().window
        self.window.title('Book Management System')
        label = label(self.window, 'Home Page')
        label.pack()
    


    # To run the Admin page
    def loadUI(self):
        self.window.mainloop()

        
        