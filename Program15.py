# Match case program
x = int(input("Enter a number:"))
match x:
    case 0:
        print("Your number is zero")
    case 4:
        print("Your number is four")
    case _ if (x!=90):
        print(x,"x is not 90")
    case _ if(x!=80):
        print(x, "x is not 80")
# case _: is for default case