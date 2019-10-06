import turtle 

def draw_poly (t, n, sz):
    """Make turtle t draw a polygon n sides, 
    each size sz units."""    
        
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Pretty pattern")

mint = turtle.Turtle()
mint.pensize(2)
mint.speed(10)

for i in range(20):
    draw_poly (mint, 4, 80)
    mint.left(18)
    mint.hideturtle()

wn.mainloop()
