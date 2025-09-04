from turtle import Turtle,Screen
from paddle import N_Paddle
from ball import P_Ball
from scoreboard import scorecard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("THE PONG GAME")
screen.tracer(0)



r_paddle=N_Paddle((350,0))
l_paddle=N_Paddle((-350,0))
ball=P_Ball((0,0))
score=scorecard()


screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"a")
screen.onkeypress(l_paddle.go_down,"z")

is_game_on=True

while is_game_on:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()
    
    #Ball bounces from the top of screen
    if ball.ycor() >280 or ball.ycor() < -280: 
        ball.bounce_y()

    #Ball bounces from the Side window on hitting the paddle as 
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #Ball goes missing when not hit by r_paddle
    if ball.xcor() > 380:
        ball.miss()
        score.l_point()

    #Ball goes missing when not hit by l_paddle
    if ball.xcor() < -380:
        ball.miss()
        score.r_point()

screen.exitonclick()
