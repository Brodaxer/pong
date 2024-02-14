from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.speed("slow")
        self.rising = True
        self.descend = False

    def move(self):

        if self.ycor() == 260:
            self.rising = False
            self.descend = True
        elif self.ycor() == -260:
            self.rising = True
            self.descend = False

        if self.descend:
            new_x = self.xcor() + 10
            new_y = self.ycor() - 10
            self.goto(new_x, new_y)
        elif self.rising:
            new_x = self.xcor() + 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)

    def move_back(self):
        if self.ycor() == 260:
            self.rising = False
            self.descend = True
        elif self.ycor() == -260:
            self.rising = True
            self.descend = False

        if self.rising:
            new_x = self.xcor() - 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)
        elif self.descend:
            new_x = self.xcor() - 10
            new_y = self.ycor() - 10
            self.goto(new_x, new_y)

