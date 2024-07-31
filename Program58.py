def decorator_function(fx):
    def mfx(*args,**kwargs):
        print("Apka function mei swagat hai")
        fx(*args,**kwargs)
        print("Wapis jarur aana")
    return mfx
@decorator_function
def Hello(a,b):
    print("Hello World")
    print(f"Addition of {a} and {b} is {a+b}")
Hello(5,3)

