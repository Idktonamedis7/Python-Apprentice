"""
For this program, you will tell Tina the Turtle to draw a triangle.

You should look at the previous programs to see how to use the turtle commands.
Copy lines of code from those programs to this one to draw a triangle.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast.


# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

tina.pencolor('green')                   # Set the pen color to blue
tina.backward(200)                       # Move tina forward by the forward distance
tina.left(60)                          # Turn tina right a quarter turn

tina.pencolor('red')                    # Set the pen color to red
tina.forward(200)                       # Continue the last two steps three more times
tina.left(60)                          # to draw a square

tina.pencolor('pink')                  # Set the pen color to green
tina.backward(200)
tina.left(60)

turtle.exitonclick()                    # Close the window when we click on it