import turtle 

def draw_star(t, l):
    """Make turtle t draw a star whose length of each side is 100 units"""
    for i in range(5):
        t.forward(l)
        t.right(144)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
mint = turtle.Turtle()
mint.pensize(3)

for i in range(5):
    draw_star(mint, 100)
    mint.penup()
    mint.forward(350)
    mint.right(144)
    mint.pendown()

wn.mainloop()

#There are 6 stars if we donot pick up the pen. 
