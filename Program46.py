# Reading a file
# f = open("myfile.txt","rt")

# print(f)
# text = f.read()
# print(text)
# f.close()

# Writing a file
# f = open("myfile2.txt","a")
# f.write("Hello, world!")
# f.close()

with open("myfile2.txt","r") as f:
    text = f.read()
    print(text)
with open("myfile2.txt","w") as f:
    f.write("Mera naam Vrund hai")
