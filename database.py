# database.py
import sqlite3

DB_NAME = "quiz_data.db"
CATEGORIES = [
    "Quality and Productivity Systems",
    "Business Strategy",
    "Business Applications Development",
    "Management Information Systems",
    "Business Intelligence and Analytics"
    ]

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    with connect() as conn:
        c = conn.cursor()
        for category in CATEGORIES:
            c.execute(f'''
                CREATE TABLE IF NOT EXISTS "{category}" (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question TEXT NOT NULL,
                    option1 TEXT NOT NULL,
                    option2 TEXT NOT NULL,
                    option3 TEXT NOT NULL,
                    option4 TEXT NOT NULL,
                    answer TEXT NOT NULL
                )
            ''')
        conn.commit()

def add_question(category, question, option1, option2, option3, option4, answer):
    with connect() as conn:
        c = conn.cursor()
        c.execute(f'''
            INSERT INTO "{category}" (question, option1, option2, option3, option4, answer)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (question, option1, option2, option3, option4, answer))
        conn.commit()

def get_questions(category):
    with connect() as conn:
        c = conn.cursor()
        c.execute(f'SELECT question, option1, option2, option3, option4, answer FROM "{category}"')
        return c.fetchall()