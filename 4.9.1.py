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

for i in range(5):
    draw_squares(mint, 20)
    mint.penup()
    mint.forward(40)
    mint.pendown()

wn.mainloop()
