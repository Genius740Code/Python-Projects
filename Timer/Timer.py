import tkinter as tk
from tkinter import messagebox
import time
import winsound

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")
        
        self.label = tk.Label(root, text="Enter time in seconds:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, width=10)
        self.entry.pack(pady=5)
        
        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack(pady=10)
        
        self.timer_running = False
        self.end_time = 0
        
    def start_timer(self):
        if not self.timer_running:
            try:
                time_seconds = int(self.entry.get())
                if time_seconds <= 0:
                    messagebox.showerror("Error", "Please enter a positive integer greater than zero.")
                    return
                
                self.end_time = time.time() + time_seconds
                self.timer_running = True
                self.update_timer()
                
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid integer.")
    
    def update_timer(self):
        if self.timer_running:
            remaining_time = self.end_time - time.time()
            if remaining_time <= 0:
                self.timer_running = False
                self.end_timer()
                return
            
            minutes, seconds = divmod(remaining_time, 60)
            time_str = f"{int(minutes):02}:{int(seconds):02}"
            self.label.configure(text=time_str)
            self.root.after(100, self.update_timer)
    
    def end_timer(self):
        winsound.Beep(1000, 1000)  # Beep sound for 1 second
        messagebox.showinfo("Timer Finished", "Timer has finished!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
