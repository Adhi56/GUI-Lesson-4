from tkinter import *
from tkinter.ttk import *
import time

root = Tk()
root.geometry("650x600")
root.title("Library system")
root.config(background="light blue")

booklabel = Label(root, text="Choose a Book", background="light blue")
booklabel.place(x=100, y=40)

scroll = Scrollbar(root)
scroll.place(x=350, y=80, height=120)

booklist = Listbox(root, height=6, width=35)
booklist.place(x=100, y=80)

booklist.config(yscrollcommand=scroll.set)
scroll.config(command=booklist.yview)

booklist.insert(END, "Harry Potter")
booklist.insert(END, "The Hobbit")
booklist.insert(END, "Wimpy Kid")
booklist.insert(END, "The Lion King")
booklist.insert(END, "Percy Jackson")

authorlabel = Label(root, text="Author", background="light blue")
authorlabel.place(x=100, y=230)

authorentry = Entry(root, width=35)
authorentry.place(x=220, y=230)

chosenlabel = Label(root, text="Your Books", background="light blue")
chosenlabel.place(x=100, y=300)

scroll2 = Scrollbar(root)
scroll2.place(x=520, y=330, height=200)

chosenlist = Listbox(root, height=12, width=50)
chosenlist.place(x=100, y=330)

chosenlist.config(yscrollcommand=scroll2.set)
scroll2.config(command=chosenlist.yview)

def addbook():
    index = booklist.curselection()
    author = authorentry.get()
    if index != () and author != "":
        book = booklist.get(index)
        chosenlist.insert(END, book + " by " + author)
        authorentry.delete(0, END)


addbutton = Button(root, text="Add Book", width=15, command=addbook)
addbutton.place(x=420, y=40)

progress = Progressbar(root, orient="horizontal", length=150, mode="indeterminate")
progress.place(x=250, y=550)

def loadbar():
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 100
    root.update_idletasks()
    time.sleep(0.5)

loadbutton = Button(root, text="Load System", width=15, command=loadbar)
loadbutton.place(x=260, y=500)

root.mainloop()
