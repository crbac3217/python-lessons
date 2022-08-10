from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.player = 1

    def set_up_paddle(self):
        if self.player == 1:
            self.goto(350, 0)
        else:
            self.goto(-350, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        print(f"{self.player} paddle is moving up")

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        print(f"{self.player} paddle is moving down")
