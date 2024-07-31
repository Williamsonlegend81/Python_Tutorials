names = "Harry,Shubham"
print(names[0:5])
print("Length of the string", len(names))
print("Mango is a",len("Mango"),"character word")
fruit = "Apple"
print(fruit[0:5])
# including zero but not five
# print(fruit[0:]) # by default it will take length of string
print(fruit[-1:-3])
# Negative index can be represented as len(fruit)-index
# 4:2 can be interpreted in the above statement
print(fruit[-3:-1])
alphabets = "ABCDE"
for character in alphabets:
    print(character)