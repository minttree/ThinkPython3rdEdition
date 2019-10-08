def is_rightangled(a,b,c):
    if abs(a*a + b*b - c*c) < 0.00001:
        print(True)
    else:
        print(False)

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
is_rightangled(a,b,c)

