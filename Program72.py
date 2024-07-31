import time
def time_tracker(func):
    def wrapper(*args):
        t1 = time.time()
        func(*args)
        t2 = time.time()-t1
        print(f"Time taken to execute {func.__name__} is {t2}")
    return wrapper

@time_tracker
def Average(*numbers):
    sum = 0
    for number in numbers:
        sum = sum+number
    avg = sum/len(numbers)
    print(f"Average of numbers is {avg}")
    time.sleep(1)

Average(10,20,30,40,50,60,70,80,90,100)