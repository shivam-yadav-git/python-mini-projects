from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.turtlesize(0.5, 0.5)
        self.penup()
        self.create_food()


    def create_food(self):
        set_x = random.randint(-280, 280)
        set_y = random.randint(-280, 280)
        self.goto(set_x, set_y)


