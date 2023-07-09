FONT = ("Courier", 22, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-180, 270)
        self.punts = 0
        self.hideturtle()

    def actual_puntos(self):
        self.clear()
        self.write(f"El Puntaje : {self.punts}", align="center", font=FONT)


    def sumar_puntos(self):
        self.punts +=1
        self.actual_puntos()

