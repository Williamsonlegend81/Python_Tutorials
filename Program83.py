class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("Sound made by animal")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark")

a = Animal("Dog","Mammal")
a.make_sound()

b = Dog("Sheru","Pomerian")
b.make_sound()

class Cat(Animal):
    def __init__(self,name,breed,color):
        Animal.__init__(self,name,species="Cat")
        self.breed = breed
        self.color = color

    def make_sound(self):
        print("Meow")
    def __str__(self):
        return f"{self.name} is a cat of {self.breed} of color {self.color}"

c = Cat("Mausi","Indian","Gray")
print(c)
c.make_sound()