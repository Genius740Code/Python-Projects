import os

def restart_windows():
    os.system('shutdown /r /t 1')

def shutdown_computer():
    try:
        os.system("shutdown /s /t 1")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Restart Windows")
    print("2. Shutdown Computer")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        restart_windows()
    elif choice == "2":
        shutdown_computer()
    else:
        print("Invalid choice. Please enter either '1' or '2'.")
