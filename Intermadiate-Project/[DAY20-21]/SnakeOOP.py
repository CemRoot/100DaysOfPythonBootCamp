from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # (x, y)
MOVE_DISTANCE = 20  # pixels
UP = 90  # degrees
DOWN = 270  # degrees
LEFT = 180  # degrees
RIGHT = 0  # degrees


class Snake:
    """"""

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the snake"""
        for position in STARTING_POSITIONS:  # for each position in the starting positions
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")  # create a new segment
        new_segment.color("white")  # set the color of the segment
        new_segment.penup()  # set the segment to be penup
        new_segment.goto(position)  # move the segment to the position
        self.segments.append(new_segment)  # add the segment to the snake's segments
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # move the head
        for seg_num in range(len(self.segments) - 1, 0, -1):  # for each segment in the snake
            new_x = self.segments[seg_num - 1].xcor()  # get the x coordinate of the segment
            new_y = self.segments[seg_num - 1].ycor()  # get the y coordinate of the segment
            self.segments[seg_num].goto(new_x, new_y)  # move the segment to the previous segment's coordinates
        self.head.forward(MOVE_DISTANCE)  # move the head forward

    def up(self):
        # up is the same as down but with a 270-degree turn
        if self.head.heading() != DOWN:  # if the head is not facing down
            self.head.setheading(UP)  # set the head to face up

    def down(self):
        # down is the same as up but with a 90-degree turn
        if self.head.heading() != UP:  # if the head is not facing up
            self.head.setheading(DOWN)  # set the head to face down

    def left(self):
        # left is the same as right but with a 180-degree turn
        if self.head.heading() != RIGHT:  # if the head is not facing right
            self.head.setheading(LEFT)  # set the head to face left

    def right(self):
        # right is the same as left but with a 0-degree turn
        if self.head.heading() != LEFT:  # if the head is not facing left
            self.head.setheading(RIGHT)  # set the head to face right

