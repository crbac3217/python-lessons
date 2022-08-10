from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("Blue")


def drawShape(points):
    for _ in range(points):
        t.forward(100)
        t.right(360/points)

for _ in range(3, 8):
    drawShape(_)

screen = Screen()
screen.exitonclick()

