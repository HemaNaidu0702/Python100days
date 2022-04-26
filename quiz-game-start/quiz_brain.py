class QuizBrain:
    def __init__(self, q_list):
        self.ques_number = 0
        self.score = 0
        self.ques_list = q_list


    def still_has_questions(self):
        return self.ques_number < len(self.ques_list)



    def next_question(self):
        current_question = self.ques_list[self.ques_number]
        self.ques_number += 1
        user_answer = input(f"Q.{self.ques_number}: {current_question.text} (True/False: )")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you got it right")
        else:
            print("Wrong!")
        print(f"correct answer is : {correct_answer}.")
        print(f"your current score is: {self.score}/{self.ques_number}")
        print("\n")