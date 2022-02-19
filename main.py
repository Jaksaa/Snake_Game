from screen import Screen_Settings
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen_Settings()
screen.settings()

display = Screen()
snake = Snake()
food = Food()
score = Scoreboard()

display.listen()
display.tracer(0)
display.onkey(snake.up, "Up")
display.onkey(snake.down, "Down")
display.onkey(snake.left, "Left")
display.onkey(snake.right, "Right")

is_on = True

while is_on:
    display.update()
    time.sleep(0.1)
    snake.snake_move()
    score.tracking_score()
    if snake.direction.distance(food) < 15:
        food.another_food()
        score.eat_dot += 1
        if score.eat_dot > 0:
            snake.snake_grow()
    if snake.direction.xcor() > 300 or snake.direction.xcor() < -300 or snake.direction.ycor() > 300 or snake.direction.ycor() < -300:
        score.reset()
        snake.snake_reset()
        display.clearscreen()
        screen.settings()
        score.tracking_score()
    for x in snake.square_list[1:]:
        if snake.direction.distance(x) < 10:
            is_on = False
            score.reset()
            display.clearscreen()
            screen.settings()
            score.tracking_score()

display.exitonclick()















display.exitonclick()