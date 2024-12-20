from colorgram import *
import turtle as turtle_module
import random

extracted_colors = colorgram.extract('hirst_painting.PNG', 10)


colors = []


for color in extracted_colors:
    one_color = (color.rgb.r, color.rgb.g, color.rgb.b)
    colors.append(one_color)


screen = turtle_module.Screen()
screen.screensize(600, 600)

turtle_module.colormode(255)
t = turtle_module.Turtle()
t.hideturtle()
t.penup()
t.goto(-300, -300)

def draw_line():
    while t.xcor() < 300:
        t.dot(20, random.choice(colors))
        t.forward(50)


while t.xcor() < 300 and t.ycor() < 300:
    t.dot(20, random.choice(colors))
    t.forward(50)
    if t.xcor() == 300:
        t.goto(-300, t.ycor()+50)



screen.exitonclick()












