# This is a sample Python script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import curses

import tkinter

import customtkinter
from tkinter import ttk
from wipeMenu import wipeMenuClass
from cProfile import label
from tkinter.ttk import Style
from tkinter import Tk, font

base = tkinter.Tk()


def move_focus(event):
    if event.keysym == "Up":

        thing = base.focus_get()

        if thing == quit:
           wipe.focus()
           wipe.configure(bg="#2D333A")
           quit.configure(bg="#434d57")

    elif event.keysym == "Down":
        print("hi")
        thing = base.focus_get()
        if thing == wipe:
            quit.focus()
            quit.configure(bg="#2D333A")
            wipe.configure(bg="#434d57")



def focus(event):
    widget = base.focus_get()
    print(widget, "has focus")


def activate_button(event):
    current_focus = base.focus_get()
    if (current_focus == wipe):
        wipe_clicker()
    elif (current_focus == mac):
        mac_clicker()
    elif (current_focus == quit):
        base.quit()


# Actions performed when a button is chosen
def wipe_clicker():
    print("wipe")
    wipe_menu = wipeMenuClass(base)
    wipe_menu.setup_gui()

def mac_clicker():
    print("Mac")


#  my_label.configure(text=mac.cget("text"))

customtkinter.set_appearance_mode("dark")

# Code base interface.


base.attributes("-fullscreen", True)
base.configure(bg="#010101")

frame = ttk.Frame(base)
frame.configure(style="Custom.TFrame")
frame.pack(fill="both", expand=True, pady=55, padx=55)

base.bind("<Up>", move_focus)
base.bind("<Down>", move_focus)
base.bind("<Return>", activate_button)

# Wipe button
wipe = tkinter.Button(frame, text="Wipe", command=wipe_clicker, height=5, width=100, font=('Comfortaa', 14, 'bold'),
                      highlightthickness=0, borderwidth=0, fg="White", takefocus=False, bg="#434d57")
# wipe = customtkinter.CTkButton(frame, text="wipe", command=wipe_clicker, height=100, width=1000, hover_color="#272e34",fg_color="#434d57", font=("Davish", 20), bg_color="#708090")
wipe.pack(pady=(100, 80))

# MacAddress button


# QuitButton
quit = tkinter.Button(frame, text="Exit", command=base.quit, height=5, width=100, font=('Comfortaa', 14, 'bold'),
                      highlightthickness=0, borderwidth=0, fg="White", bg="#434d57")
# quit = customtkinter.CTkButton(frame, text="Exit", command=root.quit, height=100, width=1000, hover_color="#272e34",fg_color="#434d57", font=("Davish", 20), bg_color="#708090")
quit.focus()

print(base.focus_get())
quit.pack(pady=80)
mac = tkinter.Label(frame, text="Mac")
# mac = customtkinter.CTkButton(frame, text="mac", command=mac_clicker, height=100, width=1000, hover_color="#272e34",   fg_color="#434d57", font=("Davish", 20), bg_color="#708090")
mac.pack()
# Style
style = ttk.Style()
style.configure("Custom.TFrame", background="#708090")
base.mainloop()
