from tkinter import *
from tkinter import ttk

from pages.Base import Base
from pages.db import Database
from utils.constants import *


class HomePage():
    def __init__(self, adminDetails) -> None:
        # super(self).__init__(self)
        self.window = Base().window
        self.window.title('Book Management System')
        self.adminDetails = adminDetails
        print(adminDetails)
        self.db = Database()
        self.loadDashboard()
        self.loadUI()
        
    
    def loadDashboard(self):

        def addNewBook():
            self.db.addNewBook(name=bookName.get(), publisher_name=pbName.get(), published_year=pbYear.get(),book_store=self.adminDetails[0][0],quantity=quantity.get(), price=price.get())

        mainFrame = Frame(self.window, bg=button_bg_color)
        mainFrame.pack(fill=BOTH)
        labelFrame = LabelFrame(mainFrame, text='Add a book', bg=labelFrameBG, fg='white', highlightbackground='white', font='lucida 12 bold', relief='solid', padx=20)
        labelFrame.pack(expand=True, fill=X)
        nameLabel = Label(labelFrame, text='Book name', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        nameLabel.pack(pady=3)
        bookName = ttk.Entry(labelFrame, width=30)
        bookName.pack(pady=3)
        quantityLabel = Label(labelFrame, text='qunatity', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        quantityLabel.pack(pady=3)
        quantity = ttk.Entry(labelFrame, width=30)
        quantity.pack(pady=3)
        
        pbNameLabel = Label(labelFrame, text='Publisher Name', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        pbNameLabel.pack(pady=3)
        pbName = ttk.Entry(labelFrame, width=30)
        pbName.pack(pady=3)
        pbYearLabel = Label(labelFrame, text='Published Year', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        pbYearLabel.pack(pady=3)
        pbYear = ttk.Entry(labelFrame, width=30)
        pbYear.pack(pady=3)
        priceLabel = Label(labelFrame, text='Price', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        priceLabel.pack(pady=3)
        price = ttk.Entry(labelFrame, width=30)
        price.pack(pady=3)
        addBook = Button(labelFrame, text='Add New book', command=addNewBook)
        addBook.pack()


    # To run the Admin page
    def loadUI(self):
        self.window.mainloop()
