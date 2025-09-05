import turtle as y
import random
from turtle import Screen

Ichigo=y.Turtle()
Ichigo.speed("fastest")

y.colormode(255) # Maximum value that a rgb color can take

def colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    ran_col=(r,g,b)
    return ran_col

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        Ichigo.color(colour())
        Ichigo.circle(100)
        Ichigo.setheading(Ichigo.heading() + 5)

draw_spirograph(5)



screen=Screen()
screen.exitonclick()