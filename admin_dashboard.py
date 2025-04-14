from tkinter import *
from tkinter import ttk, messagebox
from admin_add_questions import show_add_question
import sqlite3

DB_NAME = "quiz.db"

def show_admin_dashboard():
    dashboard = Tk()
    dashboard.title("Admin Dashboard")
    dashboard.geometry("300x250")

    Label(dashboard, text="Admin Panel", font=("Arial", 16)).pack(pady=15)

    Button(dashboard, text="Add Question", width=20, command=lambda: go_to_add(dashboard)).pack(pady=5)
    Button(dashboard, text="Manage Questions", width=20, command=lambda: go_to_manage(dashboard)).pack(pady=5)
    Button(dashboard, text="Back to Main Menu", width=20, command=lambda: go_back(dashboard)).pack(pady=10)

def go_to_add(current_window):
    current_window.destroy()
    show_add_question()

def go_back(current_window):
    current_window.destroy()
    from main import main
    main()

def go_to_manage(current_window):
    current_window.destroy()
    manage_win = Tk()
    manage_win.title("Manage Questions")
    manage_win.geometry("700x400")

    # Entry fields
    Label(manage_win, text="Question:").pack()
    question_entry = Entry(manage_win, width=80)
    question_entry.pack()

    Label(manage_win, text="Answer:").pack()
    answer_entry = Entry(manage_win, width=80)
    answer_entry.pack()

    Label(manage_win, text="Subject:").pack()
    subject_var = StringVar()
    subject_dropdown = ttk.Combobox(manage_win, textvariable=subject_var, width=77)
    subject_dropdown['values'] = (
        "Quality and Productivity Systems",
        "Business Strategy",
        "Business Applications Development",
        "Management Information Systems",
        "Business Intelligence and Analytics"
    )
    subject_dropdown.pack()

    selected_id = None

    def load_questions():
        for row in tree.get_children():
            tree.delete(row)
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("SELECT id, question, answer, subject FROM questions")
        for row in c.fetchall():
            tree.insert('', 'end', values=row)
        conn.close()

    def select_row(event):
        nonlocal selected_id
        selected = tree.focus()
        values = tree.item(selected, 'values')
        if values:
            selected_id = values[0]
            question_entry.delete(0, END)
            question_entry.insert(0, values[1])
            answer_entry.delete(0, END)
            answer_entry.insert(0, values[2])
            subject_var.set(values[3])

    def update_question():
        if not selected_id:
            messagebox.showwarning("Select", "Please select a question to update.")
            return
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("UPDATE questions SET question=?, answer=?, subject=? WHERE id=?",
                  (question_entry.get(), answer_entry.get(), subject_var.get(), selected_id))
        conn.commit()
        conn.close()
        load_questions()
        clear_entries()

    def delete_question():
        if not selected_id:
            messagebox.showwarning("Select", "Please select a question to delete.")
            return
        result = messagebox.askyesno("Delete", "Are you sure you want to delete this question?")
        if result:
            conn = sqlite3.connect(DB_NAME)
            c = conn.cursor()
            c.execute("DELETE FROM questions WHERE id=?", (selected_id,))
            conn.commit()
            conn.close()
            load_questions()
            clear_entries()

    def clear_entries():
        question_entry.delete(0, END)
        answer_entry.delete(0, END)
        subject_var.set("")
        nonlocal selected_id
        selected_id = None

    Button(manage_win, text="Update", command=update_question).pack(pady=5)
    Button(manage_win, text="Delete", command=delete_question).pack(pady=5)

    tree = ttk.Treeview(manage_win, columns=("ID", "Question", "Answer", "Subject"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Question", text="Question")
    tree.heading("Answer", text="Answer")
    tree.heading("Subject", text="Subject")
    tree.pack(pady=10, fill="x")
    tree.bind("<ButtonRelease-1>", select_row)

    load_questions()