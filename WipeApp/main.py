# This is a sample Python script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import curses

import tkinter

import customtkinter
from tkinter import ttk

from wipeMenu import wipeMenuClass
import uuid
import psutil

base = tkinter.Tk()


def print_first_mac_address():
    for interface_name, addresses in psutil.net_if_addrs().items():
        for addr in addresses:
            if addr.family == psutil.AF_LINK:  # Check for MAC address type
                return addr.address


def navigate_up(event):
    if event.keysym == "Up":

        thing = base.focus_get()

        if thing == bios:
            wipe.focus()
            wipe.configure(bg="#2D333A")
            bios.configure(bg="#434d57")

        elif thing == quit:
            bios.focus()
            bios.configure(bg="#2D333A")
            quit.configure(bg="#434d57")


def navigate_down(event):
    if event.keysym == "Down":
        print("hi")
        thing = base.focus_get()
        if thing == wipe:
            bios.focus()
            bios.configure(bg="#2D333A")
            wipe.configure(bg="#434d57")
        elif thing == bios:
            quit.focus()
            quit.configure(bg="#2D333A")
            bios.configure(bg="#434d57")


def focus(event):
    widget = base.focus_get()
    print(widget, "has focus")


def activate_button(event):
    current_focus = base.focus_get()
    if (current_focus == wipe):
        wipe_clicker()

    elif (current_focus == quit):
        base.quit()

def focus_on_wipe_button():
    wipe.focus
    base.bind("<Up>", navigate_up)
    base.bind("<Down>", navigate_down)
    base.bind("<Return>", activate_button)


def wipe_clicker():
    wipe_menu = wipeMenuClass(base, callback=focus_on_wipe_button)
    wipe_menu.setup_gui()


customtkinter.set_appearance_mode("dark")

base.attributes("-fullscreen", True)
base.configure(bg="#010101")
style = ttk.Style()
frame = ttk.Frame(base)
frame.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)
for i in range(3):  # 3 columns
    frame.grid_columnconfigure(i, weight=3)
    frame.grid_columnconfigure(0, weight=1)

for j in range(5):  # 5 rows
    frame.grid_rowconfigure(j, weight=1)

base.grid_rowconfigure(0, weight=1)
frame.configure(style="Custom.TFrame")
style.configure("Custom.TFrame", background="#708090")
frame.pack(fill="both", expand=True, pady=55, padx=55)

base.bind("<Up>", navigate_up)
base.bind("<Down>", navigate_down)
base.bind("<Return>", activate_button)

wipe = tkinter.Button(frame, text="Wipe", command=wipe_clicker, height=5, width=50, font=('Comfortaa', 14, 'bold'),
                      highlightthickness=0, borderwidth=0, fg="White", takefocus=False, bg="#434d57")

wipe.grid(column=1, row=0, sticky="nsew", pady=(80, 0))

bios = tkinter.Button(frame, text="Bios Setup", height=5, width=50, font=('Comfortaa', 14, 'bold'),
                      highlightthickness=0, borderwidth=0, fg="White", bg="#434d57")
bios.grid(column=1, row=1, sticky="nsew", pady=(80, 80))

quit = tkinter.Button(frame, text="Exit", command=base.quit, height=5, width=50, font=('Comfortaa', 14, 'bold'),
                      highlightthickness=0, borderwidth=0, fg="White", bg="#434d57")

quit.focus()

quit.grid(column=1, row=2, sticky="nsew", pady=(0, 50))
first_mac = print_first_mac_address()
mac = tkinter.Label(frame, text=f"Mac : {first_mac}", font=('Comfortaa', 18, 'bold'),
                    highlightthickness=0, borderwidth=0, fg="#FFFFFF", bg="#708090")

mac.grid(column=0, row=5, sticky="nsew")

try:
    base.mainloop()
except KeyboardInterrupt:
    print("Keyboard Interrupt")
