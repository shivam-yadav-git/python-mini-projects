from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
quiz_brain = QuizBrain(question_bank)

for item in question_data:
    question = Question(item['text'], item['answer'])
    question_bank.append(question)

while quiz_brain.next_ques():
    pass

