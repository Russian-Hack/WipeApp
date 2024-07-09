import tkinter
import customtkinter
from tkinter import ttk


class wipeMenuClass:
    def __init__(self, master):
        self.master = master
        self.setup_gui()

    def setup_gui(self):
        def quitter(event):
         self.master.withdraw()

        self.master.attributes('-fullscreen', True)
        self.master.configure(background="#010101")

        self.frame = ttk.Frame(self.master, style="Custom.TFrame")
        self.frame.pack(fill="both", expand=True, padx=55, pady=55)

        style = ttk.Style()
        style.configure("Custom.TFrame", background="#708090")

        self.my_tree = ttk.Treeview(self.frame)
        self.my_tree['columns'] = ("Size")
        self.my_tree.column("#0", width=120)
        self.my_tree.column("Size", width=120)
        self.my_tree.heading("#0", text="Name")
        self.my_tree.heading("Size", text="Size")
        self.my_tree.configure(height=1)
        self.my_tree.pack(fill="both", expand=True, padx=300, pady=80)

        self.master.bind("<Escape>", quitter)


# Main script logic
if __name__ == "__main__":
    root = tkinter.Tk()
    app = wipeMenuClass(root)