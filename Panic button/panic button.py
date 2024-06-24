import keyboard
import psutil
import webbrowser
import tkinter as tk

close_apps = False
excluded_apps = {'notepad.exe'}  # Use a set for faster membership checking

def is_user_application(process):
    """Check if a process is a user application."""
    try:
        if process.username() != 'SYSTEM' and process.status() in {psutil.STATUS_IDLE, psutil.STATUS_RUNNING}:
            return True
    except psutil.Error:
        pass
    return False

def close_specified_applications():
    process_names = {'chrome.exe', 'notepad.exe'}  # Use a set for faster membership checking

    for process in psutil.process_iter(['pid', 'name', 'username', 'status']):
        if process.info['name'] in process_names and process.info['name'] not in excluded_apps and is_user_application(process):
            try:
                process.terminate()
                print(f"Terminated {process.info['name']} (PID {process.info['pid']})")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

def open_youtube():
    print("Opening YouTube...")
    webbrowser.open("https://www.youtube.com/")

def check_key_combination(e):
    if keyboard.is_pressed('page up') and keyboard.is_pressed('page down') and keyboard.is_pressed('`'):
        print("Key combination detected!")
        if close_apps:
            close_specified_applications()
        else:
            close_all_user_applications()
        open_youtube()
        root.quit()

def on_button_click():
    if close_apps:
        close_specified_applications()
    else:
        close_all_user_applications()
    open_youtube()
    root.quit()

def on_closing():
    root.destroy()
    print("Press 'esc' to exit the script.")
    keyboard.wait('esc')

def toggle_close_apps():
    global close_apps
    close_apps = not close_apps
    print(f"Close specified applications: {close_apps}")

def close_all_user_applications():
    for process in psutil.process_iter(['pid', 'name', 'username', 'status']):
        if is_user_application(process) and process.info['name'] not in excluded_apps:
            try:
                process.terminate()
                print(f"Terminated {process.info['name']} (PID {process.info['pid']})")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

keyboard.hook(check_key_combination)

root = tk.Tk()
root.title("Close Applications and Open YouTube")

button = tk.Button(root, text="Panic Button", command=on_button_click)
button.pack(pady=20)

checkbox = tk.Checkbutton(root, text="Close Only Specified Apps", command=toggle_close_apps)
checkbox.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
