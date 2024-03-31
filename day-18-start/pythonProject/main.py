import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
turtle.colormode(255)

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# for _ in range(4):
#     tim.color = random.choice(["blue", "green", ""])
#     tim.forward(100)
#     tim.right(90)
#
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)
#
# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)
#
# for _ in range(7):
#     tim.forward(100)
#     tim.right(360/7)
#
# for _ in range (8):
#     tim.forward(100)
#     tim.right(45)
#
# for _ in range (9):
#     tim.forward(100)
#     tim.right(40)
#
# for _ in range (10):
#     tim.forward(100)
#     tim.right(36)

# colors = ['red', 'green', 'blue', 'yellow', 'orange']
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for i in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(i)
colors = ['red', 'green', 'blue', 'yellow', 'orange']
kierunek = [0, 90, 180, 270]
tim.pensize(1)
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

# def losowy_walk(kierunek):
#     tim.forward(20)
#     tim.setheading(random.choice(kierunek))
#
# for i in range(200):
#     tim.color(random_color())
#     losowy_walk(kierunek)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        tim.circle(100)

draw_spirograph(5)



screen = Screen()
screen.exitonclick()