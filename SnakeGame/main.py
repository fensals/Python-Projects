from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Create a screen object
screen = Screen()
# set up the screen width and height
screen.setup(width=600, height=600)
# change te screen background color
screen.bgcolor("black")
# set title to appear on screen
screen.title("HUNGRY RATTLESNAKE")
# set screen to turn off tracer as snake moves
screen.tracer(0)

# Step 1: Create a snake body (consisting of 3 squares lined up side by side)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()

game_is_on = True

while game_is_on:
    # this makes the screen update its visual every 0.1 secs
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect when the snake 'eats' food
    if snake.head.distance(food) < 15:
        food.food_refresh()
        snake.extend()
        scoreboard.score_increase()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# set screen to not disappear until it is clicked on
screen.exitonclick()
