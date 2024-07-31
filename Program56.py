class Person:
    def __init__(self, n, o):
        print("Hey I am person")
        self.name = n
        self.occupation = o
    name = "Harry"
    occupation = "Developer"

    def Info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Harry","Developer")
# print(a.name)
b = Person("Siddharth Rambhia", "AI Engineer")
a.Info()
b.Info()