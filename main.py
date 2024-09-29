from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

window = Screen()
window.setup(800, 700)
window.bgcolor("black")
window.title("Snake Game 🐍")
window.tracer(0)


def loss():
    global game_on
    if sam.check_if_snake_body() or sam.check_if_wall():
        writer = Turtle()
        writer.hideturtle()
        writer.color("white")
        window.bgcolor("red")
        writer.write("You lost🤭", font=("boulder", 26, "normal"), align="center")
        time.sleep(2)
        game_on = False
        window.bgcolor("black")
        writer.clear()
        sam.delete()
        food.delete()

high_score = 0
score = 0
pen = Turtle()
pen.color("white")
pen.penup()
pen.goto(0, 300)
pen.hideturtle()
pen.write(f"Score: {score}  High score: {high_score}", font=("boulder", 26, "normal"), align="center")

def score_update():
    global score, high_score
    score += 1
    if score > high_score:
        high_score = score
    pen.clear()
    pen.write(f"Score: {score}  High score: {high_score}", font=("boulder", 26, "normal"), align="center")

def start_menu():
    if not high_score:
        user_menu_choice = window.textinput("Please choose an action:", "1- Start new game\nAny other key to EXIT")
    else:
        user_menu_choice = window.textinput("Please choose an action:", "1- Start new game\n2- Play another round\nAny other key to EXIT")
    return user_menu_choice

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
            score_update()
            sam.grow()
        window.update()
        time.sleep(0.1)
        sam.move()
        loss()
        

def reset_game():
    global score
    score = 0
    pen.clear()
    pen.write(f"Score: {score}  High score: {high_score}", font=("boulder", 26, "normal"), align="center")
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
            reset_game()
            sub_game()
        else:
            break

game()

