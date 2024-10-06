import turtle

def koch_curve(turtle_obj, length, depth):
    if depth == 0:
        turtle_obj.forward(length)
    else:
        length /= 3.0
        koch_curve(turtle_obj, length, depth-1)
        turtle_obj.left(60)
        koch_curve(turtle_obj, length, depth-1)
        turtle_obj.right(120)
        koch_curve(turtle_obj, length, depth-1)
        turtle_obj.left(60)
        koch_curve(turtle_obj, length, depth-1)

def koch_snowflake(turtle_obj, length, depth):
    for _ in range(3):
        koch_curve(turtle_obj, length, depth)
        turtle_obj.right(120)

def setup_turtle():
    # Initialize the turtle graphics window
    screen = turtle.Screen()
    screen.setup(width=1000, height=1000)
    screen.bgcolor("black")
    
    turtle_obj = turtle.Turtle()
    turtle_obj.speed(0)
    turtle_obj.penup()
    turtle_obj.goto(-300, 200)
    turtle_obj.pendown()
    turtle_obj.pencolor("white")
    
    return screen, turtle_obj

def main():
    screen, turtle_obj = setup_turtle()
    
    # User input for the recursion depth
    depth = int(input("Enter the level of recursion (e.g., 3): "))
    
    # Draw the Koch snowflake
    koch_snowflake(turtle_obj, 600, depth)
    
    # Hide the turtle and display the window
    turtle_obj.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()