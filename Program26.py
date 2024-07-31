name = input("Enter your name:")
print("Swagat hain",name,"iss adbhut khel Kaun Banega Crorepati main")

# Who invented Telephone -> Alexander Graham Bell
# Taj Mahal situated in Agra was built by which Mughal ruler -> Shah Jahan
# Who holds the record of fastest fifty in T20 cricket -> Dipender Singh Airee
# Who holds the record of fastest ODI century in cricket -> AB De Villiers
# What is capital of Jharkhand -> Ranchi
# Which team has won maximum cricket ODI World Cup -> Australia

ques1 = "Who invented Telephone?"
ques2 = "Taj Mahal situated in Agra was built by which Mughal ruler?"
ques3 = "Which city is capital of Jharkhand?"
ques4 = "Which team has won maximum cricket ODI World Cups?"
ques5 = "Who holds the record of fastest fifty in International T20 cricket?"
ques6 = "Who holds the record of fastest ODI century in cricket?"
ques7 = "Who is creator of C++ language?"
ques = [ques1,ques2,ques3,ques4,ques5,ques6,ques7]
ans = [2,4,1,2,2,3,1]
option11 = "Galileo Galilei"
option12 = "Sir Alexander Graham Bell"
option13 = "Thomas Alva Adison"
option14 = "Sir Alexander Fleming"
option21 = "Akbar"
option22 = "Humayun"
option23 = "Aurangzeb"
option24 = "Shah Jahan"
option31 = "Ranchi"
option32 = "Raipur"
option33 = "Bhubaneshwar"
option34 = "Kolkata"
option41 = "India"
option42 = "Australia"
option43 = "New Zealand"
option44 = "West Indies"
option51 = "Yuvraj Singh"
option52 = "Dipender Singh Airee"
option53 = "Colin Munro"
option54 = "Quinton De Kock"
option61 = "Corey Anderson"
option62 = "Shahid Afridi"
option63 = "AB De Villiers"
option64 = "Gleen Maxwell"
option71 = "Bjarne Stroustrup"
option72 = "Dennis Ritchie"
option73 = "Guido van Rossum"
option74 = "James Gosling"
sum = 0
options = [[option11,option12,option13,option14],[option21,option22,option23,option24],\
            [option31,option32,option33,option34],[option41,option42,option43,option44],\
            [option51,option52,option53,option54],[option61,option62,option63,option64],\
            [option71,option72,option73,option74]]
print("Apke pass prashn ayega aur 4 vikalp usme se apko sahi vikalp chun na hai")
print("Jaise ap agge badte jayenge utne jyadi dhan rashi app jit te jayenge")
print("10,000 rupees")
print("50,000 rupees")
print("1,60,000 rupees")
print("3,20,000 rupees")
print("6,40,000 rupees")
print("50,00,000")
print("1,00,00,000 rupees")
amount = [10000,50000,160000,320000,640000,5000000,10000000]
counter = 7
print("Pehla sawal apke comupter screen par yeh raha")
while (counter>0):
    v = 1
    print("Question:",ques[7-counter])
    while (v<=4):
        print(v,".",options[7-counter][v-1],sep="")
        v= v+1
    print("Select the correct option.")
    t = int(input("Enter your desired option here:"))
    if (t==ans[7-counter]):
        print("Yeh bilkul sahi jawab hai")
        sum = amount[7-counter]
        print("You won",sum)
        if (counter==1):
            print("Apko dher saari bhadiya iss game ko jitne ke liye")
    else:
        print("Apsoos yeh galat jawab")
        if counter == 7:
            sum = 0
        else:
            sum = amount[6-counter]
        break
    counter = counter-1
print("Shukriya Kaun Banega Crorepati mei bhaag lene ke liya Thank You")
print("Amount you won is", sum)



