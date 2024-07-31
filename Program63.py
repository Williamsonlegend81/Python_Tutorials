# class Employee:
#     def __init__(self):
#         self.name = "Harry"
# a = Employee()
# print(a.name)

# Private
class Employee:
    def __init__(self):
        self.__name = "Harry"

a = Employee()
# print(a.__name) cannot be accessed directly
print(a._Employee__name) # can be accessed indirectly (name mangling)
print(a.__dir__()) # To wiew all functions that can be accessed by object a