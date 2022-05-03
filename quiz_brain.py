

class QuizBrain:
    def __init__(self,question_bank):
        self.current_question = 0
        self.question_bank = question_bank

    def next_ques(self):
        if self.current_question < len(self.question_bank):
            answer = input(f"Question: {self.question_bank[self.current_question].text}(True/False): ")
            if answer == self.question_bank[self.current_question].answer:
                self.current_question += 1
                print("Correct")
                return True
            else:
                print("Incorrect")
                print(f"Your score is {self.current_question}")
                return False
        else:
            print("You have won the game !!")
            return False
