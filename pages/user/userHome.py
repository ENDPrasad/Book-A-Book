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
            self.db.cursor.execute("SELECT * FROM books")
            books = self.db.cursor.fetchall()
            count = 0
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
        tabs.add(tab1, text='Book Details', compound=LEFT)
        tabs.add(tab2, text='Your Orders', compound=LEFT)
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
     
        # topFrame = Frame(self.window, bg=button_bg_color)
        # topFrame.pack(fill=X, expand=True, anchor=N)
        # profile = Button(topFrame, text='Profile', width=5, height=2, command=self.viewProfile)
        # profile.pack(anchor=E)
        # searchFrame = Frame(self.window, bg=button_bg_color)
        # searchFrame.pack(fill=X, expand=True)
        # bookNameLabel = Label(searchFrame, text='book name', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        # bookNameLabel.pack(pady=3, side=LEFT)
        # bookName = ttk.Entry(searchFrame, width=30)
        # bookName.pack(pady=3, side=LEFT)
        # zipcodeLabel = Label(searchFrame, text='Zipcode', fg='white', bg=labelFrameBG, font='lucida 10 bold')
        # zipcodeLabel.pack(pady=3, side=LEFT)
        # zipcode = ttk.Entry(searchFrame, width=30)
        # zipcode.pack(pady=3, side=LEFT)
        # submit = Button(searchFrame, text='Search', command=partial(self.searchBook, bookName.get(), zipcode.get()),fg='white', bg=button_bg_color, font='Lucida 12 bold')
        # submit.pack(pady=3, side=LEFT)

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