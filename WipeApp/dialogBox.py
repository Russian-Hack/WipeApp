import tkinter as tk
from tkinter import ttk

class CustomConfirmation:
    def __init__(self, master, message, callback_confirm, callback_cancel):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.geometry('500x400')
        self.frame = ttk.Frame(self.top, style="Custom.TFrame")

        style = ttk.Style()
        style.configure("Custom.TFrame", background="#708090")

        self.frame.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)
        for i in range(3):
            self.frame.grid_columnconfigure(i, weight=1)
            self.frame.grid_rowconfigure(i, weight=1)
        self.top.configure(bg="#101010")
        self.message = message
        self.callback_confirm = callback_confirm
        self.callback_cancel = callback_cancel

        self.label = ttk.Label(self.frame, text=message)
        self.label.grid(column=1, row=0, sticky="nsew", padx=10, pady=10)

        self.button_confirm = tk.Button(self.frame, text="Confirm", command=self.confirm,
                                        font=('Comfortaa', 14, 'bold'),
                                        highlightthickness=0, borderwidth=0, fg="White", bg="#434d57")
        self.button_confirm.grid(column=1, row=1, sticky="nsew", padx=10, pady=10)

        self.button_cancel = tk.Button(self.frame, text="Cancel", command=self.cancel,
                                       font=('Comfortaa', 14, 'bold'),
                                       highlightthickness=0, borderwidth=0, fg="White", bg="#434d57")
        self.button_cancel.grid(column=1, row=2, sticky="nsew", padx=10, pady=10)

        self.top.bind("<Up>", self.navigate_up)
        self.top.bind("<Down>", self.navigate_down)
        self.top.bind("<Enter>", self.activate_button)

        self.frame.pack(fill="both", expand=True, padx=15, pady=15)
        self.button_cancel.focus_set()  # Set initial focus to Cancel button
        self.button_cancel.configure(bg="#2D333A")
    def navigate_up(self, event):
        thing = self.top.focus_get()
        if thing == self.button_cancel:
            self.button_confirm.focus_set()
            self.button_confirm.configure(bg="#2D333A")
            self.button_cancel.configure(bg="#434d57")

    def navigate_down(self, event):
        thing = self.top.focus_get()
        if thing == self.button_confirm:
            self.button_cancel.focus_set()
            self.button_cancel.configure(bg="#2D333A")
            self.button_confirm.configure(bg="#434d57")



    def confirm(self):
        print("down")
        self.top.destroy()
        if self.callback_confirm:
            self.callback_confirm()


    def cancel(self):
        print("up")
        self.top.destroy()
        if self.callback_cancel:
            self.callback_cancel()


    def activate_button(self, event):
        current_focus = self.top.focus_get()
        print(current_focus)
        if current_focus == self.button_confirm:
            self.confirm()
        elif current_focus == self.button_cancel:
            self.cancel()
