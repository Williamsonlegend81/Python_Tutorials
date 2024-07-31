def my_generator():
    for i in range(50):
        yield i

gen = my_generator()
for n in gen:
    print(n)