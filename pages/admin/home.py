from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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
            try:
                self.db.addNewBook(name=bookName.get(), publisher_name=pbName.get(), published_year=pbYear.get(),book_store=self.adminDetails[0][0],quantity=quantity.get(), price=price.get(), author=author.get())
                messagebox.askokcancel("Success", "Book added successfully!!")
                bookName.delete(0, END)
                pbName.delete(0, END)
                pbYear.delete(0, END)
                price.delete(0, END)
                author.delete(0, END)
                quantity.delete(0, END)
            except Exception as ex:
                print('Unable to add book!!')
                print(ex)


        mainFrame = Frame(self.window, bg=button_bg_color)
        mainFrame.pack(fill=BOTH)
        labelFrame = LabelFrame(mainFrame, text='Add a book', bg=labelFrameBG, fg='white', highlightbackground='white', font='lucida 12 bold', relief='solid', padx=20)
        labelFrame.pack(expand=True, fill=X)
        nameLabel = Label(labelFrame, text='Book name', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        nameLabel.pack(pady=2)
        bookName = ttk.Entry(labelFrame, width=30)
        bookName.pack(pady=2)
        quantityLabel = Label(labelFrame, text='qunatity', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        quantityLabel.pack(pady=2)
        quantity = ttk.Entry(labelFrame, width=30)
        quantity.pack(pady=2)
        
        pbNameLabel = Label(labelFrame, text='Publisher Name', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        pbNameLabel.pack(pady=2)
        pbName = ttk.Entry(labelFrame, width=30)
        pbName.pack(pady=2)
        pbYearLabel = Label(labelFrame, text='Published Year', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        pbYearLabel.pack(pady=2)
        pbYear = ttk.Entry(labelFrame, width=30)
        pbYear.pack(pady=2)
        priceLabel = Label(labelFrame, text='Price', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        priceLabel.pack(pady=2)
        price = ttk.Entry(labelFrame, width=30)
        price.pack(pady=2)

        authorLabel = Label(labelFrame, text='Author', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        authorLabel.pack(pady=2)
        author = ttk.Entry(labelFrame, width=30)
        author.pack(pady=2)
        addBook = Button(labelFrame, text='Add New book', command=addNewBook)
        addBook.pack()


    # To run the Admin page
    def loadUI(self):
        self.window.mainloop()
