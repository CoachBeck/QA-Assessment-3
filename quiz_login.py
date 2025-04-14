# quiz_login.py

from tkinter import *
from database import CATEGORIES
from quiz_interface import start_quiz

def show_quiz_login(prev_window):
    prev_window.destroy()
    window = Tk()
    window.title("Choose a Quiz")
    window.geometry("300x200")

    Label(window, text="Select a Quiz Category", font=("Arial", 14)).pack(pady=10)

    category_var = StringVar()
    category_var.set(CATEGORIES[0])

    OptionMenu(window, category_var, *CATEGORIES).pack(pady=10)

    Button(window, text="Start Quiz", command=lambda: launch_quiz(window, category_var.get())).pack(pady=10)
    Button(window, text="Back", command=lambda: go_back(window)).pack()

def launch_quiz(window, category):
    window.destroy()
    start_quiz(category)

def go_back(window):
    window.destroy()
    from main import main
    main()
