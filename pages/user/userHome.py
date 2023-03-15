from functools import partial
from tkinter import *
from tkinter import ttk
from pages.Base import Base
from pages.db import Database

# from pages.Base import Base
from utils.constants import *


class UserHomePage():
    def __init__(self, userDetails) -> None:
        # super(self).__init__(self)
        self.window = Base().window
        self.window.title('Book Management System')
        self.userDetails = userDetails
        self.db = Database()
        self.loadDashboard()
        self.loadBooks()
        self.loadUI()
    
    def loadDashboard(self):
        topFrame = Frame(self.window, bg=button_bg_color)
        topFrame.pack(fill=X, expand=True, anchor=N)
        profile = Button(topFrame, text='Profile', width=5, height=2, command=self.viewProfile)
        profile.pack(anchor=E)
        searchFrame = Frame(self.window, bg=button_bg_color)
        searchFrame.pack(fill=X, expand=True)
        bookNameLabel = Label(searchFrame, text='book name', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        bookNameLabel.pack(pady=3, side=LEFT)
        bookName = ttk.Entry(searchFrame, width=30)
        bookName.pack(pady=3, side=LEFT)
        zipcodeLabel = Label(searchFrame, text='Zipcode', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        zipcodeLabel.pack(pady=3, side=LEFT)
        zipcode = ttk.Entry(searchFrame, width=30)
        zipcode.pack(pady=3, side=LEFT)
        submit = Button(searchFrame, text='Search', command=partial(self.searchBook, bookName.get(), zipcode.get()),fg='white', bg=button_bg_color, font='Lucida 12 bold')
        submit.pack(pady=3, side=LEFT)

    def searchBook(self, bookName, zipcode):
        data = self.db.searchBooks(bookName, zipcode)
        print('Searched Data-', data)
        self.loadBooks(data)

    # def loadBookDetails(self):
    #     sideFrame = Frame(self.window, bg=button_bg_color, width=100)
    #     item = self.window.selection()[0]
    #     bookData = self.window.item(item)["values"][0]
    #     nameLabel = Label(sideFrame, text=bookData[0], fg='white', bg=labelFrameBG, font='lucida 10 bold')
    #     nameLabel.pack(pady=10)
    #     authorLabel = Label(sideFrame, text=bookData[2], fg='white', bg=labelFrameBG, font='lucida 10 bold')
    #     authorLabel.pack(pady=10)


    def loadBooks(self, bookData=''):
        def loadBookDetails(event):
            sideFrame = Frame(self.window, bg=button_bg_color)
            sideFrame.pack(fill=BOTH, expand=True, side=LEFT)
            item = tree.selection()[0]
            # print(item)
            bookName = tree.item(item)["values"][0]
            publisher = tree.item(item)["values"][2]
            print("Item Data:", item)
            nameLabel = Label(sideFrame, fg='white', bg=labelFrameBG, font='lucida 10 bold')
            authorLabel = Label(sideFrame, fg='white', bg=labelFrameBG, font='lucida 10 bold')
            nameLabel.config(text=bookName)
            authorLabel.config(text=publisher)
            nameLabel.pack(pady=10)
            authorLabel.pack(pady=10)
            # self.loadUI()
        
        rows = ''
        if bookData == '':
            rows = self.db.getBooks()
        else:
            rows = bookData
        print("Total books:")
        print(rows)
        displayFrame = Frame(self.window, bg=button_bg_color)
        displayFrame.pack(fill=BOTH, expand=True, side=LEFT)
        # listOfBooks = Listbox(displayFrame)
        tree = ttk.Treeview(displayFrame, column=("c1", "c2", "c3"), show='headings')
        tree.column("#1", anchor=CENTER)
        tree.heading("#1", text="Name")
        tree.column("#2", anchor=CENTER)
        tree.heading("#2", text="Price")
        tree.column("#3", anchor=CENTER)
        tree.heading("#3", text="Author")
        tree.pack()
        for row in rows:
            print(row) 
            tree.insert("", END, values=row)
            tree.bind("<Double-1>", loadBookDetails)
            

    # Profile Page
    def viewProfile(self):
        pass

    # To run the Admin page
    def loadUI(self):
        self.window.mainloop()

        
        
# user = UserHomePage([['Prasad']])
# user.loadDashboard()
# user.loadUI()