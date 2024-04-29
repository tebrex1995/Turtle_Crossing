import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 270

screen = Screen()
turtle = Player((0, -280))
car = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(turtle.move, "Up")

counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    #Car movement
    car.create_car()
    car.move()

    #Collision with a car
    for x in car.cars:
        if x.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Turtle goes to finish line
    if turtle.ycor() > FINISH_LINE_Y:
        turtle.return_to_start()
        car.increase_speed()
        scoreboard.increase_level()


screen.exitonclick()