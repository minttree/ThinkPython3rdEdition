import turtle 

def spiral (t, n, d):
    """Make turtle t draw a spiral"""
    size = 7
    for i in range(n):
        t.forward(-size)
        t.left(d)
        t.forward(size)
        t.left(d)
        size = size + 7

wn = turtle.Screen()
wn.bgcolor("lightgreen")

mint = turtle.Turtle()
mint.speed(1)

spiral(mint, 31, 92)
#use the parameter d = 90 to get the first spiral

wn.mainloop()
