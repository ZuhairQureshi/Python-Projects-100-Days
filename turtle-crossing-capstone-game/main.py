import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

counter = 0
tick = 0.1
rand_count = random.randint(5, 15)
player = Player()
moving_cars = CarManager()
scoreboard = Scoreboard()
game_is_on = True
gaming = True


def restart():
    global tick, counter, game_is_on, gaming, player

    if not gaming:
        gaming = True
        counter = 0
        player.reset_position()
        scoreboard.score = 1
        scoreboard.update()
        tick = 0.1
        moving_cars.clear_list()
        moving_cars.cars.clear()
        game_is_on = True
        game_loop()

def quit():
    global gaming
    if not gaming:
        screen.bye()


screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(restart, "p")
screen.onkey(quit, "q")


def game_loop():
    global tick, counter, rand_count, player, moving_cars, scoreboard, game_is_on, gaming
    while game_is_on:
        time.sleep(tick)
        screen.update()
        moving_cars.move()
        counter += 1

        if counter % rand_count == 0:
            counter = 0
            rand_count = random.randint(1,7)
            moving_cars.generate_car()

        for car in moving_cars.cars:
            if car.xcor() - player.xcor() <= 20 and player.distance(car.pos()) <= 20:
                game_is_on = False
                gaming = False
                scoreboard.game_over()

            if car.xcor() < -350:
                moving_cars.cars.remove(car)
                car.hideturtle()

        if player.ycor() > 300:
            moving_cars.clear_list()
            moving_cars.cars.clear()
            scoreboard.score += 1
            scoreboard.update()
            player.reset_position()
            tick *= 0.5

game_loop()
screen.exitonclick()