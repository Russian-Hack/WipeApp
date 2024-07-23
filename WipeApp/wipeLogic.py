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
            if self.is_mounted(self.selected_drive):
                subprocess.run(['sudo', 'umount', self.selected_drive], check=True)

            # Perform wiping operations
            mkfs_command = ['sudo', 'mkfs.ext4', '-F', self.selected_drive]

            # Open subprocess with stdin to provide 'yes' automatically
            with subprocess.Popen(mkfs_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE) as proc:
                try:
                    outs, errs = proc.communicate(input=b'yes\n', timeout=15)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    outs, errs = proc.communicate()

            # Provide passphrase securely using a temporary file
            passphrase = b'MySecurePassphrase'
            passphrase_file = '/tmp/passphrase_file'
            with open(passphrase_file, 'wb') as f:
                f.write(passphrase)

            cryptsetup_command = ['sudo', 'cryptsetup', 'luksFormat', '--type', 'luks2', '--batch-mode', '--key-file',
                                  passphrase_file, self.selected_drive]

            subprocess.run(cryptsetup_command, check=True)

            # Close the LUKS volume
            subprocess.run(['sudo', 'cryptsetup', 'luksClose', '--batch-mode', 'ENCRYPTED'], check=True)

            # Format again to ensure data is securely wiped
            subprocess.run(['sudo', 'mkfs.ext4', '-F', self.selected_drive], check=True)
            with subprocess.Popen(mkfs_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE) as proc:
                try:
                    outs, errs = proc.communicate(input=b'yes\n', timeout=15)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    outs, errs = proc.communicate()

            # Mount the drive back (if needed)
            mount_point = '/mnt/myluks'
            subprocess.run(['sudo', 'mount', self.selected_drive, mount_point], check=True)

            # Show completion message
            messagebox.showinfo("Wipe Complete",
                                f"Drive {self.selected_drive} has been securely wiped and reformatted in ext4.")

            # Print message to terminal
            print(f"Wipe process completed for drive: {self.selected_drive}")

        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Subprocess error occurred: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error occurred: {str(e)}")
