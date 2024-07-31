import time

i=1
t1 = time.time()
while (i<=100000):
    print(i)
    i=i+1
t2 = time.time()-t1

t3 = time.time()
for number in range(1,100001):
    print(number)
t4 = time.time()-t3
print(f"Time taken by while loop {t2}")
print(f"Time taken by for loop {t4}")