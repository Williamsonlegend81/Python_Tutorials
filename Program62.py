class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def Show_details(self):
        print(f"Name of employee is {self.name} and his id is {self.id}")

class Programmer(Employee):
    def Show_language(self):
        print("The default language is Python")
e = Employee("Rohan Das",400)
e.Show_details()
p = Programmer("Rajesh Kava",345)
p.Show_language()