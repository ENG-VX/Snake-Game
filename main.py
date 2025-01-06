from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time

window = Screen()
window.setup(800, 700)
window.bgcolor("black")
window.title("Snake Game 🐍")
window.tracer(0)

score = Score()

def loss():
    global game_on
    if sam.check_if_snake_body() or sam.check_if_wall():
        score.end_message()
        game_on = False
        window.bgcolor("black")
        sam.delete()
        food.delete()


def start_menu():
    return window.textinput("Please choose an action:", "1- Play another round\n2- Reset the game and play new round\nAny other key to EXIT")

def sub_game():
    global game_on
    game_on = True
    window.listen()
    window.onkey(sam.up, "w")
    window.onkey(sam.down, "s")
    window.onkey(sam.left, "a")
    window.onkey(sam.right, "d")
    
    while game_on:
        if sam.head.distance(food) < 20:
            food.aper()
            score.update_score()
            sam.grow()
        window.update()
        time.sleep(0.1)
        sam.move()
        loss()
        

def reset_game():
    score.score = 0
    score.clear()
    score.write_score()
    global sam,food
    sam = Snake()
    food = Food()
    window.update()

def game():
    while True:
        user_menu_choice = start_menu()
        if user_menu_choice == "1":
            reset_game()
            sub_game()        
        elif user_menu_choice == "2":
            open("High Score.txt","w").write("0")
            score.highScore = 0
            reset_game()
            sub_game()
        else:
            break

game()

