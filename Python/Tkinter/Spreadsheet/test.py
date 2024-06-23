import tkinter as tk
from tkinter import Tk, Entry, mainloop, StringVar, Canvas, Scrollbar

height = 25
width = 25
root = Tk()

def file_command():
    print("File command")

# Other command functions...

def create_window():
    global root
    root.title("Excel-like Table")
    root.geometry("800x600")
    root.resizable(True, True)

    canvas = Canvas(root)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

    scroll_x = Scrollbar(root, orient="horizontal", command=canvas.xview)
    scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

    canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # Define your menus and commands...

    labels = []
    for i in range(height + 1):
        for j in range(width + 1):
            if i == 0:
                label_text = chr(65 + j) if j > 0 else ""
            elif j == 0:
                label_text = str(i) if i > 0 else ""
            else:
                label_text = ""
            label = tk.Label(frame, text=label_text)
            label.grid(row=i, column=j)
            labels.append(label)

    text_vars = []
    for i in range(height):
        row_vars = []
        for j in range(width):
            text_var = StringVar()
            entry = Entry(frame, textvariable=text_var)
            entry.grid(row=i + 1, column=j + 1)
            row_vars.append(text_var)
        text_vars.append(row_vars)  

    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

create_window()

root.mainloop()
