from tkinter import *
from tkinter import colorchooser

root = Tk()
root.geometry("300x350")
root.title('Colour Picker')
root.config(background='white')

def open_colour_wheel():
    colour = colorchooser.askcolor()[1]
    if colour:
        frame.config(background= colour)


frame = Frame(root, width= 200, height= 200, background= 'grey')
frame.pack(pady = 20)

colourpickbutton = Button(root, text= 'Pick A Colour', fg = 'black', bg = 'white', bd = 20, command= open_colour_wheel)
colourpickbutton.pack(side= 'bottom', pady = 5)















root.mainloop()