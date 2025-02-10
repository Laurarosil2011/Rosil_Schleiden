import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Shape Generator")
screen.bgcolor("black") # This is for the background color

# Create turtle object
pen = turtle.Turtle() 
pen.speed(5) # for the speed
pen.pensize(2) # for the size

# Shape drawer function
def draw_shape(sides, size):
    angle = 360 / sides    # Internal angle of a regular polygon with a given number of sides
    for _ in range(sides):
        pen.forward(size)
        pen.right(angle)

# Main loop to keep asking for shapes
shapes = {
    "triangle": 3,
    "square": 4,
    "pentagon": 5,
    "hexagon": 6
}

while True:
    shape = screen.textinput("Shape Input", "Enter shape (triangle, square, pentagon, hexagon or 'exit' to quit):")

    if shape is None or shape.lower() == "exit":
        break  # To exit loop immediately

    shape = shape.lower()
    if shape in shapes:
        pen.clear()  # Clear previous shape
        pen.color("blue") 
        draw_shape(shapes[shape], 100)
    else:
        screen.textinput("Error", "Invalid shape. Press OK to retry.") # In case of errors in typing the desired shape
 
# Finish
pen.hideturtle() # To make the turtle object invisible
screen.mainloop()
