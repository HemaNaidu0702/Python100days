from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for ques in question_data:
    ques_text = ques["text"]
    ques_answer = ques["answer"]
    new_question = Question(ques_text, ques_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Youve completed the quiz")
print(f"Your final score is: {quiz.score} / {quiz.ques_number}")