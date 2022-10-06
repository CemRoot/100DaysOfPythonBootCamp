from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
	def __init__(self):
		self.turtle = Turtle()
		self.turtle.penup()
		self.turtle.shape("turtle")
		self.turtle.color("black")
		self.turtle.left(90)
		self.turtle.setposition(STARTING_POSITION)

	def go_up(self):
		self.turtle.sety(self.turtle.ycor() + MOVE_DISTANCE)
		if self.turtle.ycor() > FINISH_LINE_Y:
			self.turtle.sety(FINISH_LINE_Y)

	def go_to_start(self):
		self.turtle.goto(STARTING_POSITION)

	def is_at_finish_line(self):
		if self.turtle.ycor() >= FINISH_LINE_Y:
			return True
		else:
			return False
