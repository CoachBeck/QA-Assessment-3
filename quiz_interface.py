# quiz_interface.py

from tkinter import *
from database import get_questions
from questions import Question

def start_quiz(category):
    questions_raw = get_questions(category)
    questions = [Question(q[0], q[1:5], q[5]) for q in questions_raw]

    if not questions:
        no_data_window = Tk()
        no_data_window.title("No Questions")
        Label(no_data_window, text="No questions available in this category.", fg="red").pack(pady=20)
        Button(no_data_window, text="Back", command=lambda: go_back(no_data_window)).pack()
        return

    QuizInterface(questions)

def go_back(window):
    window.destroy()
    from main import main
    main()

class QuizInterface:
    def __init__(self, questions):
        self.questions = questions
        self.index = 0
        self.score = 0

        self.window = Tk()
        self.window.title("Quiz Time!")
        self.window.geometry("500x300")

        self.question_label = Label(self.window, text="", wraplength=400, font=("Arial", 12))
        self.question_label.pack(pady=20)

        self.options_var = StringVar()
        self.option_buttons = []
        for _ in range(4):
            btn = Radiobutton(self.window, text="", variable=self.options_var, value="", font=("Arial", 10))
            btn.pack(anchor="w", padx=50)
            self.option_buttons.append(btn)

        self.feedback_label = Label(self.window, text="", font=("Arial", 10))
        self.feedback_label.pack(pady=5)

        Button(self.window, text="Submit Answer", command=self.check_answer).pack(pady=10)

        self.load_question()

        self.window.mainloop()

    def load_question(self):
        if self.index < len(self.questions):
            q = self.questions[self.index]
            self.question_label.config(text=f"Q{self.index + 1}: {q.text}")
            self.options_var.set(None)
            for i, opt in enumerate(q.options):
                self.option_buttons[i].config(text=opt, value=opt)
            self.feedback_label.config(text="")
        else:
            self.show_results()

    def check_answer(self):
        selected = self.options_var.get()
        if not selected:
            self.feedback_label.config(text="Please select an answer.", fg="red")
            return
        if self.questions[self.index].is_correct(selected):
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            correct = self.questions[self.index].correct_answer
            self.feedback_label.config(text=f"Incorrect! Correct answer was: {correct}", fg="red")
        self.index += 1
        self.window.after(1000, self.load_question)

    def show_results(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        Label(self.window, text="Quiz Completed!", font=("Arial", 16)).pack(pady=20)
        Label(self.window, text=f"Your Score: {self.score} out of {len(self.questions)}").pack(pady=10)
        Button(self.window, text="Back to Main Menu", command=self.restart).pack(pady=10)

    def restart(self):
        self.window.destroy()
        from main import main
        main()
