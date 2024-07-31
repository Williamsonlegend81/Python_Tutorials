f = open("myfile4.txt","w")
line1 = "This is one of the best tutorial in Python\n"
line2 = "The instructor of this great tutorial is Harry\n"
line3 = "This course will clear all basic concepts of python\n"
lines = [line1,line2,line3]
f.writelines(lines)
f.close()