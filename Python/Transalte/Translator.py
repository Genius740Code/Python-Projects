from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from textblob import TextBlob

language = googletrans.LANGUAGES

def translate():
    try:
        txt = text1.get(1.0, END)
        c1 = combo1.get()
        c2 = combo2.get()
        
        if txt:
            words = TextBlob(txt)
            lan = words.detect_language()
            
            for key, value in language.items():
                if value == c2:
                    lan_ = key
            
            words = words.translate(from_lang=lan, to=lan_)
            text2.delete(1.0, END)
            text2.insert(END, words)
    
    except Exception as e:
        messagebox.showerror("Error", "An error occurred. Please try again.")

# GUI setup
window = Tk()
window.title("DataFlair Language Translation")
window.geometry("600x500")
window.resizable(False, False)

lang_value = list(language.values())

combo1 = ttk.Combobox(window, values=lang_value, state='readonly')
combo1.place(x=100, y=20)
combo1.set("Choose a language")

f1 = Frame(window, bg='black', bd=4)
f1.place(x=100, y=100, width=150, height=150)

text1 = Text(f1, font="Roboto 14", bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=140, height=140)

combo2 = ttk.Combobox(window, values=lang_value, state='readonly')
combo2.place(x=300, y=20)
combo2.set("Choose a language")

f2 = Frame(window, bg='black', bd=4)
f2.place(x=300, y=100, width=150, height=150)

text2 = Text(f2, font="Roboto 14", bg='white', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=140, height=140)

button = Button(window, text='Translate', font=('normal', 15), bg='yellow', command=translate)
button.place(x=230, y=300)

window.mainloop()
