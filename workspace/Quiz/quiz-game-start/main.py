""" Main Program implemented used OOPs concept """


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for text in question_data:
    question = Question(text["text"], text["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

quiz_on = True

while quiz_on:
    quiz.next_question()
    quiz_on = quiz.still_has_questions()
    if not quiz_on:
        print("You've completed the quiz. Hurray!")
        print(f"Your final score is {quiz.score}/{quiz.question_number}")
