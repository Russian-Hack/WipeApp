import subprocess
import threading
from tkinter import messagebox, Toplevel, Label, Button
import os

class WipeLogic:
    def __init__(self, selected_drive):
        self.selected_drive = selected_drive
        self.wipe_in_progress = False
        self.passphrase = b'MySecurePassphrase'

    def wipe_drive(self):
        self.wipe_in_progress = True
        threading.Thread(target=self._wipe_thread).start()
        self.show_progress_dialog()

    def show_progress_dialog(self):
        self.progress_window = Toplevel()
        self.progress_window.title("Wiping Drive")
        dialog_width = 300
        dialog_height = 100
        screen_width = self.progress_window.winfo_screenwidth()
        screen_height = self.progress_window.winfo_screenheight()
        x = (screen_width // 2) - (dialog_width // 2)
        y = (screen_height // 2) - (dialog_height // 2)
        self.progress_window.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")
        self.progress_label = Label(self.progress_window, text="Wiping in progress...")
        self.progress_label.pack(pady=20)
        cancel_button = Button(self.progress_window, text="Cancel", command=self.cancel_wipe)
        cancel_button.pack(pady=10)
        self.progress_window.after(100, self.check_wipe_status)

    def check_wipe_status(self):
        if self.wipe_in_progress:
            self.progress_window.after(100, self.check_wipe_status)
        else:
            self.progress_window.destroy()

    def cancel_wipe(self):
        self.wipe_in_progress = False
        messagebox.showinfo("Canceled", "Wipe operation has been canceled.")
        self.progress_window.destroy()

    @staticmethod
    def is_mounted(device):
        try:
            subprocess.run(['mountpoint', '-q', device], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def _wipe_thread(self):
        try:
            if self.is_mounted(self.selected_drive):
                subprocess.run(['sudo', 'umount', '-lf', self.selected_drive], check=True)

            subprocess.run(['sudo', 'mkfs.ext4', '-F', self.selected_drive], check=True)

            passphrase_file = '/tmp/passphrase_file'
            with open(passphrase_file, 'wb') as f:
                f.write(self.passphrase)

            subprocess.run(['sudo', 'mkdir', '-p', '/mnt/MYLUKS'], check=True)

            subprocess.run([
                'sudo', 'cryptsetup', 'luksFormat', '--type', 'luks2',
                '--batch-mode', '--key-file', passphrase_file,
                '--label', 'MYLUKS', self.selected_drive
            ], check=True)

            subprocess.run(['sudo', 'cryptsetup', 'luksOpen',
                            '--key-file', passphrase_file,
                            self.selected_drive, 'MYLUKS'], check=True)

            subprocess.run(['sudo', 'dd', 'if=/dev/zero',
                            'of=/dev/mapper/MYLUKS',
                            'bs=4M', 'status=progress'], check=True)

            subprocess.run(['sudo', 'cryptsetup', 'luksClose', 'MYLUKS'], check=True)

            os.remove(passphrase_file)

            messagebox.showinfo("Wipe Complete",
                                f"Drive {self.selected_drive} has been securely wiped.")
            print(f"Wipe process completed for drive: {self.selected_drive}")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.wipe_in_progress = False
        finally:
            self.wipe_in_progress = False
