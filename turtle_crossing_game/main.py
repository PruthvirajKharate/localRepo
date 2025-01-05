import time
from turtle import Screen
from player import Player
from car_manager import CarManager, increment_speed
from scoreboard import Scoreboard
from random import choice

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Creating a player
player = Player()
#Creating a turtle for writing score
score = Scoreboard()

screen.listen()
screen.onkey(player.move, 'a')

# Array for storing cars
cars=[]
game_is_on = True


i = 0
while game_is_on:
    time.sleep(0.1)
    if i%50==0:
        for i in range(-250, 250, 20):
            if choice([True, False, False,False]):
                car = CarManager(i)
                cars.append(car)
    i+=1
    for car in cars:
        if car.distance(player)<=10:
            game_is_on=False
            print('Game is over your score is '+score.score)
        if not car.move():
            cars.remove(car)
            del car



    if player.at_finish():
        player.go_to_start()
        score.increment_score()
        increment_speed()


    screen.update()

screen.exitonclick()
