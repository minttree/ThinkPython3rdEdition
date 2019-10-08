def mark(a):
    """Give grade of mark:"""
    if a >=75:
        print(a, "First")
    elif a>=70 and a<75:
        print(a, "Upper Second")
    elif a>=60 and a<70:
        print(a, "Second")
    elif a>=50 and a<60:
        print(a, "Third")
    elif a>=45 and a<50:
        print(a, "F1 Supp")
    elif a>=40 and a<45:
        print(a, "F2")
    else:
        print(a, "F3")

xs = [83,75,74.9,70,69.9,65,60,59.9,55,50,49.9,45,44.9,40,39.9,2,0]

for i in xs:
    mark(i)
