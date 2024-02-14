import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from gameover import Game_over

screen = Screen()
screen.bgcolor("black")
screen.title("Pong game")
screen.setup(width=800, height=600)
player1 = Paddle()
player2 = Paddle()
player1.goto(350, 0)
player2.goto(-350, 0)
end = Game_over()
screen.listen()
direction_heading = "Right"

screen.onkeypress(player1.down, "Down")
screen.onkeypress(player1.up, "Up")
screen.onkeypress(player2.down, "s")
screen.onkeypress(player2.up, "w")
screen.tracer(0)

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if ball.distance(player1) < 15:
        direction_heading = "Left"
    elif ball.distance(player2) < 15:
        direction_heading = "Rgiht"

    if direction_heading == "Right":
        ball.move()
        print("aa")
    elif direction_heading == "Left":
        print("BB")
        ball.move_back()
    else:
        print("cc")
        ball.move()

    if ball.xcor() > 380 or ball.xcor() < -380:
        if direction_heading == "Right":
            end.write("Winner player 2", align= "center" ,font=("Ariel", 30, "normal"))
        elif direction_heading == "Left":
            end.write("Winner player 1", align= "center", font=("Ariel", 30, "normal"))
        game_is_on = False










screen.exitonclick()
