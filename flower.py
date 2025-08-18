import turtle
def draw_petal(t,radius,angle):
    for _ in range(2):
        t.circle(radius,angle)
        t.left(180 - angle)

num_petals=turtle.numinput("Petals",'enter the number of petals:',default=6,minval=1,maxval=36)
import turtle
wn =turtle.Screen()
g =turtle.Turtle()
g.speed(0)

for _ in range(6):
    draw_petal(g,90,90)
    g.fillcolor("cyan")
    g.left(360/6)
wn.mainloop()