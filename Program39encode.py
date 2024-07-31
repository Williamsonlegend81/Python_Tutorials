import random
string1 = input("Enter your message to encode it:")

temp = ""
count = 1
for i in string1:
    if (i==" " and count==1):
        ld1 = [temp]
        temp = ""
        count = count+1
    elif (i==" " and count>1):
        ld1.append(temp)
        temp = ""
    else:
        temp = temp+i
ld1.append(temp)
ld2 = []
for i in ld1:
    if (len(i)<=3):
        i = i[::-1]
        ld2.append(i)
    else:
        newstr = ""
        a = chr(random.randint(ord('a'),ord('z')))
        b = chr(random.randint(ord('a'),ord('z')))
        c = chr(random.randint(ord('a'),ord('z')))
        newstr = a+b+c
        for x in range(3,len(i)):
            newstr = newstr+i[x]
        for x in range(3):
            newstr = newstr+i[x]
        ld2.append(newstr)
for i in ld2:
    print(i,end=" ")

