import subprocess
import tkinter
from tkinter import ttk

import psutil
from wipeLogic import WipeLogic
from dialogBox import CustomConfirmation


class wipeMenuClass:
    def __init__(self, master, callback=None):
        self.master = master
        self.new_window = tkinter.Toplevel(master)
        self.callback = callback
    #Unbinds all the key from the WipeMenu on exit
    def unbind_keys(self):
        self.master.unbind("<Up>")
        self.master.unbind("<Down>")
        self.master.unbind("<Return>")
        self.master.unbind("<Escape>")
    #Sets up the interface and the other functions of the menu
    def setup_gui(self):
        #Closes the wipeMenu
        def quittera():
            print("hi")
            self.new_window.withdraw()
            self.new_window.focus()
            self.unbind_keys()
            if self.callback:
                self.callback()
        #Creates an action for when you choose a drive. It creates a confirm popup
        def on_enter_pressed(event):
            selected_item = self.my_tree.selection()[0]
            selected_drive = self.my_tree.item(selected_item)['values'][0]  # Assuming first column is device path
            self.my_tree.item(selected_item, tags=("selected",))
            show_confirm_popup(selected_drive)
        #To navigate up between drives
        def navigate_up(event):
            current_index = self.my_tree.index(self.my_tree.selection())
            if current_index > 0:
                self.my_tree.selection_set(self.my_tree.get_children()[current_index - 1])
        #The confirm popup
        def show_confirm_popup(selected_drive):
            confirm_message = f"Are you sure you want to wipe {selected_drive}?"
            #What happens when you press confirm in the popup (starts the wipe)
            def confirm_action():
                wipe_selected_item(selected_drive)
                self.new_window.deiconify()
                self.new_window.focus_set()
                bind_keys(self)
                self.my_tree.focus_set()
                self.my_tree.selection_set(self.my_tree.get_children()[0])
            #Closes the popup menu without performing any other action
            def cancel_action():
                self.new_window.deiconify()
                self.new_window.focus_set()
                bind_keys(self)
                self.my_tree.focus_set()
                self.my_tree.selection_set(self.my_tree.get_children()[0])



            #confirm_popup = CustomConfirmation(self.new_window, confirm_message, confirm_action, cancel_action)
        
        def wipe_selected_item(selected_drive):
            wiper = WipeLogic(selected_drive)
            wiper.wipe_drive()
            print(f"Wiping {selected_drive}")

        def navigate_down(event):
            current_index = self.my_tree.index(self.my_tree.selection())
            if current_index < len(self.my_tree.get_children()) - 1:
                self.my_tree.selection_set(self.my_tree.get_children()[current_index + 1])

        def bind_keys(self):
            self.my_tree.bind("<Up>", navigate_up)
            self.my_tree.bind("<Down>", navigate_down)
            self.my_tree.bind("<Return>", on_enter_pressed)
            self.my_tree.bind("<Escape>", lambda event: quittera())

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
        self.my_tree.bind("<Up>", navigate_up)
        self.my_tree.bind("<Down>", navigate_down)
        self.my_tree.bind("<Return>", on_enter_pressed)
        self.my_tree.bind("<Escape>", lambda event: quittera())
        try:
            # Example using lsblk to list all block devices, adjust filtering as needed
            lsblk_output = subprocess.check_output(['lsblk', '-o', 'NAME,SIZE', '-n', '-l', '-p']).decode(
                'utf-8').strip()
            devices_info = lsblk_output.split('\n')

            for device_info in devices_info:
                fields = device_info.split()
                if len(fields) >= 2:
                    device_name = fields[0]
                    device_size = fields[1]
                    # Example filter: include only devices starting with /dev/sd, /dev/nvme, or /dev/disk/by-id/usb
                    if device_name.startswith('/dev/sd') or device_name.startswith(
                            '/dev/nvme') or '/dev/disk/by-id/usb' in device_name:
                        self.my_tree.insert("", "end", values=(device_name, device_size))

        except subprocess.CalledProcessError as e:
            print(f"Error executing lsblk command: {e}")
        except Exception as e:
            print(f"Unexpected error retrieving device information: {e}")

        self.my_tree.selection_set(self.my_tree.get_children()[0])

        self.my_tree.bind("<<TreeviewSelect>>", lambda event: print(event))
        self.my_tree.selection_set(self.my_tree.get_children()[0])

        print(self.frame.focus_get())
