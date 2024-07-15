import tkinter
import customtkinter
from tkinter import ttk

import psutil

from dialogBox import CustomConfirmation


class wipeMenuClass:
    def __init__(self, master, callback=None):
        self.master = master
        self.new_window = tkinter.Toplevel(master)
        self.callback = callback

    def unbind_keys(self):
        self.master.unbind("<Up>")
        self.master.unbind("<Down>")
        self.master.unbind("<Return>")
        self.master.unbind("<Escape>")

    def setup_gui(self):

        def quittera():
            print("hi")
            self.new_window.withdraw()
            self.new_window.focus()
            self.unbind_keys()
            if self.callback:
                self.callback()

        def on_enter_pressed(event):
            print("hhi")
            selected_item = self.my_tree.selection()[0]
            self.my_tree.tag_configure("selected", background="green")
            self.my_tree.item(selected_item, tags=("selected",))
            show_confirm_popup()


        def navigate_up(event):
            current_index = self.my_tree.index(self.my_tree.selection())
            if current_index > 0:
                self.my_tree.selection_set(self.my_tree.get_children()[current_index - 1])

        def show_confirm_popup():
            selected_item = self.my_tree.selection()[0]
            confirm_message = f"Are you sure you want to wipe {selected_item}?"

            # Define the callback function for confirm action
            def confirm_action():
                wipe_selected_item()
            self.new_window.deiconify()  # Show the main window again
            self.new_window.focus_set()
            self.my_tree.focus_set()
            self.my_tree.selection_set(self.my_tree.get_children()[0])
            bind_keys(self)


        # Optionally add more logic after confirmation

            # Create an instance of CustomConfirmation
            confirm_popup = CustomConfirmation(self.new_window, confirm_message, confirm_action, lambda: None)

        def wipe_selected_item():
            selected_item = self.my_tree.selection()[0]
            print(f"Wiping {selected_item}")

        def navigate_down(event):
            current_index = self.my_tree.index(self.my_tree.selection())
            if current_index < len(self.my_tree.get_children()) - 1:
                self.my_tree.selection_set(self.my_tree.get_children()[current_index + 1])
        def bind_keys(self):
            self.master.bind("<Up>", navigate_up)
            self.master.bind("<Down>", navigate_down)
            self.master.bind("<Return>", on_enter_pressed)
            self.master.bind("<Escape>", lambda event: quittera())

        self.master.bind("<Up>", navigate_up)
        self.master.bind("<Down>", navigate_down)
        self.master.bind("<Return>", on_enter_pressed)
        self.master.bind("<Escape>", lambda event: quittera())

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

        self.my_tree.grid(column=1, row=1, sticky="nsew", columnspan=8, rowspan=8, padx=(15, 15))

        partitions = psutil.disk_partitions()

        for p in partitions:
            named = p.mountpoint
            sized = (psutil.disk_usage(p.mountpoint).total) / 1000000000

            sized_rounded = round(sized, 2)

            self.my_tree.insert("", "end", values=(named, f"{sized_rounded} GB"))
        self.my_tree.bind("<<TreeviewSelect>>", lambda event: print(event))
        self.my_tree.selection_set(self.my_tree.get_children()[0])

        print(self.frame.focus_get())
