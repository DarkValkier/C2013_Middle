import turtle
import random

def draw_rectangle(a, b, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.end_fill()


turtle.reset()
window = turtle.Screen()
turtle.shape('turtle')
turtle.pensize(3)
turtle.speed(10)

for i in range(8):
    draw_rectangle(300, 100, random.choice(['blue', 'red', 'green', 'yellow']))
    turtle.left(45)


window.exitonclick()