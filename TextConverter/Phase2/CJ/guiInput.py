# -*- coding: utf-8 -*-

from Tkinter import *


master = Tk()
master.title('Text Encoder')

e = StringVar()


# Variable to hold the input
inp = None
L1 = Label(master)
L1.pack(side = LEFT)

E1 = Entry(master, textvariable = e)
E1.pack(side = RIGHT)

def userinput():
    # Declare 'inp' to be global
    global inp
    a = (e.get())
    print a
    # Update the variable
    inp = a



b = Button(master, text = 'Encode', command = userinput)
b.pack(side = BOTTOM)


master.mainloop()
