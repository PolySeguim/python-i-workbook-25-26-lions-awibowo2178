import turtle

# Create a turtle object - complex data type
geoff = turtle.Turtle()
geoff.color("blue")
geoff.shape("turtle")

#Screen is a complex data type - has attributes and behaviors
screen = turtle.Screen()
screen.title

# Move the turtle forward by 100 units
# does not return a value but performs an action
def foward100():
    geoff.forward(100)

# Turn the turtle to the right by 90 degrees
def right90():
    geoff.right(90)

def circle():
    geoff.circle(50)

def square():
    for i in range(4):
        geoff.forward(100)
        geoff.right(90)

def pentagon():
    for i in range(5):
        geoff.forward(100)
        geoff.right(72)

def rainbow():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for color in colors:
        geoff.color(color)
        geoff.forward(10)
        geoff.circle(20)
        geoff.forward(10)

def backForth():
    geoff.speed(1)
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for color in colors:
        geoff.color(color)
        geoff.pensize(4)
        geoff.forward(100)
        geoff.forward(-50)

def funActivity():
    size = 20
    for i in range(30):
        geoff.stamp()
        size = size + 3
        geoff.penup()
        geoff.forward(size)
        geoff.pendown()
        geoff.right(24)

def pythonTurtles():
    for i in range(10): # for 1000 times, I would switch the 10 to 1000. i just don't want to print it that many times
        print("We like Python's turtles!")

def months():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    for month in months:
        print("One of the months of the year is " + month)

def iterationExercise():
    xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
    sum = 0
    product = 1
    for number in xs:
        sum = sum + number
        product = product * number
        print(number, " -- ", number**2)
        print(sum, product)



#screen.onkey(square, "k")
#screen.onkey(pentagon, "l")
#screen.onkey(foward100, "Up")
#screen.onkey(right90, "Right")
#screen.onkeypress(circle, "Left")
#screen.listen()
#screen.mainloop()
#rainbow()
#backForth()
#funActivity()
#pythonTurtles()
#months()
iterationExercise()


# Keep the window open until clicked
turtle.done()

