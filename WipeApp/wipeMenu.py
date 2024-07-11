import tkinter
from tkinter import ttk


import psutil





class wipeMenuClass:
    def __init__(self, master):
        self.master = master
        self.new_window = tkinter.Toplevel(master)

    def setup_gui(self):
        def quittera():
        # Destroy all widgets in the frame
            self.master.focus_set()
            self.master.unbind("<Up>")
            self.master.unbind("<Down>")
            self.master.unbind("<Return>")
            self.master.unbind("<Left>")
            self.master.unbind("<Right>")
            self.my_tree.unbind("<Up>")
            self.my_tree.unbind("<Down>")
            self.my_tree.unbind("<Return>")
            self.my_tree.unbind("<Left>")
            self.my_tree.unbind("<Right>")

            for widget in self.frame.winfo_children():
             widget.destroy()
            self.new_window.destroy()




        def confirm():
            print("confirm")

        def focus_exit_button(event):
            self.exitButton.focus()

        def focus_last_item(event):
            last_item = self.my_tree.get_children()[-1]
            self.my_tree.focus_set()
            self.my_tree.selection_set(last_item)

        def on_enter_pressed(event):
            selected_item = self.my_tree.selection()[0]
            self.my_tree.tag_configure("selected", background="green")
            self.my_tree.item(selected_item, tags=("selected",))
            print(f"Enter pressed on item: {selected_item}")

        self.new_window.attributes('-fullscreen', True)
        self.new_window.configure(background="#010101")

        self.frame = ttk.Frame(self.new_window, style="Custom.TFrame")
        self.frame.pack(fill="both", expand=True, padx=55, pady=55)

        style = ttk.Style()
        columns = ("Name", "Size")

        widths = {"#0": 5, "Name": 500, "Size": 500}
        headings = {"#0": "", "Name": "Name", "Size": "Size"}

        widths = {"#0": 0, "Name": 500, "Size": 500}
        headings = {"Name": "Name", "Size": "Size"}

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
        self.new_window.bind("<Escape>", quittera)


        self.my_tree.grid(column=1, row=1, sticky="nsew", columnspan=4, rowspan=8, padx=(15, 15))
        self.my_tree.focus_set()

        self.acceptButton = tkinter.Button(self.frame, height=1, width=30,
                                           text="Confirm Wipe", command=confirm, font=('Comfortaa', 14, 'bold'),
                                           highlightthickness=0, borderwidth=0, fg="White", bg="#434d57")

        self.exitButton = tkinter.Button(self.frame, height=1, width=30,
                                         text="Exit", command=quittera, font=('Comfortaa', 14, 'bold'),
                                         highlightthickness=0, borderwidth=0, fg="White", bg="#434d57")

        self.acceptButton.grid(column=7, row=4, sticky="nsew", columnspan=1, rowspan=1, padx=(15, 15))
        self.exitButton.grid(column=7, row=8, sticky="nsew", columnspan=1, rowspan=1, padx=(15, 15))

        partitions = psutil.disk_partitions()

        for p in partitions:
            named = p.mountpoint
            sized = (psutil.disk_usage(p.mountpoint).total) / 1000000000
            sized_rounded = round(sized, 2)
            self.my_tree.insert("", "end", values=(named, f"{sized_rounded} GB"))

        self.master.bind("<Up>", lambda event: self.navigate_treeview(-1))
        self.master.bind("<Down>", lambda event: self.navigate_treeview(1))
        self.master.bind("<Return>", on_enter_pressed)
        self.master.bind("<Left>", focus_exit_button)
        self.master.bind("<Right>", focus_last_item)

        def navigate_treeview(args):
            selected_item = self.my_tree.selection()[0]
            print(selected_item)

        self.my_tree.bind("<<TreeviewSelect>>", navigate_treeview)
        self.my_tree.focus()


