import tkinter
import customtkinter
from tkinter import ttk

import psutil


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
        self.frame.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)
        for i in range(10):
            self.frame.grid_columnconfigure(i, weight=1)
            self.frame.grid_rowconfigure(i, weight=1)
        self.frame.pack(fill="both", expand=True, padx=55, pady=55)

        style = ttk.Style()
        style.configure("my_tree.heading", background="#708090")
        columns = ("Name", "Size")
        widths = {"#0": 0, "Name": 500, "Size": 500}

        headings = {"Name": "Name", "Size": "Size"}

        style.configure("Custom.TFrame", background="#708090")
        style.configure("Tree.TFrame", font=('Comfortaa', 14), rowheight=36, foreground="white", background="#434d57")
        style.map('Tree.TFrame', background=[('selected', "#647382")])

        self.my_tree = ttk.Treeview(self.frame, columns=columns, height=1, style='Tree.TFrame')

        for col, width in widths.items():
            self.my_tree.column(col, width=width)
        for col, heading in headings.items():
            self.my_tree.heading(col, text=heading)

        def on_enter_pressed(event):
            selected_item = self.my_tree.selection()[0]
            self.my_tree.tag_configure("selected", background="green")
            self.my_tree.item(selected_item, tags=("selected",))

        self.my_tree.grid(column=1, row=1, sticky="nsew", columnspan=4, rowspan=8, padx=(15, 15))
        self.my_tree.focus_set()

        self.acceptButton = tkinter.Button(self.frame, height=1, width=30
                                           , text="Confirm Wipe", command=confirm, font=('Comfortaa', 14, 'bold'),
                                           highlightthickness=0, borderwidth=0, fg="White", bg="#434d57")

        self.exitButton = tkinter.Button(self.frame, height=1, width=30
                                         , text="Exit", command=quittera, font=('Comfortaa', 14, 'bold'),
                                         highlightthickness=0, borderwidth=0, fg="White", bg="#434d57")
        self.acceptButton.grid(column=7, row=4, sticky="nsew", columnspan=1, rowspan=1, padx=(15, 15))
        self.exitButton.grid(column=7, row=8, sticky="nsew", columnspan=1, rowspan=1, padx=(15, 15))
        partitions = psutil.disk_partitions()
        self.master.bind("<Up>", lambda event: self.navigate_treeview(-1))
        self.master.bind("<Down>", lambda event: self.navigate_treeview(1))
        self.master.bind("<Return>", on_enter_pressed)

        def navigate_treeview(args):
            global i
            i = self.my_tree.selection()[0]
            print(i)

        for p in partitions:
            named = p.mountpoint
            sized = (psutil.disk_usage(p.mountpoint).total) / 1000000000

            sized_rounded = round(sized, 2)

            self.my_tree.insert("", "end", values=(named, f"{sized_rounded} GB"))
        self.my_tree.bind("<<TreeviewSelect>>", navigate_treeview)
        self.my_tree.focus()
