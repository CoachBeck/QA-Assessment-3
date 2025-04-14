# admin_add_question.py

from tkinter import *
from database import add_question, CATEGORIES

def show_add_question():
    window = Tk()
    window.title("Add Question")
    window.geometry("400x400")

    Label(window, text="Add New Quiz Question", font=("Arial", 14)).pack(pady=10)

    # Category Dropdown
    Label(window, text="Select Category:").pack()
    category_var = StringVar(window)
    category_var.set(CATEGORIES[0])  # Default value
    OptionMenu(window, category_var, *CATEGORIES).pack()

    # Question Text
    Label(window, text="Question:").pack()
    question_entry = Entry(window, width=50)
    question_entry.pack()

    # Multiple-Choice Options
    options_entries = []
    for i in range(4):
        Label(window, text=f"Option {i + 1}:").pack()
        entry = Entry(window, width=40)
        entry.pack()
        options_entries.append(entry)

    # Correct Answer Dropdown
    Label(window, text="Correct Answer:").pack()
    correct_answer_var = StringVar(window)
    correct_answer_var.set("Option 1")
    OptionMenu(window, correct_answer_var, "Option 1", "Option 2", "Option 3", "Option 4").pack()

    feedback_label = Label(window, text="", fg="green")
    feedback_label.pack(pady=5)

    def submit_question():
        category = category_var.get()
        question = question_entry.get()
        options = [entry.get() for entry in options_entries]
        answer = options[["Option 1", "Option 2", "Option 3", "Option 4"].index(correct_answer_var.get())]

        if not question or any(opt == "" for opt in options):
            feedback_label.config(text="Please fill out all fields!", fg="red")
            return

        add_question(category, question, *options, answer)
        feedback_label.config(text="Question added successfully!", fg="green")
        question_entry.delete(0, END)
        for entry in options_entries:
            entry.delete(0, END)

    Button(window, text="Submit Question", command=submit_question).pack(pady=10)
    Button(window, text="Back to Admin Menu", command=lambda: go_back(window)).pack()

def go_back(window):
    window.destroy()
    from admin_dashboard import show_admin_dashboard
    show_admin_dashboard()