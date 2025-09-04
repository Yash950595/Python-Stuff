import turtle as y
import random
from turtle import Screen
Ichigo=y.Turtle()
Ichigo.width(10)
Ichigo.speed(20)

y.colormode(255) # Maximum value that a rgb color can take
def colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    ran_col=(r,g,b)
    return ran_col


directions=[0,90,180,270]

for _ in range(250):
    Ichigo.forward(40)
    Ichigo.setheading(random.choice(directions))
    Ichigo.color(colour())


screen=Screen()
screen.exitonclick()