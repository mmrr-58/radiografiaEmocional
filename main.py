from database import *

answers = {}
questions = sendQuestions('daily')
for question in questions:
    answer = input(f"{question[1]}: ")
    answers[question[0]] =  answer

recordAnswers(answers)