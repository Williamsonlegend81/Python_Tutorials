import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds}")
    time.sleep(seconds)
    return seconds

# time1 = time.perf_counter()
# func(4)
# func(2)
# func(1)
# time2 = time.perf_counter()
# print(time2-time1)

# Same code using threads
time1 = time.perf_counter()
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
time2 = time.perf_counter()
print(time2-time1)

def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # future = executor.submit(func,3)
        # future = executor.submit(func,2)
        # future = executor.submit(func,1)
        # print(future.result())
        # print(future.result())
        # print(future.result())
        l = [3,5,1,2]
        results = executor.map(func,l)
        for result in results:
            print(result)

poolingDemo()
