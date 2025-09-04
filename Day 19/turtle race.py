from turtle import Turtle,Screen
import random

screen=Screen()

screen.setup(width=500,height=400)
your_bet = screen.textinput(title="User input",prompt="Which color turtle wins the race: ") #prompt already works like input function.No need to give extra input function
print(your_bet)
colours=["red","yellow","blue","green","orange","pink"]
y_position=[-70,-40,-10,20,50,80]  ### position of the turtle is taken from its center and not the dimensions that are given for the turtle



for multi_turtles in range (0,6):
    Ichigo=Turtle(shape="turtle")
    Ichigo.color(colours[multi_turtles])
    Ichigo.penup()
    Ichigo.goto(x=-230,y=y_position[multi_turtles])


screen.exitonclick()
