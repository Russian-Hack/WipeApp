import subprocess
import threading
import tkinter as tk
from tkinter import messagebox


class WipeLogic:
    def __init__(self, selected_drive):
        self.selected_drive = selected_drive

    def wipe_drive(self):
        threading.Thread(target=self._wipe_thread).start()

    def _wipe_thread(self):
        try:
            # Perform wiping operations here
            subprocess.run(['sudo', 'mfkf.exfat', self.selected_drive])
            subprocess.run(['sudo', 'cryptsetup', 'luksFormat', '--type', 'luks2', '--verify-passphrase', self.selected_drive])
            subprocess.run(['sudo', 'mkfs.exfat', '/dev/mapper/encrypted_drive'])
            subprocess.run(['sudo', 'cryptsetup', 'luksClose', 'encrypted_drive'])
            subprocess.run(['sudo', 'mkfs.exfat', self.selected_drive])

            # Show completion message
            messagebox.showinfo("Wipe Complete", f"Drive {self.selected_drive} has been securely wiped and reformatted in exFAT.")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")