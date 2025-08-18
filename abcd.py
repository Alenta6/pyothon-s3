import turtle
wn = turtle.Screen()
wn.bgcolor("purple")
wn.title("My turtle Square")
my_turtle = turtle.Turtle()
my_turtle.fillcolor("white")
my_turtle.pencolor("white")
my_turtle.pensize(8)

my_turtle.begin_fill()
for _ in range(3):
   my_turtle.forward(100)
   my_turtle.right(-120)
my_turtle.end_fill()
turtle.done()