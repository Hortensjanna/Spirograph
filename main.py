from turtle import Turtle, Screen
import random

colours = ['gold', 'hotpink', 'orchid1', 'yellow', 'springgreen3', 'cornflowerblue', 'slateblue3', 'purple4']
angles = [0, 90, 180, 270]
tim = Turtle()
tim.speed('fastest')


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random.choice(colours))
        tim.circle(100)
        tim.right(size_of_gap)

draw_spirograph(7)


screen = Screen()
screen.screensize(100,100)
screen.exitonclick()