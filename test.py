import mysql.connector
from tkinter import Tk, ttk
from tkinter import *
from utils.constants import *


def clickEvent():
    pass

root = Tk()

#---------------------------------------------------------------------------------------------
sideFrame = Frame(root, background=labelFrameBG)
sideFrame.pack(side=LEFT)
nameLabel = Label(sideFrame, text="Name:", fg='white', bg=labelFrameBG, font='lucida 10')
nameLabel.grid(column=0, row=0)
authorLabel = Label(sideFrame, text="Author:", fg='white', bg=labelFrameBG, font='lucida 10')
authorLabel.grid(column=0, row=1)
publishedYearLabel = Label(sideFrame, text="Published year:", fg='white', bg=labelFrameBG, font='lucida 10')
publishedYearLabel.grid(column=0, row=2)
publisherLabel = Label(sideFrame, text="Publisher:", fg='white', bg=labelFrameBG, font='lucida 10')
publisherLabel.grid(column=0, row=3)

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