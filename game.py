import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Shape Generator")
screen.bgcolor("black")

# Create turtle object
pen = turtle.Turtle()
pen.speed(5)
pen.pensize(2)

# Shape drawer function
def draw_shape(sides, size):
    angle = 360 / sides
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
        break

    shape = shape.lower()
    if shape in shapes:
        pen.clear()  # Clear previous shape
        pen.color("blue")
        draw_shape(shapes[shape], 100)
    else:
        screen.textinput("Error", "Invalid shape. Press OK to retry.")

# Finish
pen.hideturtle()
screen.mainloop()
