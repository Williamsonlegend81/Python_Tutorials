def Average(a,b,c=1):
    print("Print the average is",(a+b+c)/2)

# Average(b=9)
Average(a=5,b=7)
# Average(4,10)

def Name(fname, mname="John", lname="Watson"):
    print("Hello",fname,mname,lname)

# Name("Amy",mname="Virender",lname="Agarwal")
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    return sum/len(numbers)

# return will take the value of average(parameters)
c = average(10,20,30,40)
print(c)
# average(5,9,10,20,40,100,3,7,2,5,6,512)
def name(**name):
    print(type(name))
    print("Hello,", name["fname"],name["mname"],name["lname"])

name(fname = "Girish", mname = "Moolchandbhai", lname = "Patel")