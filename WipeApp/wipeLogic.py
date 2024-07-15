import os
import subprocess
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class WipeLogic:
    def __init__(self, selected_drive, size):
        self.selected_drive = selected_drive
        self.progress_window = None
        self.progress_bar = None
    def wipe_drive(self):
        drive_size = self.size
        self.progress_window=tk.Toplevel()
        self.progress_window.title("Wiping")
        self.progress_bar = ttk.Progressbar(self.progress_window, orient = "horizontal", lenght = 300, mode = 'indeterminate')
        self.progress_bar.pack(side = "right", pady=20)
        self.progress_bar.start()

        threading.Thread(target=self.wipe_thread).start()

    def _wipe_thread(self):
        try:
            subprocess.run(['sudo', 'mfkf.exfat', self.selected_drive])
            subprocess.run(['sudo', 'cryptsetup', 'luksFormat', '--type', 'luks2', '--verify-passphrase', self.selected_drive])
            subprocess.run(['sudo', 'mkfs.exfat', '/dev/mapper/encrypted_drive'])
            subprocess.run(['sudo', 'cryptsetup', 'luksClose', 'encrypted_drive'])
            subprocess.run(['sudo', 'mkfs.exfat', self.selected_drive])
            messagebox.showinfo("Wipe Complete", f"Drive {self.selected_drive} has been securely wiped and reformatted in exFAT.")
        except Exception as e:
            messagebox.showerror("Error", f"Error occured: {str(e)}")
        self.progress_bar.stop()
        self.progress_window.destroy()
