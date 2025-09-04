from turtle import Turtle

STARTING_POSITION = (0, -280) #this is a tuple 
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle): #This is a method
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
        
    def go_up(self): #Function declared into a class is called method and takes self as the argument
        self.forward(MOVE_DISTANCE)

    def move_to_start(self):
        self.goto(STARTING_POSITION)
    
    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False
