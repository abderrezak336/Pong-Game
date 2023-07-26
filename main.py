from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from wall import Wall
import time



scoreboard = Scoreboard()

screen = Screen()

r_paddle = Paddle(x=360, y=0)

l_paddle = Paddle(x=-360, y=0)


ball = Ball()

wall = Wall()


screen.tracer(0)

screen.bgcolor("black")

screen.title("PongGame")

screen.setup(width=800, height=600)

user_input = screen.textinput("Level", "choose the level please 'hard', 'not hard', 'easy': ")
screen.listen()


screen.onkey(r_paddle.r_up, "Up")

screen.onkey(r_paddle.r_down, "Down")

screen.onkey(l_paddle.l_up, "z")

screen.onkey(l_paddle.l_down, "s")

scoreboard.updatescreen()



game_is_on = True

while game_is_on:
    if user_input == "hard":
        time.sleep(0.03)

    elif user_input == "not hard":
        time.sleep(0.05)

    elif user_input == "easy":
        time.sleep(0.08)



    screen.update()


    ball.move_the_ball()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.second_bounce()


    if ball.xcor() > 380:
        ball.backhome()
        ball.x_move *= -1
        scoreboard.increas_l_score()

    if ball.xcor() < -380:
        ball.backhome()
        ball.x_move *= -1
        scoreboard.increas_r_score()

















screen.exitonclick()








































screen.exitonclick()

