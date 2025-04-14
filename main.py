# main.py

from tkinter import *
from admin_login import show_admin_login
from quiz_login import show_quiz_login
from database import create_tables

def main():
    create_tables()

    root = Tk()
    root.title("Quiz Bowl")
    root.geometry("300x200")

    Label(root, text="Welcome to Quiz Bowl!", font=("Arial", 16)).pack(pady=20)

    Button(root, text="Admin Login", width=20, command=lambda: show_admin_login(root)).pack(pady=10)
    Button(root, text="Take a Quiz", width=20, command=lambda: show_quiz_login(root)).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
