from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor()+20)
        else:
            pass

    def down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor()-20)
        else:
            pass
