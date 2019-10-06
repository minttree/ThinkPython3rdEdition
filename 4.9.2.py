import turtle 

def draw_squares (t, sz):
    """Make turtle t draw a square of sz."""    
        
    for i in range(4):
        t.forward(sz)
        t.left(90)



wn = turtle.Screen()
wn.bgcolor("lightgreen")

mint = turtle.Turtle()
mint.pensize(3)

size = 20
for i in range(5):
    draw_squares(mint, size)
    mint.forward(size/2)
    mint.penup()    
    mint.right(90)
    mint.forward(10)
    size = size + 20
    mint.right(90)
    mint.forward(size/2)
    mint.right(180)
    mint.pendown()

wn.mainloop()
