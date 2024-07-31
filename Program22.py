marks = [3,5,6,"Bhargav",True,9,10,11,20]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5]) it will give IndexError
print(marks[-3]) # it will print 6 as it will be evaluated as len(marks)-|(negindex)|
if "Bhargav" in marks:
    print("Yes")
else:
    print("No")
# same thing can be applied to string as well
if "Ha" in "Harry":
    print("Yes")
else:
    print("No")
print(marks[1:9])
print(marks[1:9:2])
# marks[0:] can be evaluated as marks[0:len(marks)]

# List comprehension
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
names = [i for i in names if len(i)>4]
print(names)
