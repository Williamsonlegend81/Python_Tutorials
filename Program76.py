l = [1,2,3,4,5]
print(dir(l))

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
p = Person("Harry",60)
print(p.__dict__)

print(help(str))