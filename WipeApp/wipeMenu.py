import tkinter
import customtkinter
from tkinter import ttk

import psutil


class wipeMenuClass:
    def __init__(self, master):
        self.master = master
        self.new_window = tkinter.Toplevel(master)

    def setup_gui(self):

        def quittera():
            print("hi")
            self.new_window.focus()
            self.new_window.withdraw()


        def confirm():
            print("confirm")
        def on_enter_pressed(event):
            selected_item = self.my_tree.selection()[0]
            self.my_tree.tag_configure("selected", background="green")
            self.my_tree.item(selected_item, tags=("selected",))

        def navigate_up(event):
            current_index = self.my_tree.index(self.my_tree.selection())
            if current_index > 0:
                self.my_tree.selection_set(self.my_tree.get_children()[current_index - 1])

        def navigate_down(event):
            current_index = self.my_tree.index(self.my_tree.selection())
            if current_index < len(self.my_tree.get_children()) - 1:
                self.my_tree.selection_set(self.my_tree.get_children()[current_index + 1])
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
            print("hhi")
            selected_item = self.my_tree.selection()[0]
            self.my_tree.tag_configure("selected", background="green")
            self.my_tree.item(selected_item, tags=("selected",))

        self.my_tree.grid(column=1, row=1, sticky="nsew", columnspan=8, rowspan=8, padx=(15, 15))
        

        partitions = psutil.disk_partitions()
        self.master.bind("<Up>", navigate_up)
        self.master.bind("<Down>", navigate_down)
        self.master.bind("<Return>", on_enter_pressed)
        self.new_window.bind("<Escape>", lambda event : quittera())



        for p in partitions:
            named = p.mountpoint
            sized = (psutil.disk_usage(p.mountpoint).total) / 1000000000

            sized_rounded = round(sized, 2)

            self.my_tree.insert("", "end", values=(named, f"{sized_rounded} GB"))
        self.my_tree.bind("<<TreeviewSelect>>", lambda event: print(event))
        self.my_tree.selection_set(self.my_tree.get_children()[0])

        print(self.frame.focus_get())
