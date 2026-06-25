import turtle
import random

screen = turtle.Screen()
screen.bgcolor("pink")
screen.setup(600, 600)

t = turtle.Turtle()
t.pensize(100)
t.pencolor("lightblue")
t.circle(90)

colors = ["red", "yellow", "blue", "lightgreen", "purple", "white", "lavender"]

for i in range(30):
    t.forward(15)
    t.left(15)

    t.pendown()
    t.pensize(5)
    t.pencolor(random.choice(colors))
    t.forward(10)
    t.penup()

turtle.done()


