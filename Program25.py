countries = ("Spain","Italy","India","England","Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries = tuple(temp)
print(countries)

# we can concatenate tuples without converting them to list
countries1 = ("India","Bangladesh","Pakistan","Sri Lanka")
countries2 = ("China","Myanmar","Bhutan","Nepal")
countries1 = countries1 + countries2
print(countries1)
print()
# count method will show number of elements of that value
tuple1 = (0,1,2,3,2,2,2,1,1,13,3)
res = tuple1.count(3)
print(res)

# tuple.index(element, start, end)
resp = tuple1.index(2,3,7)
reso = len(tuple1)
print(reso)
print("First occurence of 2 in the tuple is",resp)
