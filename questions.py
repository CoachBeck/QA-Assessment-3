# question.py

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, selected_option):
        return selected_option == self.correct_answer

    def __str__(self):
        return f"{self.text}\nOptions: {self.options}"