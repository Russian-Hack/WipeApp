# This is a sample Python script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import curses

import tkinter
from cProfile import label



root = tkinter.Tk()

wipe = tkinter.Button(root, text="Wipe", command=print("wipe"))

mac=tkinter.Button(root,text="Addresse Mac",command=print("IP"))
mac.pack()

quit= tkinter.Button(master=root, text="Exit", command=root.quit)

quit.pack()

root.mainloop()