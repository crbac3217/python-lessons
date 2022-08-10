from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

isgameover = False
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snek")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def ate_food():
    food.MoveRandom()
    snake.IncreaseOne()
    scoreboard.increase_one()


while isgameover != True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <= 15:
        ate_food()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        isgameover = True
        scoreboard.game_over()
    for seg in snake.snek[1:]:
        if snake.head.distance(seg) < 10:
            isgameover = True
            scoreboard.game_over()

screen.exitonclick()