string = "15"
number = 7
string_number = int(string) # throws an error if the
# string is not a valid integer
sum = number+string_number
print("Sum of both the integers is:",sum)

# implicit type casting
c = 1.9
d = 8
print(type(d))
d = c+d
print(type(d))
