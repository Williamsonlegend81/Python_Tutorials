class Employee:
    company = "Apple"
    def Show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def ChangeCompany(cls,newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Harry"
e1.Show()
e1.ChangeCompany("Tesla")
e1.Show()
print(Employee.company)