import keyboard
import psutil
import webbrowser

def close_all_applications():
    process_names = ['chrome.exe', 'notepad.exe'] #App to close

    for process_name in process_names:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                print(f"Terminating {process_name} (PID {process.info['pid']})")
                process.terminate()

def open_youtube():
    print("Opening YouTube...")
    webbrowser.open("https://www.youtube.com/") #App to open

def check_key_combination(e):
    if keyboard.is_pressed('page up') and keyboard.is_pressed('page down') and keyboard.is_pressed('`'): #Buttons to press
        print("Key combination detected!")
        close_all_applications()
        open_youtube()

keyboard.hook(check_key_combination)

print("Press 'esc' to exit the script.")
keyboard.wait('esc')  # Wait for the user to press 'esc' to exit the script
