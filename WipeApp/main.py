# This is a sample Python script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import curses

import tkinter
import customtkinter
from tkinter import ttk
from cProfile import label
from tkinter.ttk import Style


def move_focus(event):
    if event.keysym == "Up":

        if root.focus_get() == wipe:

            wipe.focus()
            print(wipe.focus_get())
            wipe.configure(bg="#434d57")

        elif root.focus_get() == mac:
            wipe.focus()
            wipe.configure(bg="#272e34")
            mac.configure(bg="#434d57")

        elif root.focus_get() == quit:
            mac.focus()
            mac.configure(bg="#272e34")

    elif event.keysym == "Down":
        print("bye")
        if root.focus_get() == wipe:
            mac.focus()
            mac.configure(fg_color="#272e34")

        elif root.focus_get() == mac:
            quit.focus()
            quit.configure(fg_color="#272e34")

        elif root.focus_get() == quit:
            quit.focus()
            quit.configure(fg_color="#272e34")


def focus(event):
    widget = root.focus_get()
    print(widget, "has focus")


def activate_button(event):
    print("lol")
    current_focus = root.focus_get()
    if (current_focus == wipe):
        wipe_clicker()
    elif (current_focus == mac):
        mac_clicker()
    elif (current_focus == quit):
        root.quit()



# Actions performed when a button is chosen
def wipe_clicker():
    print("wipe")


def mac_clicker():
    print("Mac")


#  my_label.configure(text=mac.cget("text"))

customtkinter.set_appearance_mode("dark")

# Code base interface.
root = tkinter.Tk()

root.attributes("-fullscreen", True)
root.configure(bg="#010101")
frame = ttk.Frame(root)
frame.configure(style="Custom.TFrame")
frame.pack(fill="both", expand=True, pady=55, padx=55)
root.bind("<Up>", move_focus)
root.bind("<Down>", move_focus)
root.bind("<Return>", activate_button)




# Wipe button
wipe = tkinter.Button(frame, text="wipe", command=wipe_clicker(), height=10, width=40)
#wipe = customtkinter.CTkButton(frame, text="wipe", command=wipe_clicker, height=100, width=1000, hover_color="#272e34",fg_color="#434d57", font=("Davish", 20), bg_color="#708090")
wipe.pack(pady=(200, 80))

# MacAddress button
mac = tkinter.Button(frame, text="mac", command=mac_clicker, height=10, width=40)
#mac = customtkinter.CTkButton(frame, text="wipe", command=mac_clicker, height=100, width=1000, hover_color="#272e34",   fg_color="#434d57", font=("Davish", 20), bg_color="#708090")
mac.pack(pady=80)

# QuitButton
quit = tkinter.Button(frame, text="Exit", command=root.quit, height=10, width=40)
#quit = customtkinter.CTkButton(frame, text="Exit", command=root.quit, height=100, width=1000, hover_color="#272e34",fg_color="#434d57", font=("Davish", 20), bg_color="#708090")
quit.focus()
print(root.focus_get())
quit.pack(pady=80)

# Style
style = ttk.Style()
style.configure("Custom.TFrame", background="#708090")


root.mainloop()
