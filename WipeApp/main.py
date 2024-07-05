# This is a sample Python script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import curses

import tkinter
import customtkinter
from cProfile import label
from tkinter.ttk import Style

#Actions performed when a button is chosen
def wipe_clicker():
    print("wipe")

def mac_clicker():
    print("Mac")



#Code base interface.
root = tkinter.Tk()
root.geometry("1920x1080")
root.configure(bg="#35454F")

#Wipe button
wipe = tkinter.Button(root, text="Wipe", command=wipe_clicker)
wipe.pack()

#MacAddress button
mac=tkinter.Button(root,text="Addresse Mac",command=mac_clicker)
mac.pack()

#QuitButton
quit= tkinter.Button(master=root, text="Exit", command=root.quit)
quit.pack()

root.mainloop()