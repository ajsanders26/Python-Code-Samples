# Aaron Sanders
# 07/30/2025

# Asks user parameters to draw a regular polygon using the turtle library

import turtle

window = turtle.Screen()
turt = turtle.Turtle()

# User input
sides = int(input("How many sides for the polygon? "))
length = int(input("What is the length of each side? "))
color_line = str(input("What is the color of the line? "))
color_fill = str(input("What is the color of the fill? "))

# Set pen and fill color, begin fill
turt.pensize(2)
turt.color(color_line, color_fill)
turt.begin_fill()

# Draw regular polygon
angle = 360 / sides
for i in range(sides):
    turt.forward(length)
    turt.left(angle)

turt.end_fill()

window.exitonclick()
    
