from turtle import Turtle
class Snake:
    # UP = ["w","W","Up"]
    # DOWN = ["s","S","Down"]
    # LEFT = ["a","A","Left"]
    # RIGHT = ["d","D","Right"]

    def __init__(self):
        self.snake_parts = []
        self.positions = [(-40,0), (-20,0), (0,0)]
        self.create_snake()
        self.head = self.snake_parts[-1]

    def create_snake(self):
        # self.delete()
        for i in range(len(self.positions)):
            new_snake_part = Turtle("square")
            new_snake_part.color("white")
            new_snake_part.penup()
            new_snake_part.goto(self.positions[i])
            self.snake_parts.append(new_snake_part)
        self.snake_parts[-1].color("red")

    def check_if_snake_body(self):
            # headX,headY = self.head.pos()
            # for turtlePart in self.snake_parts[:-1]:
            #     if abs(headX - turtlePart.xcor()) < 15 and abs(headY - turtlePart.ycor()) < 15:
            #         return True
            # return False
            for snakePart in self.snake_parts[:-1]:
                if snakePart.distance(self.head) <15:
                    return True
            return False

    def check_if_wall(self):
            headX,headY = self.head.pos()
            if abs(headX) > 385 or abs(headY) > 330:
                return True
            return False

    def move(self):
        for i in range(len(self.snake_parts) -1):
            self.snake_parts[i].goto(self.snake_parts[i+1].pos())
        self.head.forward(20)

    def grow(self):
        new_snake_part = Turtle("square")
        new_snake_part.color("white")
        new_snake_part.penup()
        new_snake_part.goto(self.snake_parts[0].pos())  # Place it where the tail is
        self.snake_parts.insert(0, new_snake_part)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)    

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def delete(self):
        for snakePart in self.snake_parts:
            snakePart.hideturtle()
        self.snake_parts = []


    

