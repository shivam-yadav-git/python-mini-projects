from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def create_scoreboard(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        current_score = f"Score {self.score}"
        self.clear()
        self.write(current_score, False, 'center', ('Arial', 8, 'normal'))

    def update_score(self):
        self.score += 1

    def game_over(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over !!", False, 'center', ('Arial', 8, 'normal'))
