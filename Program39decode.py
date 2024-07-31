string1 = input("Enter your encrypted message:")
newstr = ""
temp = ""
count=1
for i in string1:
    if (i==" " and count==1):
        ld1 = [temp]
        temp = ""
        count = count+1
    elif(i==" " and count>1):
        ld1.append(temp)
        temp = ""
    else:
        temp = temp + i
ld1.append(temp)
print(ld1)
for i in ld1:
    if (len(i)<=3):
        i = i[::-1]
        print(i,end=" ")
    else:
        newstr = ""
        for a in range(-3,0,1):
            newstr = newstr+i[a]
        for b in range(3,len(i)-3):
            newstr = newstr+i[b]
        print(newstr,end=" ") 

