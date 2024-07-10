import tkinter
import customtkinter
from tkinter import ttk


class wipeMenuClass:
    def __init__(self, master):
        self.master = master
        self.new_window = tkinter.Toplevel(master)

    def setup_gui(self):
        def quitter(event):
            self.new_window.withdraw()

        self.new_window.attributes('-fullscreen', True)
        self.new_window.configure(background="#010101")

        self.frame = ttk.Frame(self.new_window, style="Custom.TFrame")
        self.frame.pack(fill="both", expand=True, padx=55, pady=55)

        style = ttk.Style()
        style.configure("Custom.TFrame", background="#708090")
        self.my_tree = ttk.Treeview(self.frame)
        self.my_tree['columns'] = ("Name", "Size")
        self.my_tree.column("#0",width=5)
        self.my_tree.column("Size", width=500)
        self.my_tree.column("Name", width=500)
        self.my_tree.heading("#0", text="")
        self.my_tree.heading("Name", text="Name")
        self.my_tree.heading("Size", text="Size")
        self.my_tree.configure(height=1)
        self.my_tree.pack(fill="both", expand=True, padx=300, pady=80)


        self.new_window.bind("<Escape>", quitter)


