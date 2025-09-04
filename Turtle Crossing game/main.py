import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p=Player()
car_manager=CarManager()
score=Scoreboard()

screen.listen()
screen.onkey(p.go_up,"Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car() #This is a method. Here car_manager is the object that holds the CarManager class
    car_manager.move_cars() #This method here tells us about the all the moving cars.

    #Detect the collision with cars
    for car in car_manager.all_cars:
        if car.distance(p) < 20: #here error was caused beacuse even after importing we had assigned Player class name to the "p" variable
            game_is_on=False
            score.game_over()

    if p.is_at_finish_line():
        p.move_to_start()
        car_manager.level_up()
        score.increase_score()


screen.exitonclick()