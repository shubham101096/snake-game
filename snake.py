from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        for i in range(3):
            self.add_segment((-20*i, 0))
        self.head = self.segments[0]

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        for i in range(3):
            self.add_segment((-20*i, 0))
        self.head = self.segments[0]

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        # self.head.setheading(90)
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        segment = Turtle(shape="square", )
        segment.color("white")
        segment.penup()
        segment.setposition(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
