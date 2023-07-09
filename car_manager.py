import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_car = []
        self.velocidad_coche = STARTING_MOVE_DISTANCE

    def crear_auto(self):
        random_num = random.randint(1, 7)
        if random_num == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            new_car.setheading(180)

            self.all_car.append(new_car)

    def movimiento_vehicular(self):
        for autos in self.all_car:
            autos.forward(self.velocidad_coche)

    def subir_nivel(self):
        self.velocidad_coche += MOVE_INCREMENT



