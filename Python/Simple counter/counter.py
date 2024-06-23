import tkinter as tk

class CounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Counter App")

        self.counter = 0
        self.dark_mode = False

        self.counter_label = tk.Label(master, text="Counter: 0", font=("Helvetica", 16))
        self.counter_label.pack(pady=20)

        self.increment_button = tk.Button(master, text="+", command=self.increment_counter)
        self.increment_button.pack(side=tk.LEFT, padx=10)

        self.decrement_button = tk.Button(master, text="-", command=self.decrement_counter)
        self.decrement_button.pack(side=tk.RIGHT, padx=10)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_counter)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.dark_mode_button = tk.Button(master, text="Dark Mode", command=self.toggle_dark_mode)
        self.dark_mode_button.pack(side=tk.RIGHT, padx=10)

    def update_counter_label(self):
        bg_color = "black" if self.dark_mode else "white"
        fg_color = "white" if self.dark_mode else "black"
        self.counter_label.config(text=f"Counter: {self.counter}", bg=bg_color, fg=fg_color)

    def increment_counter(self):
        self.counter += 1
        self.update_counter_label()

    def decrement_counter(self):
        self.counter -= 1
        self.update_counter_label()

    def reset_counter(self):
        self.counter = 0
        self.update_counter_label()

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self.master.configure(bg="black" if self.dark_mode else "white")
        self.update_counter_label()

def main():
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
