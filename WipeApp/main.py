# This is a sample Python script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import curses

import tkinter
from cProfile import label


#Code base interface.
root = tkinter.Tk()
root.geometry("1920x1080")
wipe = tkinter.Button(root, text="Wipe", command=print("wipe"))
root.configure(bg="#35454F")
wipe.pack()
mac=tkinter.Button(root,text="Addresse Mac",command=print("IP"))
mac.pack()
quit= tkinter.Button(master=root, text="Exit", command=root.quit)
quit.pack()
root.mainloop()