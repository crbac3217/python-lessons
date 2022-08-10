from turtle import Turtle, Screen
import time
from snake import Snake

isgameover = False
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snek")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while isgameover != True:
    screen.update()
    time.sleep(0.2)
    snake.move()




screen.exitonclick()