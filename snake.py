from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    snake_body = []

    def __init__(self):
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for pos in starting_positions:
            self.add_square(pos)

    def add_square(self, pos):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(pos)
        self.snake_body.append(square)

    def extend(self):
        self.add_square(self.snake_body[-1].position())

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def reset_snake(self):
        for square in self.snake_body:
            square.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
