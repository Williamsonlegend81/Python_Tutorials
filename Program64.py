class Student:
    def __init__(self):
        self._name = "Harry"
    def _funName(self): # protected method
        return "CodewithHarry"
    
class Subject(Student): # inherited class
    pass
obj = Student()
obj1 = Subject()
print(dir(obj))
print(obj._name)
print(obj._funName())

print(obj1._name)
print(obj1._funName())