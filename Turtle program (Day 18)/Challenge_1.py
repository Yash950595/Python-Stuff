from turtle import Turtle,Screen
import random

Ichigo=Turtle()
Ichigo.shape("classic")
Ichigo.color("Red")

'''def draw_square():
    Ichigo.left(90)
    Ichigo.forward(100)

draw_square()
draw_square()
draw_square()
draw_square()

def dashed_line():
    Ichigo.forward(10)
    Ichigo.penup()
    Ichigo.forward(10)
    Ichigo.pendown()

dashed_line()
dashed_line()
dashed_line()
dashed_line()
dashed_line()'''

num_of_sides = 3  # Start with triangle
colours=["green yellow","dark turquoise","gold","dark red","light pink","medium violet red","medium purple","indigo","dark slate blue"]

def draw_shapes():
    for sides in range(num_of_sides, 11):  # 3 to 10 sides
        angle = 360 / sides
        Ichigo.color(random.choice(colours))
        
        for _ in range(sides):
            Ichigo.forward(100)
            Ichigo.right(angle)
            


draw_shapes()



















'''for _ in range(3):
    Ichigo.forward(100)
    Ichigo.right(120)

for _ in range(4):
    Ichigo.forward(100)
    Ichigo.right(90)

for _ in range(5):
    Ichigo.forward(100)
    Ichigo.right(72)

for _ in range(6):
    Ichigo.forward(100)
    Ichigo.right(60)

for _ in range(7):
    Ichigo.forward(100)
    Ichigo.right(51.42)

for _ in range(8):
    Ichigo.forward(100)
    Ichigo.right(45)

for _ in range(9):
    Ichigo.forward(100)
    Ichigo.right(40)

for _ in range(10):
    Ichigo.forward(100)
    Ichigo.right(36)'''















screen=Screen()
screen.exitonclick()

