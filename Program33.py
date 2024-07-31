dict1 = {344:"Harry",56:"Shubham",678:"Zakir",567:"Neha"}
# print(dict1[567])
# print(dict1.get(344))
# Methods to access value
# If element is not present and we use dict[key] it will raise an error
# If element is not present and we use dict.get(key) it will return None

# In order to acccess all keys
print(dict1.keys())
# Another method
for key in dict1:
    print(key)

# In order to access values in dictionary
print(dict1.values())
# Another Method
for key in dict1.keys():
    print(f"For a {key} in the dictionary the value of corresponding key is {dict1[key]}")

# It will return in tuples, key associated with value
print(dict1.items())
# Another method
for key,value in dict1.items():
    print(f"The {key} has {value} associated with it in the dictionary")
