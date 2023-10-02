from turtle import Turtle, Screen
import datetime

# Create the window
window = Screen()
window.title("Analog Clock")
window.bgcolor("white")
window.setup(width=1000, height=800)

# Create the outer circle
circle = Turtle()
circle.penup()
circle.pencolor("black")
circle.speed(0)
circle.pensize(5)
circle.hideturtle()
circle.goto(0, -390)
circle.pendown()
circle.fillcolor("white")
circle.begin_fill()
circle.circle(400)
circle.end_fill()

# Create hour hand
hHand = Turtle()
hHand.shape("arrow")
hHand.color("red")
hHand.speed(10)
hHand.shapesize(stretch_wid=0.4, stretch_len=18)

# Create minute hand
mHand = Turtle()
mHand.shape("arrow")
mHand.color("dark red")
mHand.speed(10)
mHand.shapesize(stretch_wid=0.4, stretch_len=26)

# Create second hand
sHand = Turtle()
sHand.shape("arrow")
sHand.color("black")
sHand.speed(10)
sHand.shapesize(stretch_wid=0.4, stretch_len=36)

# Create center circle
centerCircle = Turtle()
centerCircle.shape("circle")
centerCircle.color("white")
centerCircle.shapesize(stretch_wid=1.5, stretch_len=1.5)

# Create the pen for drawing numbers and dots
pen = Turtle()
pen.speed(0)
pen.color("black")

# Function to draw a dot on top of a number
def drawDot(x, y, color):
    """
    Draw a dot on top of a number.

    Args:
        x (int): X-coordinate of the number.
        y (int): Y-coordinate of the number.
        color (str): Color of the dot.
    """
    pen.penup()
    pen.goto(x, y + 45)  # Adjust the Y-coordinate to place the dot higher above the number
    pen.dot(30, color)   # Draw a  dot using the pen turtle

# Draw numbers and dots on top of numbers
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
positions = [(170, 260), (300, 140), (340, -30), (300, -200), (170, -325), (0, -370),
             (-170, -325), (-300, -200), (-340, -30), (-280, 140), (-160, 260), (0, 300)]

for i, (number, (x, y)) in enumerate(zip(numbers, positions)):
    pen.penup()
    pen.goto(x, y)
    pen.write(number, align="center", font=("Algerian", 20, "bold"))
    if i in {2, 5, 8, 11}:
        drawDot(x, y, "red")
    else:
        drawDot(x, y, "blue")

# Hide the pen turtle
pen.hideturtle()

# Writing "CDU" below 12
pen.penup()
pen.goto(0, 260)  # Adjust the Y-coordinate to position the text below 12
pen.color("red")  # Set the text color to red
pen.write("CDU", align="center", font=("Algerian", 20))

# function to move the hour hand
def movehHand():
    """
    Update the position of the hour hand.
    """
    currentHourInternal = datetime.datetime.now().hour
    degree = (currentHourInternal - 15) * -30
    currentMinuteInternal = datetime.datetime.now().minute
    degree = degree + -0.5 * currentMinuteInternal
    hHand.setheading(degree)
    window.ontimer(movehHand, 60000)

# function to move the minute hand
def movemHand():
    """
    Update the position of the minute hand.
    """
    currentMinuteInternal = datetime.datetime.now().minute
    degree = (currentMinuteInternal - 15) * -6
    currentSecondInternal = datetime.datetime.now().second
    degree = degree + (-currentSecondInternal * 0.1)
    mHand.setheading(degree)
    window.ontimer(movemHand, 1000)

#  function to move the second hand
def movesHand():
    """
    Update the position of the second hand.
    """
    currentSecondInternal = datetime.datetime.now().second
    degree = (currentSecondInternal - 15) * -6
    sHand.setheading(degree)
    window.ontimer(movesHand, 1000)

# Start updating the clock hands
window.ontimer(movehHand, 1)
window.ontimer(movemHand, 1)
window.ontimer(movesHand, 1)

# Close the window when clicked
window.exitonclick()
