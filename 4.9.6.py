import turtle 

def draw_poly (t, n, sz):
    """Make turtle t draw a polygon n sides, 
    each size sz units."""    
        
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

def draw_equitriangle(t, sz):
    """Make turtle t draw an equilateral triangle"""
    draw_poly(t, 3, sz)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

mint = turtle.Turtle()
mint.pensize(3)

draw_equitriangle(mint, 100)

wn.mainloop()
