# a = True
print(a:=False)

numbers = [1,2,3,4,5]
while(n:=len(numbers))>0:
    print(numbers.pop())

names = ["John","Jim","Jim"]
if (name:=input("Enter a name:")) in names:
    print(f"Hello, {name}")
else:
    print("Name not found")

food = []
while (a:=input("Enter the food you like:"))!="quit":
    food.append(a)
print(food)