from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for n in question_data:
    question_bank.append(Question(n["question"], n["correct_answer"]))
    # print(n["text"], n["answer"])

# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score was: {quiz.score}/{len(quiz.question_list)}")
