import random

choice = input("Enter encode or decode:")
if (choice=="encode"):
    a = input("Enter your message:")

    ld = a.split(" ")
    newld = []
    for i in ld:
        if (len(i)>3):
            a1 = chr(random.randint(ord('a'),ord('z')))
            b1 = chr(random.randint(ord('a'),ord('z')))
            c1 = chr(random.randint(ord('a'),ord('z')))
            newstring = a1+b1+c1
            for b in range(3,len(i)):
                newstring = newstring+i[b]
            newstring = newstring+i[0]+i[1]+i[2]
            newld.append(newstring)

        else:
            newstring = i[::-1]
            newld.append(newstring)
    for w in newld:
        print(w,end=" ")

else:
    a = input("Enter your encoded message:")
    ld = a.split(" ")
    newld = []
    for i in ld:
        if (len(i)>3):
            newstring = i[len(i)-3]+i[len(i)-2]+i[len(i)-1]
            for n in range(3,len(i)-3):
                newstring = newstring+i[n]
            newld.append(newstring)
        else:
            newstring = i[::-1]
            newld.append(newstring)
    for w in newld:
        print(w,end=" ")