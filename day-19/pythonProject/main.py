from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
y_positions = [-70, - 40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winnre!")

        rand_distance= random.randint(0,10)
        turtle.forward(rand_distance)












# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# def clockwise():
#     tim.right(10)
# def counterclockwise():
#     tim.left(10)
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="c", fun=clear_screen)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="a", fun=counterclockwise)



screen.exitonclick()