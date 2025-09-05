from turtle import Turtle,Screen
import random
Ichigo=Turtle()
Ichigo.width(10)
Ichigo.speed(20)


colours=["green yellow","dark turquoise","gold","dark red","light pink","medium violet red","medium purple","indigo","dark slate blue"]
directions=[0,90,180,270]

for _ in range(250):
    Ichigo.forward(40)
    Ichigo.setheading(random.choice(directions))
    Ichigo.color(random.choice(colours))


screen=Screen()
screen.exitonclick()


