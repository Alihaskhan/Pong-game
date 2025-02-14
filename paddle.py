from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(-350, 0)

    def up(self):
        newy = self.ycor()+20
        self.sety(newy)

    def down(self):
        newy = self.ycor()-20
        self.sety(newy)


    def go_right(self):
        self.goto(350, 0)
