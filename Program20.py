def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
def isLesser(a,b):
    pass
def greaternum(a,b):
    if (a>b):
        print(a,"is greater than",b)
    elif(b>a):
        print(b,"is greater than",a)
    else:
        print("Both are equal")
a = 10
b = 9
calculateGmean(a,b)

c = int(input("Enter a number1:"))
d = int(input("Enter a number2:"))
greaternum(c,d)