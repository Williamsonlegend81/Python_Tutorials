import random

ld1us1 = []
ld2us1 = []
ld1us2 = []
ld2us2 = []

while True:
    temp = ""
    count=1
    str1 = input("Enter your message user1:")
    if (str1=="Bye"):
        break
    for i in str1:
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
    ld1us1.append(ld1)
    # print(ld1us1)
    ld2 = []
    for i in ld1:
        if (len(i)<=3):
            i = i[::-1]
            # print(i,end=" ")
            ld2.append(i)
        else:
            a = chr(random.randint(ord('a'),ord('z')))
            b = chr(random.randint(ord('a'),ord('z')))
            c = chr(random.randint(ord('a'),ord('z')))
            str1 = i
            str3 = ""
            for i in range(3):
                str3 = str3+str1[i]
            str1 = str1+str3
            str4 = ""
            str4 = a+b+c
            for i in range(3,len(str1)):
                str4 = str4+str1[i]
            ld2.append(str4)
            # print(str3,end=" ")  
    ld2us1.append(ld2)
    # print(ld2us1) 
    
    # Part 2
    str2 = input("Enter your message user2:")
    if (str2=="Bye"):
        break
    temp2 = ""
    count2 = 1
    for i in str2:
        if (i==" " and count2==1):
            ld3 = [temp2]
            temp2 = ""
            count2 = count2+1
        elif (i==" " and count2>1):
            ld3.append(temp2)
            temp2 = ""
        else:
            temp2 = temp2+i
    ld3.append(temp2)
    ld1us2.append(ld3)
    # print(ld1us2)
    ld4 = []
    for i in ld3:
        if (len(i)<=3):
            i = i[::-1]
            # print(i,end=" ")
            ld4.append(i)
        else:
            a = chr(random.randint(ord('a'),ord('z')))
            b = chr(random.randint(ord('a'),ord('z')))
            c = chr(random.randint(ord('a'),ord('z')))
            str2 = i
            str3 = ""
            for i in range(3):
                str3 = str3+str2[i]
            str2 = str2+str3
            str4 = ""
            str4 = a+b+c
            for i in range(3,len(str2)):
                str4 = str4+str2[i]
            ld4.append(str4)
            # print(str3,end=" ")  
    ld2us2.append(ld4)
    # print(ld2us2)

h = input("Enter encode to view to encoded conversation or decode to interpret conversation:")
if (h=="encode"):
    for i in ld2us1:
        print("")
        print("User 1:")
        for x in i:
            print(x,end=" ")
    for i in ld2us2:
        print("")
        print("User 2:")
        for x in i:
            print(x,end=" ")
else:
    for i in ld1us1:
        print("")
        print("User 1:")
        for x in i:
            print(x,end=" ")
    for i in ld1us2:
        print("")
        print("User 2:")
        for x in i:
            print(x,end=" ")

# Decode
string1 = input("Enter your encrypted message:")
newstr = ""
if (len(string1)<=3):
    string1 = string1[::-1]
    print(string1)
else:
    for i in range(-3,0,1):
        newstr = newstr+string1[i]
    for i in range(3,len(string1)-3,1):
        newstr = newstr+string1[i]

