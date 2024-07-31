a = input("Enter the number:")
print(f"Multiplication table of {a} is")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
# except:
    # print("Invalid Input")

print("Some important lines of code")
print("End of program")

b = int(input("Enter a number:"))
try:
    print("Your number is",b)
except ValueError:
    print("It is a value error")