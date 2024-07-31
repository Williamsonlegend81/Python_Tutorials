import time

def time_tracker(func):
    def wrapper():
        t1 = time.time()
        time.sleep(1)
        func()
        t2 = time.time()-t1
        print(f"Time taken to implement these loop is {t2}")
    return wrapper

@time_tracker
def using_while():
    i = 0
    while(i<100):
        i = i+1
    print("While loop implemented")

@time_tracker
def using_for_loop():
    for number in range(100):
        pass
    print("For loop implemented")

using_while()
using_for_loop()
