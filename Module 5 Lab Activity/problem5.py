# Aaron Sanders
# 07/30/2025

# Mimic Ulam Spiral using turtle library

import math
import turtle

window = turtle.Screen()
window.bgcolor("#424242")

turt = turtle.Turtle()
turt.speed(0)

# Welcome
print("""

""")

# User input
radius = int(input("What is the radius of your spiral? "))
rotations = int(input("How many rotations do you wish to have? "))
steps = int(input("How many numbers do you wish to count to? "))

# Set prime and non-prime colors
color_line = "#101010"
color_prime = "red"

turt.pencolor(color_line)

# Spiral constants
angle_max = 2 * math.pi * rotations
radius_per_rad = radius / angle_max

turt.pensize(radius / rotations * 0.4)

for i in range(steps + 1):
    # Checks if i is prime, changes to prime color when found
    if i > 1:
        turt.pencolor(color_prime)
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0: # Checks divisibility from previous numbers
                turt.pencolor(color_line)
                break

    # Calculate new position for turtle
    angle = angle_max * i / steps
    r = radius_per_rad * angle # Current radius of spiral
    x = r * math.cos(angle)
    y = r * math.sin(angle)

    turt.goto(x, y)

window.exitonclick()

