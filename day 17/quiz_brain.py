class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False)?: ")
        self.check_answer(answer, curr_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, q_answer):
        if answer.lower() == q_answer.lower():
            self.score+=1
            print("That's Right!")
        else:
            print("Wrong answer.")
        print(f"The correct answer was: {q_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

