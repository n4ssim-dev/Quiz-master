import tkinter
import requests
import json

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Requête Trivia db pour récupérer 10 questions True/False
response = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
if response.status_code == requests.codes.ok:
    new_questions = response.json()['results']
    file_content = f"question_data = {json.dumps(new_questions, indent=4)}"

    with open('data.py', 'w') as f:
        f.write(file_content)
else:
    print("Fail")

try:
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)

    while quiz.still_has_questions():
       quiz.next_question()

except KeyboardInterrupt:
    print("\n\n\nGame terminated.")

