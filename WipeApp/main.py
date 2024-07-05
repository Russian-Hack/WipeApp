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

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("C:/Users/Filni1/OneDrive - BuroVirtuel/Bureau/WipeApp/WipeApp/dark_blue.json")

#Code base interface.
root = customtkinter.CTk()
root.attributes("-fullscreen", True)
root.configure(bg="#35454F")

#Wipe button
wipe = customtkinter.CTkButton(root, text="wipe", command=wipe_clicker)
wipe.pack(pady=80)

#MacAddress button
mac=customtkinter.CTkButton(root,text="Addresse Mac",command=mac_clicker)
mac.pack(pady=80)

#QuitButton
quit= customtkinter.CTkButton(master=root, text="Exit", command=root.quit)
quit.pack(pady=80)

root.mainloop()