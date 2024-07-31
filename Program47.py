f = open("myfile4.txt","r")
i = 0
while True:
    line = f.readline()
    if not line:
        # print(line,type(line))
        break
    i = i+1
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in maths is {m1}")
    print(f"Marks of student {i} in science is {m2}")
    print(f"Marks of student {i} in english is {m3}")
