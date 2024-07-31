# class ParentClass:
#     def parent_class(self):
#         print("This is a parent method")

# class DerivedClass(ParentClass):
#     def parent_method(self):
#         print("Harry")
#         super().parent_class()
#     def child_class(self):
#         print("This is a child method")

# b = DerivedClass()
# b.child_class()
# b.parent_class()

class Employee:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID

class Programmer(Employee):
    all = []
    def __init__(self,language,name,ID):
        super().__init__(
            name,ID
        )
        self.language = language
        Programmer.all.append(self)
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.ID},{self.language})"

a = Programmer("Hritesh",1001,"Java")
print(a.all)
