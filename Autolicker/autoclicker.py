import tkinter as tk
from tkinter import messagebox
import pyautogui
import keyboard
import threading
import time

class AutoClicker:
    def __init__(self, master):
        self.master = master
        self.master.title("Auto Clicker")
        
        self.keybind = tk.StringVar()
        self.interval = tk.DoubleVar()

        tk.Label(master, text="Keybind:").grid(row=0, column=0)
        tk.Entry(master, textvariable=self.keybind).grid(row=0, column=1)

        tk.Label(master, text="Click Interval (seconds):").grid(row=1, column=0)
        tk.Entry(master, textvariable=self.interval).grid(row=1, column=1)

        self.start_button = tk.Button(master, text="Set Keybind", command=self.set_keybind)
        self.start_button.grid(row=2, column=0, columnspan=2)

        self.stop_button = tk.Button(master, text="Exit", command=self.exit_clicker)
        self.stop_button.grid(row=3, column=0, columnspan=2)

        self.running = False

    def set_keybind(self):
        try:
            self.key = self.keybind.get()
            self.click_interval = self.interval.get()

            if not self.key or not self.click_interval:
                raise ValueError("Please enter a valid keybind and interval.")

            keyboard.add_hotkey(self.key, self.toggle_clicking)
            messagebox.showinfo("Info", f"Keybind '{self.key}' set. Press it to start/stop clicking.")
            self.start_button.config(state=tk.DISABLED)
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def exit_clicker(self):
        self.running = False
        self.master.destroy()

    def toggle_clicking(self):
        if self.running:
            self.running = False
        else:
            self.running = True
            self.thread = threading.Thread(target=self.run_clicker)
            self.thread.start()

    def run_clicker(self):
        while self.running:
            pyautogui.click()
            time.sleep(self.click_interval)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClicker(root)
    root.mainloop()
