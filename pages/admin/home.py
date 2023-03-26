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
        def bookInfo(event):
            value = str(list_books.get(list_books.curselection()))
            name = value.split(".")[1]
            print(name)
            self.db.cursor.execute("select * from books where name='"+name+"'")
            book_data = self.db.cursor.fetchall()
            print(book_data)
            listDetails.delete(0, END)
            listDetails.insert(0, 'Book Name: '+book_data[0][0])
            listDetails.insert(1, 'Price: '+str(book_data[0][1]))
            listDetails.insert(2, 'Author: '+book_data[0][2])
            listDetails.insert(3, 'Published Year: '+str(book_data[0][3]))
            listDetails.insert(4, 'Store Name: '+book_data[0][4])
            listDetails.insert(5, 'Quantity: '+str(book_data[0][5]))
            listDetails.insert(6, 'Publisher Name: '+str(book_data[0][6]))


        def displayBooks():
            self.db.cursor.execute("SELECT books.* FROM books where book_store ='"+self.adminDetails[0][0]+"'")
            books = self.db.cursor.fetchall()
            print(books)
            count = 0
            list_books.delete(0, END)
            for book in books:
                list_books.insert(count, str(count+1)+"."+book[0])
                count += 1
            list_books.bind("<<ListboxSelect>>", bookInfo)
    

        mainFrame = Frame(self.window)
        mainFrame.pack()
        # top frame
        topFrame = Frame(mainFrame, width=900, height=70, relief=SUNKEN, bg="#f8f8f8", borderwidth=2)
        topFrame.pack(side=TOP, fill=X)
        # center frame
        centerFrame = Frame(mainFrame, width=900, height=530, relief=SUNKEN, bg="#e0f0f0", borderwidth=2)
        centerFrame.pack()
        # center left Frame
        centerLeftFrame = Frame(centerFrame, width=600, height=530, relief=SUNKEN, bg="#e0f0f0", borderwidth=2)
        centerLeftFrame.pack(side=LEFT)
        # center right Frame
        centerRightFrame = Frame(centerFrame, width=300, height=530, relief=SUNKEN, bg="#e0f0f0", borderwidth=2)
        centerRightFrame.pack()  


        def searchBook():
            value = bookName.get()
            query = "SELECT books.* FROM books INNER JOIN Admin ON Admin.name = Books.book_store WHERE Books.name LIKE '%"+value+"%' "
            if zipcode.get() != "":
                query += "and Admin.zipCode="+zipcode.get()
            self.db.cursor.execute(query)
            # and Admin.zipCode="+zipcode.get()+"")
            searchedData = self.db.cursor.fetchall()
            print(searchedData)
            if len(searchedData) != 0:
                list_books.delete(0, END)
                count = 0
                for data in searchedData:
                    list_books.insert(count, str(count+1)+"."+data[0])
                    count += 1
        
        # search bar
        searchBar = LabelFrame(centerRightFrame, width=300, height=200, text='Search box', bg='#9bc9ff')
        searchBar.pack(fill=BOTH)

        bookNameLabel = Label(searchBar, text='book name', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        bookNameLabel.grid(row=0, column=0)
        bookName = ttk.Entry(searchBar, width=30)
        bookName.grid(row=0, column=1)
        zipcodeLabel = Label(searchBar, text='Zipcode', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        zipcodeLabel.grid(row=1, column=0)
        zipcode = ttk.Entry(searchBar, width=30)
        zipcode.grid(row=1, column=1)
        submit = Button(searchBar, text='Search', command=searchBook,fg='white', bg=button_bg_color, font='Lucida 12 bold')
        submit.grid(row=2, column=1)

        # List of books
        tabs = ttk.Notebook(centerLeftFrame,width=600, height=530)
        tabs.pack()
        tab1 = ttk.Frame(tabs)
        tab2 = ttk.Frame(tabs)
        tabs.add(tab1, text='Your books', compound=LEFT)
        tabs.add(tab2, text='Orders', compound=LEFT)
        list_books = Listbox(tab1, width=40, height=30, bd=2)
        scroll_bar = Scrollbar(tab1, orient=VERTICAL)
        list_books.grid(row=0, column=0, padx=(10,0), pady=10, sticky=N)
        scroll_bar.config(command=list_books.yview)
        list_books.config(yscrollcommand=scroll_bar.set)
        scroll_bar.grid(row=0, column=0, sticky=N+S+E)

        displayBooks()
        # list details
        listDetails = Listbox(tab1, width=80, height=30, bd=2)
        listDetails.grid(row=0, column=1, padx=(10,0), pady=10, sticky=N)
     
        # def addNewBook():
        #     try:
        #         self.db.addNewBook(name=bookName.get(), publisher_name=pbName.get(), published_year=pbYear.get(),book_store=self.adminDetails[0][0],quantity=quantity.get(), price=price.get(), author=author.get())
        #         messagebox.askokcancel("Success", "Book added successfully!!")
        #         bookName.delete(0, END)
        #         pbName.delete(0, END)
        #         pbYear.delete(0, END)
        #         price.delete(0, END)
        #         author.delete(0, END)
        #         quantity.delete(0, END)
        #     except Exception as ex:
        #         print('Unable to add book!!')
        #         print(ex)


        # mainFrame = Frame(self.window, bg=button_bg_color)
        # mainFrame.pack(fill=BOTH)
        # labelFrame = LabelFrame(mainFrame, text='Add a book', bg=labelFrameBG, fg='white', highlightbackground='white', font='lucida 12 bold', relief='solid', padx=20)
        # labelFrame.pack(expand=True, fill=X)
        # nameLabel = Label(labelFrame, text='Book name', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        # nameLabel.pack(pady=2)
        # bookName = ttk.Entry(labelFrame, width=30)
        # bookName.pack(pady=2)
        # quantityLabel = Label(labelFrame, text='qunatity', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        # quantityLabel.pack(pady=2)
        # quantity = ttk.Entry(labelFrame, width=30)
        # quantity.pack(pady=2)
        
        # pbNameLabel = Label(labelFrame, text='Publisher Name', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        # pbNameLabel.pack(pady=2)
        # pbName = ttk.Entry(labelFrame, width=30)
        # pbName.pack(pady=2)
        # pbYearLabel = Label(labelFrame, text='Published Year', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        # pbYearLabel.pack(pady=2)
        # pbYear = ttk.Entry(labelFrame, width=30)
        # pbYear.pack(pady=2)
        # priceLabel = Label(labelFrame, text='Price', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        # priceLabel.pack(pady=2)
        # price = ttk.Entry(labelFrame, width=30)
        # price.pack(pady=2)

        # authorLabel = Label(labelFrame, text='Author', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        # authorLabel.pack(pady=2)
        # author = ttk.Entry(labelFrame, width=30)
        # author.pack(pady=2)
        # addBook = Button(labelFrame, text='Add New book', command=addNewBook)
        # addBook.pack()


    # To run the Admin page
    def loadUI(self):
        self.window.mainloop()
