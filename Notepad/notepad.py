import tkinter as tk
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("600x400")

        self.text = tk.Text(root, wrap="word", undo=True)
        self.text.pack(expand=True, fill="both")

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)

        # Edit Menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text.edit_redo)

        # Format Menu
        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Choose Background Color", command=self.choose_bg_color)

        # Text Menu
        self.text_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Text", menu=self.text_menu)
        self.text_menu.add_command(label="Choose Font", command=self.choose_font)
        self.text_menu.add_command(label="Choose Font Style", command=self.choose_font_style)
        self.text_menu.add_command(label="Choose Font Size", command=self.choose_font_size)
        self.text_menu.add_command(label="Choose Font Color", command=self.choose_font_color)

    def new_file(self):
        self.text.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text.get("1.0", tk.END)
                file.write(content)

    def choose_bg_color(self):
        color_window = tk.Toplevel(self.root)
        color_window.title("Choose Background Color")

        colors = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Cyan", "Pink", "Brown", "White"]

        for color in colors:
            button = tk.Button(color_window, text=color, bg=color, command=lambda c=color: self.set_bg_color(c))
            button.pack(side="left", padx=5, pady=5)

    def set_bg_color(self, color):
        self.text.configure(bg=color)

    def choose_font(self):
        font_window = tk.Toplevel(self.root)
        font_window.title("Choose Font")

        fonts = ["Arial", "Times New Roman", "Courier New", "Verdana", "Helvetica", "Comic Sans MS"]

        for font_name in fonts:
            button = tk.Button(font_window, text=font_name, command=lambda f=font_name: self.set_font(f))
            button.pack(side="top", padx=5, pady=5)

    def set_font(self, font_name):
        self.text.configure(font=(font_name, self.text.cget("size"), self.text.cget("weight"), self.text.cget("slant")))

    def choose_font_style(self):
        style_window = tk.Toplevel(self.root)
        style_window.title("Choose Font Style")

        styles = ["normal", "italic", "bold"]

        for style in styles:
            button = tk.Button(style_window, text=style, command=lambda s=style: self.set_font_style(s))
            button.pack(side="top", padx=5, pady=5)

    def set_font_style(self, style):
        self.text.configure(font=(self.text.cget("family"), self.text.cget("size"), style, self.text.cget("slant")))

    def choose_font_size(self):
        size_window = tk.Toplevel(self.root)
        size_window.title("Choose Font Size")

        sizes = [8, 10, 12, 14, 16, 18, 20, 24, 28, 32]

        for size in sizes:
            button = tk.Button(size_window, text=str(size), command=lambda s=size: self.set_font_size(s))
            button.pack(side="top", padx=5, pady=5)

    def set_font_size(self, size):
        self.text.configure(font=(self.text.cget("family"), size, self.text.cget("weight"), self.text.cget("slant")))

    def choose_font_color(self):
        color = colorchooser.askcolor(title="Choose Font Color")
        if color[1]:
            self.text.configure(fg=color[1])

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
