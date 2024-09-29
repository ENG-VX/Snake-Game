import random
from turtle import Turtle
class Food(Turtle):

    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        x = random.randint(-360,360)
        y = random.randint(-310,310)
        self.goto(x,y)

    def aper(self):
        x = random.randint(-360,360)
        y = random.randint(-310,310)
        self.goto(x,y)

    def delete(self):
        self.hideturtle()