# Importing tkinter module
# and all functions
from tkinter import *
from tkinter.ttk import *

# creating master window
master = Tk()

# This method is used to get
# the name of the widget
# which currently has the focus
# by clicking Mouse Button-1
def focus(event):
    widget = master.focus_get()
    print(widget, "has focus")

# Entry widget
e1 = Entry(master)
e1.pack(expand = 1, fill = BOTH)

# Button Widget
e2 = Button(master, text ="Button")
e2.pack(pady = 5)

# Radiobutton widget
e3 = Radiobutton(master, text ="Hello")
e3.pack(pady = 5)

# Here function focus() is binded with Mouse Button-1
# so every time you click mouse, it will call the
# focus method, defined above
master.bind_all("<Button-1>", lambda e: focus(e))

# infinite loop
mainloop()