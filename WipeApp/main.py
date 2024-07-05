# This is a sample Python script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import curses

import tkinter
import customtkinter
from tkinter import ttk
from cProfile import label
from tkinter.ttk import Style

#Actions performed when a button is chosen
def wipe_clicker():
    print("wipe")

def mac_clicker():
    print("Mac")
  #  my_label.configure(text=mac.cget("text"))



#Code base interface.
root = customtkinter.CTk()
root.attributes("-fullscreen", True)
root.configure(bg="#708090")
frame = ttk.Frame(root)
frame.configure(style="Custom.TFrame")
#Wipe button
wipe = customtkinter.CTkButton(root, text="wipe", command=wipe_clicker, height=100, width=1000, hover_color="green", fg_color="#708090", font=("Davish", 20))
wipe.pack(pady=80)

#MacAddress button
mac=customtkinter.CTkButton(root,text="Addresse Mac",command=mac_clicker, height=100, width=1000, hover_color="green", fg_color="#708090",  font=("Davish", 20))
mac.pack(pady=80)

#my_label = customtkinter.CTkLabel(root,text="")
#my_label.pack(pady=80)
#QuitButton
quit= customtkinter.CTkButton(master=root, text="Exit", command=root.quit, height=100, width=1000, hover_color="green", fg_color="#708090", font=("Davish", 20))
quit.pack(pady=80)

root.mainloop()