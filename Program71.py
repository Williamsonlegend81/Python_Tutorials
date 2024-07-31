import time

def time_tracker(func):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        func(*args,**kwargs)
        t2 = time.time()-t1
        print(f"{func.__name__} time to execute {t2}")
    return wrapper
@time_tracker
def Addition(a,b):
    print(f"Addition of {a} and {b} is {a+b}")
@time_tracker
def Subtraction(a,b):
    print(f"Subtraction of {a} and {b} is {a-b}")
@time_tracker
def Multiplication(a,b):
    print(f"Multiplication of {a} and {b} is {a*b}")
@time_tracker
def Divison(a,b):
    print(f"Divison of {a} and {b} is {a/b}")

Addition(7,8)
Subtraction(3,9)
Multiplication(6,9)
Divison(6,26)
