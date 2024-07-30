# This is a sample Python script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import subprocess

import tkinter


from tkinter import ttk
from wipeMenu import wipeMenuClass



base = tkinter.Tk()
def reboot():
    try:
        subprocess.run(['sudo', 'reboot'], check=True)  # Run the reboot command
    except subprocess.CalledProcessError as e:
        print(f"Error trying to reboot: {e}")
        tkinter.messagebox.showerror("Error", f"Failed to reboot the system: {str(e)}")

# Prints the first mac address the computer has
# def print_first_mac_address():
#     try:
#         output = subprocess.check_output(['ifconfig']).decode('utf-8')
#         lines = output.split('\n')
#         is_up = False
#         for line in lines:
#             if 'flags=' in line:  # Check for the line with interface flags
#                 # Check if the interface is UP and RUNNING
#                 if 'UP' in line and 'RUNNING' in line:
#                     is_up = True
#                 else:
#                     is_up = False  # Reset for the next interface
#
#             if is_up and 'ether' in line:  # Look for the line containing 'ether' when UP
#                 parts = line.strip().split()
#                 mac_address_index = parts.index('ether') + 1
#                 return parts[mac_address_index].upper()  # Return the MAC address found in uppercase
#     except subprocess.CalledProcessError as e:
#         print(f"Error running ifconfig: {e}")
#     return "00-00-00-00-00-00"


# Navigates up between the wipe menu and the exit button
def navigate_up(event):
    if event.keysym == "Up":

        thing = base.focus_get()

        if thing == quit:
            wipe.focus()
            wipe.configure(bg="#2D333A")
            quit.configure(bg="#434d57")


# Navigates down between the wipe menu and the exit button
def navigate_down(event):
    if event.keysym == "Down":
        print("hi")
        thing = base.focus_get()
        if thing == wipe:
            quit.focus()
            quit.configure(bg="#2D333A")
            wipe.configure(bg="#434d57")


# Action that happens when you press enter
def activate_button(event):
    current_focus = base.focus_get()
    if (current_focus == wipe):
        wipe_clicker()

    elif (current_focus == quit):
        reboot()


# Focuses back on the wipe button in a callback, so the wipe and exit buttons work when you exit the WipeMenu
def focus_on_wipe_button():
    wipe.focus
    base.bind("<Up>", navigate_up)
    base.bind("<Down>", navigate_down)
    base.bind("<Return>", activate_button)


# Opens the WipeMenu
def wipe_clicker():
    wipe_menu = wipeMenuClass(base, callback=focus_on_wipe_button)
    wipe_menu.setup_gui()


# Creates custom buttons (made for easier readability of code)
def create_button(parent, text, command, height=5, width=50, font=('Comfortaa', 14, 'bold'), highlightthickness=0,
                  borderwidth=0, fg="White", takefocus=False, bg="#434d57"):
    return tkinter.Button(
        parent,
        text=text,
        command=command,
        height=height,
        width=width,
        font=font,
        highlightthickness=highlightthickness,
        borderwidth=borderwidth,
        fg=fg,
        takefocus=takefocus,
        bg=bg
    )

base.attributes("-fullscreen", True)
base.configure(bg="#010101")
style = ttk.Style()
frame = ttk.Frame(base)
frame.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)
for i in range(10):  # 5 columns
    frame.grid_columnconfigure(i, weight=1)
for j in range(5):  # 5 rows
    frame.grid_rowconfigure(j, weight=1)
base.grid_rowconfigure(0, weight=1)
frame.configure(style="Custom.TFrame")
style.configure("Custom.TFrame", background="#708090")
frame.pack(fill="both", expand=True, pady=55, padx=55)
base.bind("<Up>", navigate_up)
base.bind("<Down>", navigate_down)
base.bind("<Return>", activate_button)
wipe = create_button(frame, text="Wipe", command=wipe_clicker)
wipe.grid(column=3, row=1, sticky="nsew", pady=(0, 0),columnspan=4)
quit = create_button(frame, text="Quit", command=reboot)
quit.grid(column=3, row=3, sticky="nsew", pady=(0, 50), columnspan=4)

quit.focus()
quit.configure(bg="#2D333A")

try:
    base.mainloop()
except KeyboardInterrupt:
    print("Keyboard Interrupt")
