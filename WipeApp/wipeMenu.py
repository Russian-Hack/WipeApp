import tkinter
import customtkinter
from tkinter import ttk

root = tkinter.Tk()
style = ttk.Style
root.attributes("-fullscreen", True)
frame = ttk.Frame(root)
frame.configure(style="Custom.TFrame")
root.configure(bg="#010101")

my_tree = ttk.Treeview(frame)

my_tree['columns'] =("Name", "Size")
my_tree.column("#0", width=120)
my_tree.column("Name", width=20)
my_tree.column("Size", width=20)
my_tree.heading("#0", text="Label")
my_tree.heading("Name", text="Name")
my_tree.heading("Size", text="Size")
my_tree.pack(fill="both", expand=True, padx=300, pady=50)
quit = tkinter.Button(frame, text="Exit", command=root.quit, height=5, width=100, font=('Comfortaa', 14, 'bold'),
                      highlightthickness=0, borderwidth=0, fg="White", bg="#434d57")
quit.pack()



style = ttk.Style()
style.configure("Custom.TFrame", background="#708090")
frame.pack(fill="both", expand=True, padx=55, pady=55)
root.mainloop()
