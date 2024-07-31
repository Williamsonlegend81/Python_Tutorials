l = [10,45,100,5,100,100]
l.append(70)
# l.sort(reverse=True)
# l.reverse()
print(l)
print(l.index(10)) # this method will return first occurence of the element
print(l.count(100))
m = l.copy()
m[0] = 0
l.insert(1,899)
n = [900,1000,1100]
k = l+m
# it will merge l and m and m will be inserted behind l
print(k)
l.extend(n)
# it will extend l and concatenate n behind l
print(l)
print(m)


