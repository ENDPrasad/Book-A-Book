from tkinter import Tk, ttk
from tkinter import *
from utils.constants import *


def clickEvent():
    pass

window = Tk()
# topFrame = Frame(window, bg=button_bg_color)
# topFrame.pack(fill=X, expand=True, anchor=N)
# profile = ttk.Button(topFrame, text='Profile', width=5, height=2, command=clickEvent)
# profile.pack(anchor=E)


mainFrame = Frame(window, bg=button_bg_color, name='add a book')
mainFrame.pack(fill=BOTH)
labelFrame = LabelFrame(mainFrame, text='Add a book', bg=labelFrameBG, fg='white', highlightbackground='white', font='lucida 12 bold', relief='solid', padx=20)
labelFrame.pack(expand=True, fill=X)
userLabel = Label(labelFrame, text='Book name', fg='white', bg=labelFrameBG, font='lucida 10 bold')
userLabel.pack(pady=3)
userName = ttk.Entry(labelFrame, width=30)
userName.pack(pady=3)
passLabel = Label(labelFrame, text='qunatity', fg='white', bg=labelFrameBG, font='lucida 10 bold')
passLabel.pack(pady=3)
password = ttk.Entry(labelFrame, width=30)
password.pack(pady=3)
addBook = Button(labelFrame, text='Add New book', command=clickEvent)
addBook.pack()


window.mainloop()