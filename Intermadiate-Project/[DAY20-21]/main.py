from turtle import Screen
from SnakeOOP import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()  # create a screen object
screen.setup(width=600, height=600)  # set the window size
screen.bgcolor("black")  # set the background color
screen.title("My Snake Game")  # set the window title
screen.tracer(0)  # turn off the screen updates

snake = Snake()  # create a snake object
food = Food()
scoreboard = Scoreboard()

screen.listen()  # listen for key presses
screen.onkey(snake.up, "Up")  # bind the up arrow to the snake.up method
screen.onkey(snake.down, "Down")  # bind the down arrow to the snake.down method
screen.onkey(snake.left, "Left")  # bind the left arrow to the snake.left method
screen.onkey(snake.right, "Right")  # bind the right arrow to the snake.right method

game_is_on = True  # set the game_is_on variable to True

while game_is_on:  # while the game is on
	screen.update()  # update the screen
	time.sleep(0.1)  # wait 0.1 seconds
	snake.move()  # move the snake

	# Detect collision with food
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		scoreboard.increase_score()

	# Detect collision with wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		scoreboard.reset()
		snake.reset()
	# Detect collision with tail
	# If head collides with tail, game over
	for segment in snake.segments[1:]:
		if segment == snake.head:
			continue
		elif snake.head.distance(segment) < 10:
			scoreboard.reset()
			snake.reset()

screen.exitonclick()  # wait for a mouse click before closing the window

