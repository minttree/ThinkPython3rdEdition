import turtle 
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.shape("turtle")
tess.penup()
tess.stamp()

for i in range(12):
    tess.forward(90)
    tess.pendown()
    tess.forward(10)
    tess.penup()  
    tess.forward(20)
    tess.stamp()    
    tess.forward(-120)
    tess.right(30)
      

wn.mainloop()
