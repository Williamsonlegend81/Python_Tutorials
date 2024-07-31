class Fruits:
    def __init__(self,name):
        self._name = name
    def get_name(self):
        print("Getting name")
        return self._name
    def set_name(self, newname):
        self._name = newname

if __name__=="__main__":
    fruit = Fruits("banana")
    a = fruit._name
    fruit.set_name("Orange")
    print(fruit.get_name())
    
