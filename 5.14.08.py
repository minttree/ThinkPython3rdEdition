import turtle 

def draw_bar(t,height):
    """Get turtle t to draw one bar, of height."""
    t.begin_fill()    
    t.left(90)
    t.forward(height)
    t.right(90)
    t.write("    " + str(height))
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("lightgreen")


mint = turtle.Turtle()
mint.hideturtle()
mint.speed(0)
mint.pensize(3)


xs = [48,117,200,240,160,260,220]

for v in xs:
    if v >= 200:
        mint.color("black","red")
    elif v>=100 and v<200:
        mint.color("black","yellow")
    else:
        mint.color("black","green")
    draw_bar(mint, v)

alex = turtle.Turtle()
alex.pensize(3)
alex.forward(50*len(xs)+20)

wn.mainloop()

