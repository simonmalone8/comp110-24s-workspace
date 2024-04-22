"""."""

from turtle import Turtle, colormode, done
colormode(255)
turtle1: Turtle = Turtle()

turtle1.penup()
turtle1.goto(-155, -125)
turtle1.pendown()
turtle1.speed(100)
turtle1.color("red", "blue")

turtle1.begin_fill()
i: int = 0
while (i < 3):
    turtle1.forward(300)
    turtle1.left(120)
    i = i + 1
turtle1.end_fill()
done()