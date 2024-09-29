from turtle import Turtle,Screen
import time

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,300)
        

    def write_score(self):
        self.write(f"Score: {self.score}  High score: {self.highScore}", font=("boulder", 26, "normal"), align="center")

    def update_score(self):
        self.clear()
        self.score += 1
        if self.score > self.highScore:
            self.highScore = self.score
        self.write_score()
        
    def end_massage(self):
        window = Screen()
        window.bgcolor("red")
        self.goto(0,0)
        self.write("You lost🤭", font=("Arial", 26, "normal"), align="center")
        time.sleep(2)
        

    