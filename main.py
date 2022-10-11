from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.listen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
score = Scoreboard()

screen.onkey(r_paddle.move_upward, "Up")
screen.onkey(r_paddle.move_downward, "Down")
screen.onkey(l_paddle.move_upward, "u")
screen.onkey(l_paddle.move_downward, "d")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle) < 40 and ball.xcor() > -360:
        ball.bounce_x()

    # detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.r_point()
    # detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.l_point()
screen.exitonclick()
