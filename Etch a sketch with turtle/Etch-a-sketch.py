from turtle import Turtle,Screen
import random


Ichigo=Turtle()
screen=Screen()


def mov_ahead():
    Ichigo.forward(10)

def mov_back():
    Ichigo.backward(10)

def mov_left():
    angle=[5,10,15,20,25,30,35,40,45,50,55,60]
    Ichigo.left(random.choice(angle))

def mov_right():
    angle=[5,10,15,20,25,30,35,40,45,50,55,60]
    Ichigo.right(random.choice(angle))

def clear_screen():
    Ichigo.reset()



screen.listen()
screen.onkey(key="w",fun=mov_ahead) 
screen.onkey(key="s",fun=mov_back) 
screen.onkey(key="a",fun=mov_left) 
screen.onkey(key="d",fun=mov_right)
screen.onkey(key="c",fun=clear_screen)

screen.exitonclick()























'''def greet():
    print("Hello!")

def executor(fn):
    fn()  # Calls the function passed

executor(greet())'''
