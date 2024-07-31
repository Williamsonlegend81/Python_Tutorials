class Employee:
    def __init__(self,name,ID,salary):
        self.name = name
        self.ID = ID
        self.salary = salary
    def salary_inc(self,increment):
        return self.salary*increment

class Programmer(Employee):
    def __init__(self,name,ID,salary,language):
        self.language = language
        super().__init__(name, ID, salary)
    def salary_inc(self,increment):
        return super().salary_inc(increment)

p = Programmer("Hriday",12345,120000,"Python")
print(p.salary_inc(0.20))
