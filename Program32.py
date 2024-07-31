cities1 = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
cities3 = cities1.union(cities2)
print(cities3)
# cities1.update(cities2)
# it will bring elements of cities2 in cities1 we can say it will do union operation
# print(cities1)

# Union returns a set and update will add elements to existing set
# cities3 = cities2.intersection(cities1)
# print(cities3)

# cities1.intersection_update(cities2)
# print(cities1)
# intersection_update will perform operation update the set 
# and intersection will perform operation
# and return a set

# cities3 = cities1.symmetric_difference(cities2)
# print(cities3)

# cities1.symmetric_difference_update(cities2)
# print(cities1)

# Symmetric difference is basically (A-B)union(B-A) and it returns elements unlike
# update which only updates the set regardless of creating a new element

# Difference is basically (A-B) when A.difference(B) is invoked
# Difference update is basically works with same principle as previous one

# Disjoint will check if A intersection B is zero
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))
# it will return False

# Superset will check if A set is superset of B set
# B = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# A = {"Tokyo", "Madrid", "Berlin", "Delhi", "Kabul", "Seoul"}
# print(A.issuperset(B))

# is subset will check if A set is subset of B
# A = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# B = {"Tokyo", "Madrid", "Berlin", "Delhi", "Kabul", "Seoul"}
# print(A.issubset(B))

# Add function will add a single item to a set
# cities = {"Tokyo", "Delhi", "Madrid", "Berlin"}
# cities.add("Canberra")
# print(cities)

# Remove method will remove a single element of that value in set
# If item is not present and we use remove then remove will raise an error
# However discard will not throw error
# cities = {"Tokyo", "Delhi", "Madrid", "Berlin"}
# cities.remove("Delhi")
# print(cities)

# Pop will remove an element from the set randomly
# cities = {"Tokyo", "Delhi", "Madrid", "Berlin"}
# item = cities.pop()
# print(cities)
# print(item)

# Del will delete the entire set
# Existence of set will removed

# Clear will clear all items in the set
# After clear then we print(set) it will return empty set

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
  print("Carla is present.")
else:
  print("Carla is absent.")
