def day_name(a):
    """Give a day name given the day number from 0 to 6: 
        Sunday to Saturday."""
    if a == 0:
        print("You will return on Sunday.")
    elif a == 1:
        print("You will return on Monday.")
    elif a == 2:
        print("You will return on Tuesday.")
    elif a == 3:
        print("You will return on Wednesday.")
    elif a == 4:
        print("You will return on Thursday.")
    elif a == 5:
        print("You will return on Friday.")
    else:  
        print("You will return on Saturday.")

start = int(input("Please give starting day number: "))
stay = int(input("How many days will you stay? " ))
x = stay%7 + start 
if x >= 7:
    day_name(x-7)
else:
    day_name(x)
