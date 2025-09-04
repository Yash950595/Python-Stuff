from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-290,250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level:{self.level}",align="left",font=FONT)
        
    def increase_score(self):
        self.level += 1
        self.update_score() #Error was caused beacuse on missing the parenthesis update_score is just like refrence object rather than a method

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)