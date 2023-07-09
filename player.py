from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1)
        self.color("blue")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def volver_empezar(self):
        self.goto(STARTING_POSITION)

    def llegada(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


    def game_over(self):
        self.write("Juego Terminado",align= "center", font= ("Courier", 24, "normal"))


