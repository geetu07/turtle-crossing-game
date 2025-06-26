from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_cars=[]
        self.carspeed= STARTING_MOVE_DISTANCE

    def create_cars(self):
        spawn_chance = max(1, 6 - self.carspeed // MOVE_INCREMENT)
        if random.randint(1, spawn_chance) == 1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed+=MOVE_INCREMENT