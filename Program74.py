class Fruit:
    def __init__(self,name):
        self._name = name
    @property
    def fruit_name(self):
        print(f"{self._name} was accessed")
        return self._name
    @fruit_name.setter
    def fruit_name(self,value):
        print(f"{self._name} is now {value}")
        self._name = value
    @fruit_name.deleter
    def fruit_name(self):
        print(f"{self._name} was deleted")
        del self._name
        
if __name__ == "__main__":
    fruit = Fruit("Banana")
    print(fruit.fruit_name)
    fruit.fruit_name = "Orange"
    print(fruit.fruit_name)
    del fruit.fruit_name

    print(fruit.fruit_name)
