from turtle import Screen
from paddle import PADDLE
from main import BALL
import time
from main import SCOREBOARD
screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("PONG GAME")
screen.tracer(0)
r_paddle=PADDLE((360,0))
l_paddle=PADDLE((-360,0))
ball=BALL()
ball_speed=1
screen.listen()
screen.onkey(r_paddle.go_up,"o")
screen.onkey(r_paddle.go_down,"l")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
score=SCOREBOARD()
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    if ball.distance(r_paddle) < 20 or ball.xcor() > 390:
        if ball.xcor() > 390:
            ball.new_position()
            score.l_point()
        ball.bounce_x()   

    if ball.distance(l_paddle) < 20 or ball.xcor() <-390:
        if ball.xcor() < -390:
            ball.new_position()
            score.r_point()
        ball.bounce_x()


screen.exitonclick()

