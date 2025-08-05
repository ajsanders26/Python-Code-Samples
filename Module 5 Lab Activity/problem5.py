# Aaron Sanders
# 07/30/2025

# Mimic Ulam Spiral using turtle library
# Prints segments of a spiral to a specified radius and number of rotations
# Marks each nth segment of the spiral with a different color when n is prime

import math
import turtle

window = turtle.Screen()
window.bgcolor("#424242")

turt = turtle.Turtle()
turt.speed(0)

# Welcome
print("""Welcome to the Ulam Spiral Visualizer!
https://en.wikipedia.org/wiki/Ulam_spiral\n
Here you can set the size of the spiral, number of rotations, and how far to count up to.
The larger the number for the count, the more of the \"pattern\" is apparent.\n
Experiment and see what settings work for you!
(Suggested Settings: 400, 60, >10000... it may take awhile to fully render.)\n\n
""")

# User input
radius = int(input("What is the radius of your spiral?"))
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

