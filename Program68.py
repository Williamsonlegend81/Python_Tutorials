import os

ld = os.listdir("E:/Python os modules/Images")
print(ld)
count = 0
for i in ld:
    count = count+1
    if i.endswith(".png"):
        os.rename(f"E:/Python os modules/Images/{i}",f"E:/Python os modules/Images/Screenshot{count}.png")
ld2 = os.listdir("E:/Python os modules/Images")
print(ld2)