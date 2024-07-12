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

        def quittera():
            self.new_window.withdraw()

        def confirm():
            print("confirm")

        self.new_window.attributes('-fullscreen', True)
        self.new_window.configure(background="#010101")

        self.frame = ttk.Frame(self.new_window, style="Custom.TFrame")
        self.frame.pack(fill="both", expand=True, padx=55, pady=55)

        style = ttk.Style()
        columns = ("Name", "Size")
        widths = {"#0": 5, "Name": 500, "Size": 500}
        headings = {"#0": "", "Name": "Name", "Size": "Size"}
        style.configure("Custom.TFrame", background="#708090")
        style.configure("Tree.TFrame", font=('Comfortaa', 20, 'bold'))
        self.my_tree = ttk.Treeview(self.frame, columns=columns, height=1, style='Tree.TFrame')

        for col, width in widths.items():
            self.my_tree.column(col, width=width)
        for col, heading in headings.items():
            self.my_tree.heading(col, text=heading)
        self.my_tree.pack(fill="both", expand=True, padx=(100, 500), pady=80)
        self.my_tree.focus_set()

        self.acceptButton = tkinter.Button(self.frame, height=2, width=30
                                           , text="Confirm Wipe", command=confirm, font=('Comfortaa', 14, 'bold'),
                                           highlightthickness=0, borderwidth=0, fg="White", bg="#434d57")

        self.exitButton = tkinter.Button(self.frame, height=2, width=30
                                         , text="Exit", command=quittera, font=('Comfortaa', 14, 'bold'),
                                         highlightthickness=0, borderwidth=0, fg="White", bg="#434d57")
        self.acceptButton.place(x=1400, y=440)
        self.exitButton.place(x=1400, y=835)
        self.new_window.bind("<Escape>", quitter)
