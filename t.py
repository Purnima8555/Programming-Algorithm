# import turtle
# b=turtle.Screen()
# t=turtle.Turtle()
# turtle.mainloop()

## done=mainloop

# import turtle
# # help(turtle.shape)
# t=turtle.Turtle()
# t.shape("turtle")
# turtle.done()

# import turtle
# # help(turtle.shape)
# t=turtle.Turtle()
# t.shape("turtle")
# # if there is one color then, both the line and turtle will be same color
# # t.color("red")
# # if there are 2 colors then, the first color will be line and second one will be the color of the turtle
# t.color("black","green")
# t.forward(100)
# turtle.done()

# import turtle
# sc=turtle.Screen()
# sc.bgcolor("green")
# sc.title("Turtle")
# t=turtle.Turtle()
# t.shape("turtle")
# t.color("red", "green")
# t.forward(100)
# turtle.done()

# import turtle
# # Creating turtle screen
# t=turtle.Turtle()
# turtle.bgcolor("red")
# turtle.mainloop()

# from turtle import *
# a=Turtle()
# screensize(1500, 1500)
# mainloop()

# # Changing pen sze:
# import turtle
# t=turtle.Turtle()
# t.pensize(4)
# t.forward(200)
# turtle.mainloop()

# # Changing pen speed:
# import turtle
# t=turtle.Turtle()
# t.speed(3)
# t.forward(100)
# t.speed(7)
# t.forward(100)
# turtle.mainloop()

# # To hide/clear lines in turtle
# import turtle
# t=turtle.Turtle()
# t.speed(3)
# t.forward(100)
# t.speed(7)
# t.forward(100)
# t.clear()
# turtle.mainloop()

# # Forward:
# import turtle
# t=turtle.Turtle()
# t.forward(100)
# turtle.mainloop()

# # Backward:
# import turtle
# t=turtle.Turtle()
# t.backward(100)
# turtle.mainloop()

# # Left:
# import turtle
# sc=turtle.Screen()
# t=turtle.Turtle()
# t.left(75)
# t.forward(100)
# turtle.done()

# # Right:
# import turtle
# sc=turtle.Screen()
# t=turtle.Turtle()
# t.right(75)
# t.forward(100)
# turtle.done()

# # To draw square:
# import turtle
# t=turtle.Turtle()
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# turtle.mainloop()

# # To draw square using loop:
# import turtle
# sc=turtle.Screen()
# t=turtle.Turtle()
# for i in range(4):
#     t.fd(50)
#     t.lt(90)
# turtle.done()

# # To draw cicle:
# import turtle
# t=turtle.Turtle()
# t.circle(70)
# turtle.mainloop()

# # To fill color inside the square:
# # And also hide turtle:
# import turtle
# t=turtle.Turtle()
# t.begin_fill()
# t.fillcolor("green")
# for i in range(4):
#     t.forward(50)
#     t.left(90)
# t.end_fill()
# t.hideturtle()
# turtle.done()


# IMPORTANT QUESTIONS:

# # To draw a hexagon using loop:
# import turtle
# t=turtle.Turtle()
# for i in range(6):
#     t.fd(100)
#     t.rt(60)
# turtle.done()

# # To draw pentagon using loop:
# import turtle
# t=turtle.Turtle()
# for i in range(5):
#     t.fd(100)
#     t.rt(72)
# turtle.done()

# # To draw heptagon using loop:
# import turtle
# t=turtle.Turtle()
# for i in range(7):
#     t.fd(100)
#     t.rt(51.42)
# turtle.done()

# # To draw octagon using loop:
# import turtle
# t=turtle.Turtle()
# for i in range(8):
#     t.fd(100)
#     t.rt(45)
# turtle.done()

# # To draw naogon using loop:
# import turtle
# t=turtle.Turtle()
# for i in range(9):
#     t.fd(100)
#     t.rt(40)
# turtle.done()

# # To draw decagon using loop:
# import turtle
# t=turtle.Turtle()
# for i in range(10):
#     t.fd(100)
#     t.rt(36)
# turtle.done()

# # To make a dot:
# import turtle
# t=turtle.Turtle()
# t.dot(100)
# turtle.mainloop()


# # To draw shape from different position:
# import turtle
# t=turtle.Turtle()
# t.up()
# t.goto(0,-100)
# t.down()
# t.circle(100)
# turtle.done()


# # To set the orientation of the turtle to an angle:
# # 0-east
# # 90-north
# # 180-west
# # 270-south

# import turtle

# turtle.seth(0)
# turtle.forward(80)
# turtle.write("East")

# turtle.home()

# turtle.setheading(90)
# turtle.forward(80)
# turtle.write("North")

# turtle.home()

# turtle.seth(180)
# turtle.forward(80)
# turtle.write("West")

# turtle.home()

# turtle.setheading(270)
# turtle.forward(80)
# turtle.write("South")

# turtle.ht()
# turtle.done()


# # Designs using turtle:
# import turtle
# t=turtle.Turtle()

# turtle.bgcolor("black")
# turtle.pensize(2)
# turtle.speed(0)

# while(True):
#     for i in range(6):
#         for colors in["red", "blue", "magenta", "green", "yellow", "white"]:
#             turtle.color(colors)
#             turtle.circle(100)
#             turtle.left(10)
#     # turtle.hideturtle()
#     turtle.done()       


# # Implementation of methods:
# import turtle
# sc=turtle.Screen()

# sc.bgcolor('cyan')
# sc.title("Turtle example")

# t=turtle.Turtle()
# t.shape("turtle")
# t.shapesize(4)
# t.width(10)
# t.speed(5)
# t.color("red")
# t.fillcolor("yellow")

# t.forward(100)
# t.penup()
# t.forward(50)
# t.down()
# t.pendown()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

# turtle.done()
# sc.exitonclick()