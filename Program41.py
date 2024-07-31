marks = [12,56,32,98,12,45,1,4]

# index = 0
# for mark in marks:
#     print(mark)
#     if (index==3):
#         print("Harry, awesome!")
#     index = index+1

for index,mark in enumerate(marks):
    print(index,mark)
    if (index==3):
        print("Harry, awesome!")
print()
name = "Harrybhai ki Jay"
for index,character in enumerate(name,start=1):
    print(index,character)

