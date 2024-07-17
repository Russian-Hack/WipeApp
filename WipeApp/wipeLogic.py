import subprocess
import threading
import tkinter as tk
from tkinter import messagebox


class WipeLogic:
    def __init__(self, selected_drive):
        self.selected_drive = selected_drive

    def wipe_drive(self):
        threading.Thread(target=self._wipe_thread).start()

    @staticmethod
    def is_mounted(device):
        try:
            subprocess.run(['mountpoint', '-q', device], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def _wipe_thread(self):
        try:

            # Attempt to unmount the device
            subprocess.run(['sudo', 'umount', self.selected_drive], check=True)

            # Perform wiping operations
            subprocess.run(['sudo', 'mkfs.ext4', '-F', self.selected_drive], check=True, input=b'YES\n')
            subprocess.run(
                ['sudo', 'cryptsetup', 'luksFormat', '--type', 'luks2', '--verify-passphrase', self.selected_drive],
                check=True)
            subprocess.run(['sudo', 'cryptsetup', 'luksClose', self.selected_drive], check=True)
            subprocess.run(['sudo', 'mkfs.ext4', '-F', self.selected_drive], check=True, input=b'YES\n')

            # Show completion message
            messagebox.showinfo("Wipe Complete",
                                f"Drive {self.selected_drive} has been securely wiped and reformatted in ext4.")

            # Print message to terminal
            print(f"Wipe process completed for drive: {self.selected_drive}")

        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Subprocess error occurred: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error occurred: {str(e)}")
