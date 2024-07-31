# MAP
def cube(x):
    return x**3
# print(cube(10))
# l = [1,4,2,9,5]
# newl = []
# for i in l:
#     newl.append(cube(i))
# print(newl)

l = [1,2,3,4,5,6,7,8,9]
newl = list(map(lambda x:x**3,l))
print(newl)

# FILTER
def filter_function(a):
    if a>3:
        return a

newnewl = list(filter(filter_function,l))
print(newnewl)

from functools import reduce

numbers = [1,2,3,4,5]

sum = reduce(lambda x,y: x+y, numbers)

print(sum)