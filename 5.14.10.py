def find_hypot (a, b):
    """Find hypotenuse of a right-angled triangle whose lengths a and b"""
    print("The length of the hypotenuse is ", (a*a+b*b)**0.5)

x = float(input("One side is: "))
y = float(input("Other side is: "))
find_hypot(x,y) 
