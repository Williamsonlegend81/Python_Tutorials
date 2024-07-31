# tup = (1,)
# print(type(tup))
# print(tup)
# Tuple with one element is classified as int
# In order to make python realise that it is tuple give comma for eg(1,)

tup = (1,2,6,3,89,100,"Cameron Green")
print(tup)
print("Length of tuple is",len(tup))
# tup[0]= 90 it will give TypeError
print(tup[0])
print(tup[1])
print(tup[-1])
# print(tup[34]) IndexError

if "Cameron Green" in tup:
    print("Present")
else:
    print("Absent")

tup2 = tup[1:5]
print(tup2)
# tup[0:] it will print from 0 index to last element
