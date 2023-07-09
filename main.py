import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Tortuga Crash")

jugador = Player()
autos = CarManager()
puntos = Scoreboard()

screen.listen()
screen.onkey(jugador.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    puntos.actual_puntos()
    autos.crear_auto()
    autos.movimiento_vehicular()
    jugador.llegada()

    for car in autos.all_car:
        if car.distance(jugador) < 20:
            jugador.game_over()
            game_is_on = False

    if jugador.llegada():
        puntos.sumar_puntos()
        jugador.volver_empezar()
        autos.subir_nivel()



screen.exitonclick()