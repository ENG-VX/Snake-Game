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
        self.goto(0,300)
        self.write(f"Score: {self.score}  High score: {self.highScore}", font=("boulder", 26, "normal"), align="center")

    def update_score(self):
        self.clear()
        self.score += 1
        if self.score > self.highScore:
            self.highScore = self.score
        self.write_score()
        
    def end_message(self):
           
        # Change screen color to red
        window = Screen()
        window.bgcolor("red")
        
        # Clear the screen and show the message
        self.clear()
        self.goto(0, 100)
        self.write(f"              You lost🤭\nYour Score: {self.score}, High Score: {self.highScore}", font=("Arial", 26, "normal"), align="center")
        
        # Update the screen to reflect the changes
        window.update()
        
        # Wait for 2 seconds before proceeding (this will allow the message to stay visible)
        time.sleep(2)




        

    