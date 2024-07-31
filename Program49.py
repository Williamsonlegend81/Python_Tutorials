with open("myfile6.txt","w") as f:
    # Move to 10th byte in the file
    f.writelines(["line1 is Hello\n","line2 is Content\n","line3 is Farewell\n"])    
    f.truncate(5)

with open("myfile6.txt","r") as f:
    text = f.read()
    print(text)
