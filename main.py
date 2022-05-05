from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

scoreboard = Scoreboard()
food = Food()
game_is_on = True
scoreboard.create_scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if food.distance(snake.head) < 20:
        food.create_food()
        snake.add_snake_tail()
        scoreboard.update_score()
        scoreboard.create_scoreboard()
    if snake.head.xcor()>290 or snake.head.xcor()< -290 or snake.head.ycor()>290 or snake.head.ycor()< -290:
        scoreboard.game_over()
        game_is_on = False

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.game_over()
            game_is_on = False





screen.exitonclick()