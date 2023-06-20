import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_circle(size, angle, shift):
    turtle.bgcolor(next(colors))
    turtle.pensize(size // 10)  # Adjust the pensize based on the circle size
    turtle.pencolor(next(colors))
    turtle.circle(size)

    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1)

# Adjust the turtle's pensize
turtle.pensize(40)  # Change the pensize to 40 as desired

# Adjust the background color using shaders
turtle.bgcolor(0, 0, 0)  # Set the initial background color to black

draw_circle(30, 0, 1)

turtle.done()
