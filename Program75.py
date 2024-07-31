class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromstring(cls,string):
        name, age = string.split("-")
        # return cls(string.split("-")[0],int(string.split[1]))
        return cls(name,int(age))
string = "Harry-12000"
e = Employee.fromstring(string)
print(e.name)
print(e.salary)