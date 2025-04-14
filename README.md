# Quiz Bowl Application

This project is a Python-based Quiz Bowl application developed as part of a Business Information Technology course at Tennessee Tech University. 
The app allows students to take quizzes by subject and enables admins to securely add and manage questions.

Features:

- Quiz Mode** for Students  
  Users can take quizzes based on five subject areas:
  - Quality and Productivity Systems
  - Business Strategy
  - Business Applications Development
  - Management Information Systems
  - Business Intelligence and Analytics

- Admin Mode (Password Protected)  
  Admins can:
  - Log in with a password
  - Enter new questions
  - Assign questions to subjects

- Database Integration
  All questions are stored in an SQLite database (`quiz.db`) for persistent storage.

- Modular Codebase
  - `main.py`: Launches the application
  - `question.py`: Contains the `Question` class
  - `admin_interface.py`: Handles the admin GUI
  - `user_interface.py`: Handles the quiz-taking GUI
