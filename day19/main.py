import turtle
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.listen()

def moveForward():
    t.forward(100)
screen.onkey(key="space", fun=moveForward)
screen.exitonclick()