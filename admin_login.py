# admin_login.py

from tkinter import *
from admin_dashboard import show_admin_dashboard

ADMIN_PASSWORD = "admin123"

def show_admin_login(prev_window):
    prev_window.destroy()
    login_window = Tk()
    login_window.title("Admin Login")
    login_window.geometry("300x180")

    Label(login_window, text="Enter Admin Password", font=("Arial", 12)).pack(pady=10)
    
    password_entry = Entry(login_window, show="*", width=25)
    password_entry.pack(pady=5)

    feedback_label = Label(login_window, text="", fg="red")
    feedback_label.pack()

    def try_login():
        if password_entry.get() == ADMIN_PASSWORD:
            login_window.destroy()
            show_admin_dashboard()
        else:
            feedback_label.config(text="Incorrect password!")

    Button(login_window, text="Login", command=try_login).pack(pady=10)
    Button(login_window, text="Back", command=lambda: go_back(login_window)).pack()

def go_back(window):
    window.destroy()
    from main import main
    main()