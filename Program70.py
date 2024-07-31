import time
def time_tracker(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print(f"Time taken to execute the {func.__name__} is {t2}")
    return wrapper
@time_tracker
def func1():
    print("Execution of function 1")
    # time.sleep(1)
@time_tracker
def func2():
    print("Execution of function 2")
    # time.sleep(1)

func1()
func2()