from functools import partial
import mysql.connector
from tkinter import Tk, ttk
from tkinter import *
from utils.constants import *


def clickEvent():
    pass

connection = ''
cursor = ''
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='book_management_system',
                                         user='root',
                                         password='Prasad@421')
    print("DB started successfully ")
    cursor = connection.cursor()
except mysql.connector.Error as error:
    print("Failed to start MySQL: {}".format(error))


def bookInfo(event):
    value = str(list_books.get(list_books.curselection()))
    name = value.split(".")[1]
    print(name)
    cursor.execute("select * from books where name='"+name+"'")
    book_data = cursor.fetchall()
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
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    count = 0
    for book in books:
        list_books.insert(count, str(count+1)+"."+book[0])
        count += 1
    list_books.bind("<<ListboxSelect>>", bookInfo)
    


root = Tk()

#--------------------------------------------------------------
mainFrame = Frame(root)
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

def searchBook(name, zipcode):
    pass

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
submit = Button(searchBar, text='Search', command=partial(searchBook, bookName.get(), zipcode.get()),fg='white', bg=button_bg_color, font='Lucida 12 bold')
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

#---------------------------------------------------------------------------------------------
# sideFrame = Frame(root, background=labelFrameBG)
# sideFrame.pack(side=LEFT)
# nameLabel = Label(sideFrame, text="Name:", fg='white', bg=labelFrameBG, font='lucida 10')
# nameLabel.grid(column=0, row=0)
# authorLabel = Label(sideFrame, text="Author:", fg='white', bg=labelFrameBG, font='lucida 10')
# authorLabel.grid(column=0, row=1)
# publishedYearLabel = Label(sideFrame, text="Published year:", fg='white', bg=labelFrameBG, font='lucida 10')
# publishedYearLabel.grid(column=0, row=2)
# publisherLabel = Label(sideFrame, text="Publisher:", fg='white', bg=labelFrameBG, font='lucida 10')
# publisherLabel.grid(column=0, row=3)

#----------------------------------------------------------------
# topFrame = Frame(window, bg=button_bg_color)
# topFrame.pack(fill=X, expand=True, anchor=N)
# profile = ttk.Button(topFrame, text='Profile', width=5, height=2, command=clickEvent)
# profile.pack(anchor=E)


# def OnDoubleClick(self):
#         item = tree.selection()[0]
#         print(tree.item(item)["values"][0])
#         # print("you clicked on", tree.item(item,"text"))



# def ShowBooksTable():
#     con1 = mysql.connector.connect(host='localhost',
#                                          database='book_management_system',
#                                          user='root',
#                                          password='Prasad@421')
#     cur1 = con1.cursor()
#     cur1.execute("SELECT * FROM books")
#     rows = cur1.fetchall()    
#     for row in rows:
#         print(row) 
#         tree.insert("", END, values=row)
#         tree.bind("<Double-1>", OnDoubleClick)        
#     con1.close()




# tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')
# tree.column("#1", anchor=CENTER)
# tree.heading("#1", text="Name")
# tree.column("#2", anchor=CENTER)
# tree.heading("#2", text="Price")
# tree.column("#3", anchor=CENTER)
# tree.heading("#3", text="Publisher Name")
# tree.pack()
# button1 = Button(text="Display data", command=ShowBooksTable)
# button1.pack(pady=10)

# root.mainloop()


# rows = []

# for i in range(5):

#     cols = []

#     for j in range(4):

#         e = Entry(window, relief=GROOVE)

#         e.grid(row=i, column=j, sticky=NSEW)

#         e.insert(END, '%d.%d' % (i, j))

#         cols.append(e)

#     rows.append(cols)



root.mainloop()