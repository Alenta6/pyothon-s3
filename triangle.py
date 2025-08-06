import turtle
screen = turtle.Screen()
screen.bgcolor("blue")
t = turtle.Turtle()
t.pensize(10)
t.pencolor("black")
t.speed(100)
def draw_triangle(size,x,y):
    t.penup()
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    for _ in range(3):
        t.forward(size)
        t.left(120)
sizes = [80,130,200]
x=-150
y=0
for size in sizes:
    draw_triangle(size,x,y)
    x += size +20
turtle.done()