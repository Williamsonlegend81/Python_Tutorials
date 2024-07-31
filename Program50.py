# def double(x):
#     return x*2
# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum+i
#     return (sum/len(numbers))
def appl(fx,value):
    return 6+fx(value)

double = lambda x: x*2
cube = lambda y: y**3
avg = lambda x,y: (x+y)/2
ans = double(5)
ans2 = cube(10)
ans3 = avg(10,20)
# b = average(10,20,30,40,50)
# print(b)
print(appl(lambda x:x**3,10))
print(ans2)
print(ans)
print(ans3)
x = 10
y = 90
lambda x,y: print(f"The product of {x} and {y} is {x*y}")
