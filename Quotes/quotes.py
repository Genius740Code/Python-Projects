import tkinter as tk
import random

def get_daily_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "It always seems impossible until it's done. - Nelson Mandela",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "Strive not to be a success, but rather to be of value. - Albert Einstein",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
        "The best way to predict the future is to create it. - Peter Drucker",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "Your attitude, not your aptitude, will determine your altitude. - Zig Ziglar",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
        "The secret to getting ahead is getting started. - Mark Twain",
        "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
        "The best way to predict the future is to create it. - Peter Drucker",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "Your attitude, not your aptitude, will determine your altitude. - Zig Ziglar",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
        "The secret to getting ahead is getting started. - Mark Twain",
        "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "You miss 100% of the shots you don't take. - Wayne Gretzky",
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "If you want to achieve greatness stop asking for permission. - Anonymous",
        "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
        "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
        "The future belongs to those who prepare for it today. - Malcolm X",
        "Believe in yourself, take on your challenges, dig deep within yourself to conquer fears. - Chantal Sutherland",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The best way to predict the future is to create it. - Peter Drucker",
    ]

    return random.choice(quotes)

def show_daily_quote():
    quote = get_daily_quote()
    quote_label.config(text=quote)

root = tk.Tk()
root.title("Daily Quote App")
root.geometry("500x300")
root.configure(bg="#1e1e1e")

quote_label = tk.Label(root, text="", font=("Arial", 14), fg="white", bg="#1e1e1e", wraplength=400, justify='center')
quote_label.pack(pady=20)

get_quote_button = tk.Button(root, text="Get Daily Quote", command=show_daily_quote, fg="#1e1e1e", bg="#bf6161")
get_quote_button.pack(pady=10)

root.mainloop()
