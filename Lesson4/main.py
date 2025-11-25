from tkinter import *
import calendar

root = Tk()
root.geometry("300x400")
root.title('Calendar')
root.config(background= 'white')

def show_calendar():
    newroot = Tk()
    newroot.geometry('600x600')
    newroot.title('Calendar')
    newroot.config(background= 'white')
    
    year = int(yearentry.get())
    calendarcontent = calendar.calendar(year)

    calendaryear = Label(newroot, text= calendarcontent, font = 'Consolas 10 bold')
    calendaryear.grid(row=5,column=0,padx=20)

calendarlabel = Label(root, text= 'Calendar', bg= 'white', fg = 'grey', bd = 40)
calendarlabel.pack(side= 'top')

yearlabel = Label(root, text= 'What year would you like to see?', bg = 'White', fg= 'grey', bd = 25)
yearlabel.pack(side= 'top')

yearentry = Entry(root, width= 35)
yearentry.pack(side= 'top', pady= 5)

exitbutton = Button(root, text= 'Exit', fg = 'black', bg = 'white', bd = 15, command= root.destroy)
exitbutton.pack(side = 'bottom', pady= 20)

showcalendarbutton = Button(root, text= 'Show Calendar', bg = 'white', fg = 'black', bd = 15, command= show_calendar)
showcalendarbutton.pack(side= 'bottom', pady= 10)












root.mainloop()