class Employee:
    def __init__(self,name):
        self.name = name
    def Show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance = dance
    def Show(self):
        print(f"The dance is {self.dance}")

class DancerEmp(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name
    def __str__(self):
        return f"{self.name} is a dancer and knows {self.dance}"

o = DancerEmp("Kathak","Shivani")
print(o)
o.Show()
print(DancerEmp.mro())