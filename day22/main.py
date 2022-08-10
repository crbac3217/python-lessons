from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
isgameover = False;

paddle1 = Paddle()
paddle1.player = 1
paddle1.set_up_paddle()

paddle2 = Paddle()
paddle2.player = 2
paddle2.set_up_paddle()

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

while not isgameover:
    screen.update()

screen.exitonclick()
