from turtle import Turtle, Screen
import time
import os

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = self.load_high_score()  
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.write_score()

    def load_high_score(self):
        if not os.path.exists("High Score.txt"):  
            with open("High Score.txt", "w") as file:
                file.write("0")
        with open("High Score.txt", "r") as file:
            return int(file.read())

    def save_high_score(self):  
        with open("High Score.txt", "w") as file:
            file.write(str(self.highScore))

    def write_score(self):
        self.clear()
        self.goto(0,300)
        self.write(f"Score: {self.score}  High score: {self.highScore}", font=("boulder", 26, "normal"), align="center")

    def update_score(self):
        self.score += 1
        if self.score > self.highScore:  
            self.highScore = self.score
            self.save_high_score()  
        self.write_score()
        
    def end_message(self):
        window = Screen()
        window.bgcolor("red")
        self.clear()
        self.goto(0, 100)
        self.write(f"\tYou lost🤭\nYour Score: {self.score}, High Score: {self.highScore}",font=("Arial", 26, "normal"), align="center")
        time.sleep(2)
        window.bgcolor("black")  
