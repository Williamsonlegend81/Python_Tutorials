num = int(input("Enter your number:"))
if (num<0):
    print("Number is negative")
elif(num>0):
    if (num<10):
        print("Number is located between 1-10 range")
    elif(num>10 and num<20):
        print("Number is present between 10-20 range")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")