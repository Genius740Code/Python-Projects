import tkinter as tk
from tkinter import Tk, Entry, mainloop, StringVar, Canvas, Scrollbar, font

height = 25
width = 25
root = Tk()

def file_command():
    print("File command")

def edit_command():
    print("Edit command")

def view_command():
    print("View command")

def fullscreen_command(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))
    root.bind("<F11>", fullscreen_command)

def insert_command():
    print("Insert command")

def format_command():
    print("Format command")

def light_theme_command():
    print("Light theme command")
    root.configure(bg="lightblue")

def dark_theme_command():
    print("Light theme command")
    root.configure(bg="gray8")

def blue_theme_command():
    print("Light theme command")
    root.configure(bg="mediumblue")

def chart_command():
    print("Chart command")

def new_file_command(event=None):
    create_window()  
    root.bind('<Control-n>', new_file_command)

def cosmic_sans_format_command():
    Font_tuple = ("Comic Sans MS", 20, "bold") 

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

    file_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file_command)  
    file_menu.add_command(label="Save", command=file_command)
    file_menu.add_command(label="Open", command=file_command)
    file_menu.add_command(label="Import", command=file_command)
    file_menu.add_command(label="Make a copy", command=file_command)
    file_menu.add_separator()
    file_menu.add_command(label="Share", command=file_command)
    file_menu.add_command(label="Download", command=file_command)
    file_menu.add_command(label="Rename", command=file_command)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
   
    edit_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut", command=edit_command)
    edit_menu.add_command(label="Copy", command=edit_command)
    edit_menu.add_command(label="Paste", command=edit_command)
    edit_menu.add_separator()
    edit_menu.add_command(label="Undo", command=edit_command)
    edit_menu.add_command(label="Redo", command=edit_command)
    edit_menu.add_separator()
    edit_menu.add_command(label="Find", command=edit_command)

    view_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label="View", menu=view_menu)
    view_menu.add_command(label="Zoom In", command=view_command)
    view_menu.add_command(label="Zoom Out", command=view_command)
    view_menu.add_command(label="Full Screen", command=fullscreen_command)

    insert_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label="Insert", menu=insert_menu)
    insert_menu.add_command(label="Cells", command=insert_command)
    insert_menu.add_command(label="Rows", command=insert_command)
    insert_menu.add_command(label="Columns", command=insert_command)

    chart_submenu = tk.Menu(insert_menu, tearoff=False)
    insert_menu.add_cascade(label="Charts", menu=chart_submenu)
    chart_submenu.add_command(label="Bar charts", command=insert_command)
    chart_submenu.add_command(label="Line Chart", command=insert_command)
    chart_submenu.add_command(label="Scatter Plot", command=insert_command)
    chart_submenu.add_command(label="Pie Chart", command=chart_command)

    insert_menu.add_separator()
    insert_menu.add_command(label="Images", command=insert_command)
    insert_menu.add_command(label="Function", command=insert_command)
    insert_menu.add_command(label="Link", command=insert_command)

    format_menu = tk.Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label="Format", menu=format_menu)
    theme_submenu = tk.Menu(format_menu, tearoff=False)
    format_menu.add_cascade(label="Theme", menu=theme_submenu)
    theme_submenu.add_command(label="Light", command=light_theme_command)
    theme_submenu.add_command(label="Dark", command=dark_theme_command)
    theme_submenu.add_command(label="Blue", command=blue_theme_command)

    number_submenu = tk.Menu(format_menu, tearoff=False)
    format_menu.add_cascade(label="Number", menu=number_submenu)
    number_submenu.add_command(label="Integer", command=format_command)
    number_submenu.add_command(label="Float", command=format_command)

    text_submenu = tk.Menu(format_menu, tearoff=False)
    format_menu.add_cascade(label="Text", menu=text_submenu)
    text_submenu.add_command(label="Bold", command=format_command)
    text_submenu.add_command(label="Italic", command=format_command)
    text_submenu.add_command(label="Underline", command=format_command)
    text_submenu.add_command(label="Strike-through", command=format_command)

    alignment_submenu = tk.Menu(format_menu, tearoff=False)
    format_menu.add_cascade(label="Alignment", menu=alignment_submenu)
    alignment_submenu.add_command(label="Left", command=format_command)
    alignment_submenu.add_command(label="Center", command=format_command)
    alignment_submenu.add_command(label="Right", command=format_command)

    font_submenu = tk.Menu(format_menu, tearoff=False)
    format_menu.add_cascade(label="Font", menu=font_submenu)
    font_submenu.add_command(label="Arial", command=format_command)
    font_submenu.add_command(label="Times New Roman", command=format_command)
    font_submenu.add_command(label="Courier", command=format_command)
    font_submenu.add_command(label="Cosmic Sans", command=cosmic_sans_format_command)

    font_size_submenu = tk.Menu(format_menu, tearoff=False)
    format_menu.add_cascade(label="Font size", menu=font_size_submenu)

    font_size_commands = []
    for size in range(6, 17):
        command = lambda s=size: print(f"Font size {s}")
        font_size_commands.append(command)
        font_size_submenu.add_command(label=str(size), command=font_size_commands[-1])

    labels = []
    for i in range(height + 1):
        for j in range(width + 1):
            if i == 0:
                label_text = chr(65 + j - 1) if j > 0 else ""
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
