employee1 = {122:45,123:89,567:69,670:69}
employee2 = {222:67,566:90}
employee1.update(employee2)
print(employee1)

# employee1.clear() removes all items
# print(employee1)

# employee1.pop(122) removes an item with that key
# print(employee1)

employee1.popitem()
print(employee1)
# removes the last item

# Del keyword deletes entire dictionary
del employee1[123] # it will remove 123 key item
print(employee1)

