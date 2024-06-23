from tkinter import *
from tkinter import messagebox
from plyer import notification
import time

def timer():
    try:
        # Calculate total seconds entered by the user
        timer_seconds = int(hour_entry.get()) * 3600 + int(min_entry.get()) * 60 + int(sec_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter valid integers.")
        return

    # Countdown loop
    while timer_seconds > 0:
        # Calculate hours, minutes, seconds
        hours = timer_seconds // 3600
        minutes = (timer_seconds % 3600) // 60
        seconds = timer_seconds % 60

        # Update the GUI
        hour_var.set(hours)
        min_var.set(minutes)
        sec_var.set(seconds)
        window.update()

        # Wait for 1 second
        time.sleep(1)
        timer_seconds -= 1

    # Show notification when countdown is complete
    notification_title = "Timer Alert"
    notification_message = "Your countdown timer has ended!"
    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=10,  # Notification stays for 10 seconds
    )
    messagebox.showinfo("Timer Complete", "Countdown timer has ended!")

# GUI setup
window = Tk()
window.title("Countdown Timer")
window.geometry("300x250")

# Labels
Label(window, text="Hours").grid(row=0, column=0, padx=5, pady=5)
Label(window, text="Minutes").grid(row=1, column=0, padx=5, pady=5)
Label(window, text="Seconds").grid(row=2, column=0, padx=5, pady=5)

# Entry fields
hour_var = StringVar()
min_var = StringVar()
sec_var = StringVar()

hour_entry = Entry(window, textvariable=hour_var, width=5)
min_entry = Entry(window, textvariable=min_var, width=5)
sec_entry = Entry(window, textvariable=sec_var, width=5)

hour_entry.grid(row=0, column=1, padx=5, pady=5)
min_entry.grid(row=1, column=1, padx=5, pady=5)
sec_entry.grid(row=2, column=1, padx=5, pady=5)

# Activate Timer Button
Button(window, text="Activate Timer", command=timer, bg="red", fg="white").grid(row=3, columnspan=2, pady=10)

# Start GUI
window.mainloop()
