class Person:
    name = "Rohan"
    occupation = "Software Developer"
    def Info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
b.name = "Parshv Joshi"
b.occupation = "Researcher"
a.name = "Shubham"
a.occupation = "Web developer"
print(a.name,a.occupation)
a.Info()
b.Info()