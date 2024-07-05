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

        if event.widget == wipe:
            print("hi")
            wipe.focus_set()
            wipe.configure(fg_color="#434d57")
        elif event.widget == mac:
            wipe.focus_set()
            wipe.configure(fg_color="#272e34")
            mac.configure(fg_color="#434d57")
        elif event.widget == quit:
            mac.focus_set()
            mac.configure(fg_color="#272e34")
    elif event.keysym == "Down":
        print("bye")
        if event.widget==wipe:
            mac.focus_set()
            mac.configure(fg_color="#272e34")
        elif event.widget == mac:
            quit.focus_set()
            quit.configure(fg_color="#272e34")
        elif event.widget == quit:
            quit.focus_set()
            quit.configure(fg_color="#272e34")


#Actions performed when a button is chosen
def wipe_clicker():
    print("wipe")

def mac_clicker():
    print("Mac")
  #  my_label.configure(text=mac.cget("text"))

customtkinter.set_appearance_mode("dark")

#Code base interface.
root = customtkinter.CTk()


root.attributes("-fullscreen", True)
frame = ttk.Frame(root)
frame.configure(style="Custom.TFrame")
frame.pack(fill="both", expand=True, pady=55, padx=55)
root.bind("<Up>", move_focus)
root.bind("<Down>", move_focus)
#Wipe button
wipe = customtkinter.CTkButton(frame, text="wipe", command=wipe_clicker, height=100, width=1000, hover_color="#272e34", fg_color="#434d57", font=("Davish", 20), bg_color="#708090")
wipe.pack(pady=(200, 80))

#MacAddress button
mac=customtkinter.CTkButton(frame,text="Addresse Mac",command=mac_clicker, height=100, width=1000, hover_color="#272e34", fg_color="#434d57",  font=("Davish", 20),  bg_color="#708090")
mac.pack(pady=80)


#QuitButton
quit= customtkinter.CTkButton(frame, text="Exit", command=root.quit, height=100, width=1000, hover_color="#272e34", fg_color="#434d57", font=("Davish", 20),  bg_color="#708090")
quit.pack(pady=80)

#Style
style = ttk.Style()
style.configure("Custom.TFrame", background="#708090")

wipe.focus_set()
wipe.configure(fg_color="#272e34")

root.mainloop()