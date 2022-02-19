from turtle import Turtle

class Snake():
    def __init__(self):
        self.square_list = []
        self.snake()
        self.direction = self.square_list[0]

    def snake(self):
        for i in range(3):
            square = Turtle(shape="square")
            square.up()
            square.goto(x=-20 * i, y=0)
            square.color("white")
            self.square_list.append(square)

    def snake_grow(self):
        square = Turtle(shape="square")
        square.up()
        eaten_pos = self.square_list[-1].position()
        square.goto(eaten_pos)
        square.color("white")
        self.square_list.append(square)

    def snake_reset(self):
        for square in self.square_list:
            square.goto(1000,1000)
        self.square_list.clear()
        self.snake()
        self.direction = self.square_list[0]

    def snake_move(self):
        for num in range(len(self.square_list) - 1, 0, -1):
            new_x = self.square_list[num - 1].xcor()
            new_y = self.square_list[num - 1].ycor()
            self.square_list[num].goto(new_x, new_y)
        self.direction.fd(20)

    def up(self):
        if self.direction.heading() != 270:
            self.direction.setheading(90)

    def down(self):
        if self.direction.heading() != 90:
            self.direction.setheading(270)

    def right(self):
        if self.direction.heading() != 180:
            self.direction.setheading(0)

    def left(self):
        if self.direction.heading() != 0:
            self.direction.setheading(180)


