#snake_game
import time
import random
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
total_score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    time.sleep(0.1)
    if snake.snake_position():
        total_score.game_over()
        game_is_on = False
    if snake.head.distance(food) < 15:
        food_shape = ["classic", "arrow", "turtle", "circle", "square", "triangle"]
        food.shape(random.choice(food_shape))
        food_color = ["blue", "lime", "yellow", "dark orange", "red", "magenta", "indigo", "green"]
        food.color(random.choice(food_color))
        food_head = [0, 90, 180, 270]
        food.setheading(random.choice(food_head))
        food.refresh()
        snake.snake_extend()
        total_score.increase_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            total_score.game_over()
            game_is_on = False


screen.exitonclick()
