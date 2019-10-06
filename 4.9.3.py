import turtle 

def draw_poly (t, n, sz):
    """Make turtle t draw a polygon n sides, 
    each size sz units."""    
        
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

mint = turtle.Turtle()
mint.pensize(3)

draw_poly (mint, 8, 50)

wn.mainloop()
