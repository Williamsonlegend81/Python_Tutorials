class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def Show_details(self):
        print(f"Name:{self.name}")
        print(f"Species:{self.species}")
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed
    def Show_details(self):
        Animal.Show_details(self)
        print(f"Breed:{self.breed}")
class GoldenRetriever(Dog):
    def __init__(self,name,height):
        Dog.__init__(self,name,breed="Golden Retriever")
        self.height = height
    def Show_details(self):
        Dog.Show_details(self)
        print(f"Height:{self.height} cms")

a = GoldenRetriever("Hales",70)
a.Show_details()
print(GoldenRetriever.mro())