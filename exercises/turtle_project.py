"""Trees in winter with a cottage and a fire."""
 
__author__ = "730476889"
 
from turtle import Turtle, done 
import turtle


def main() -> None:
    """This is the main function."""
    ertle: Turtle = Turtle()
    ertle.speed("fastest")
    turtle.bgcolor("skyblue")

    draw_house(ertle, 150, -100, 150)

    draw_mountain(ertle, -360, 110, 200)
    draw_mountain(ertle, -280, 110, 250)
    draw_mountain(ertle, -200, 110, 200)
    draw_mountain(ertle, -120, 110, 250)
    draw_mountain(ertle, -40, 110, 200)
    draw_mountain(ertle, 40, 110, 250)
    draw_mountain(ertle, 120, 110, 200)
    draw_mountain(ertle, 200, 110, 250)

    draw_roof(ertle, 150, -100, 150)

    draw_firepit(ertle, 0, -200, 40)

    draw_fire(ertle, 0, -200, 10)
    draw_fire(ertle, 10, -200, 20)
    draw_fire(ertle, 30, -200, 10)

    draw_tree(ertle, -250, -250, 10)
    draw_tree(ertle, -150, -175, 10)
    draw_tree(ertle, -50, -250, 10)

    draw_leaves(ertle, -365, -150, 150)
    draw_leaves(ertle, -260, -75, 150)
    draw_leaves(ertle, -160, -150, 150)

    draw_ground(ertle, -500, -390, 150)

    draw_door(ertle, 250, -240, 30)

    draw_sun(ertle, -275, 300, 150)

    done()


def draw_house(turtle1: Turtle, x: float, y: float, width: float) -> None:
    """This function is creating the base of the house."""
    turtle1.penup()
    turtle1.goto(x, y) 
    turtle1.setheading(0.0)
    turtle1.pendown()
    turtle1.color("black", "dark red")
    turtle1.begin_fill()
    
    i: int = 0
    while i < 4:
        turtle1.forward(width)
        turtle1.right(90)
        i = i + 1
    turtle1.end_fill()


def draw_mountain(turtle1: Turtle, x: float, y: float, width: float) -> None:
    """This function is creating the mountains in the back."""
    turtle1.penup()
    turtle1.goto(x, y) 
    turtle1.setheading(60.0)
    turtle1.pendown()
    turtle1.color("lightblue", "blue")
    turtle1.begin_fill()

    i: int = 0
    while i < 3:
        turtle1.forward(width)
        turtle1.right(120)
        i = i + 1
    turtle1.end_fill()
    
    
def draw_roof(turtle1: Turtle, x: float, y: float, width: float) -> None:
    """This function is creating the roof of the house."""
    turtle1.end_fill()
    turtle1.penup()
    turtle1.goto(x, y) 
    turtle1.setheading(60.0)
    turtle1.pendown()
    turtle1.color("white", "black")
    turtle1.begin_fill()

    i: int = 0
    while i < 3:
        turtle1.forward(width)
        turtle1.right(120)
        i = i + 1
    turtle1.end_fill()
    
        
def draw_firepit(turtle1: Turtle, x: float, y: float, width: float) -> None:
    """This function is creating the fire pit base."""
    turtle1.penup()
    turtle1.goto(x, y) 
    turtle1.setheading(0.0)
    turtle1.pendown()
    turtle1.color("grey", "black")
    turtle1.begin_fill()
   
    i: int = 0
    while i < 4:
        turtle1.forward(width)
        turtle1.right(90)
        i = i + 1
    turtle1.end_fill()
    

def draw_fire(turtle1: Turtle, x: float, y: float, width: float) -> None:
    """This function is creating the fire in the firepit."""
    turtle1.penup()
    turtle1.goto(x, y) 
    turtle1.setheading(60.0)
    turtle1.pendown()
    turtle1.color("red", "orange")
    turtle1.begin_fill()
    
    i: int = 0
    while i < 3:
        turtle1.forward(width)
        turtle1.right(120)
        i = i + 1
    turtle1.end_fill()


def draw_tree(turtle1: Turtle, x: float, y: float, width: float) -> None:
    """This function is creating the base of the tree."""
    turtle1.penup()
    turtle1.goto(x, y) 
    turtle1.setheading(90.0)
    turtle1.pendown()
    turtle1.color("black", "brown")
    turtle1.begin_fill()
    
    i: int = 0
    while i < 1:
        turtle1.forward(150)
        turtle1.left(90)
        turtle1.forward(75)
        turtle1.left(90)
        turtle1.forward(150)
        turtle1.left(90)
        turtle1.forward(75)
        i = i + 1
    turtle1.end_fill()
   

def draw_leaves(turtle1: Turtle, x: float, y: float, width: float) -> None:
    """This function is creating the leaves on the tree."""
    turtle1.penup()
    turtle1.goto(x, y) 
    turtle1.setheading(60.0)
    turtle1.pendown()
    turtle1.color("darkgreen", "green")
    turtle1.begin_fill()
   
    i: int = 0
    while i < 3:
        turtle1.forward(width)
        turtle1.right(120)
        i = i + 1
    turtle1.end_fill()


def draw_ground(turtle1: Turtle, x: float, y: float, width: float) -> None:
    """This function is creating the ground."""
    turtle1.penup()
    turtle1.goto(x, y) 
    turtle1.setheading(0.0)
    turtle1.pendown()
    turtle1.color("black", "grey")
    turtle1.begin_fill()
     
    i: int = 0
    while i < 1:
        turtle1.forward(1000)
        turtle1.left(90)
        turtle1.forward(150)
        turtle1.left(90)
        turtle1.forward(1000)
        turtle1.left(90)
        turtle1.forward(150)
        i = i + 1
    turtle1.end_fill()


def draw_door(turtle1: Turtle, x: float, y: float, width: float) -> None:
    """This function is creating the door to the house."""
    turtle1.penup()
    turtle1.goto(x, y) 
    turtle1.setheading(90.0)
    turtle1.pendown()
    turtle1.color("black", "brown")
    turtle1.begin_fill()
    
    i: int = 0
    while i < 1:
        turtle1.forward(100)
        turtle1.left(90)
        turtle1.forward(50)
        turtle1.left(90)
        turtle1.forward(100)
        turtle1.left(90)
        turtle1.forward(50)
        i = i + 1
    turtle1.end_fill()


def draw_sun(turtle1: Turtle, x: float, y: float, width: float) -> None:
    """This function is creating the sun."""
    turtle1.penup()
    turtle1.goto(x, y)
    turtle1.setheading(90.0)
    turtle1.pendown()
    turtle1.color("yellow", "yellow")
    turtle1.begin_fill()
    turtle1.circle(50)
    turtle1.end_fill()


if __name__ == "__main__":
    main()
