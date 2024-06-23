libraries_to_check = [
    "keyboard", "psutil", "requests", "numpy", "matplotlib",
    "pandas", "seaborn", "scipy", "scikit-learn", "tensorflow",
    "torch", "flask", "django", "pygame", "sqlalchemy",
    "beautifulsoup4", "pyqt5", "tkinter", "pyaudio", "pyttsx3",
    "pywhatkit", "pyautogui", "pyperclip", "openpyxl", "pyyaml",
    "pytz", "pillow", "opencv-python", "qrcode", "matplotlib",
    "folium", "selenium", "twilio", "pyjwt", "pycryptodome",
    "paramiko", "flask-restful", "fastapi",
]

missing_libraries = []

def print_status(library, is_installed):
    status = "Installed" if is_installed else "Not Installed"
    print(f"{library:20} : {status}")

print("Checking library status:")
print("-" * 40)

for library in libraries_to_check:
    try:
        __import__(library)
        print_status(library, True)
    except ImportError:
        missing_libraries.append(library)
        print_status(library, False)

print("\nSummary:")
if missing_libraries:
    print("The following libraries are missing:")
    for missing_library in missing_libraries:
        print(f" - {missing_library}")
else:
    print("All the libraries are installed.")
