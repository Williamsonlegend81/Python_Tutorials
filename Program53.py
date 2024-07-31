import random

def checkinput(string):
    if (string!="Snake" and string!="Water" and string!="Gun"):
        print("Invalid input please enter valid option")
        return 0
    else:
        return 1
playername = input("Enter your name:")
a = int(input("How many rounds you want to play:"))
computer = 0
player = 0
i = 1
while(i<=a):
    choices = ["Snake","Water","Gun"]
    computerchoices = random.choice(choices)
    playerchoice = input("Enter Snake,Water or Gun:")
    c = checkinput(playerchoice)
    if (c==0):
        i=i-1
    print(f"Round {i}")
    if (computerchoices=="Snake" and playerchoice=="Snake"):
        print("-------------------------------------")
        print(f"Draw for round {i}")
        print(f"Choice of {playername} is {playerchoice} and choice of computer is {computerchoices}")
    elif (computerchoices=="Water" and playerchoice=="Water"):
        print("-------------------------------------")
        print(f"Draw for round {i}")
        print(f"Choice of {playername} is {playerchoice} and choice of computer is {computerchoices}")
    elif (computerchoices=="Gun" and playerchoice=="Gun"):
        print("-------------------------------------")
        print(f"Draw for round {i}")
        print(f"Choice of {playername} is {playerchoice} and choice of computer is {computerchoices}")
    elif (computerchoices=="Water" and playerchoice=="Gun"):
        print("-------------------------------------")
        print(f"Computer wins this round {i}")
        computer=computer+1
        print(f"Choice of {playername} is {playerchoice} and choice of computer is {computerchoices}")
    elif (computerchoices=="Snake" and playerchoice=="Water"):
        print("-------------------------------------")
        print(f"Computer wins this round {i}")
        computer = computer+1
        print(f"Choice of {playername} is {playerchoice} and choice of computer is {computerchoices}")
    elif (computerchoices=="Gun" and playerchoice=="Snake"):
        print("-------------------------------------")
        print(f"Computer wins this round {i}")
        computer = computer+1
        print(f"Choice of {playername} is {playerchoice} and choice of computer is {computerchoices}")
    elif (computerchoices=="Snake" and playerchoice=="Gun"):
        print("-------------------------------------")
        print(f"{playername} wins this round {i}")
        player = player+1
        print(f"Choice of {playername} is {playerchoice} and choice of computer is {computerchoices}")
    elif (computerchoices=="Water" and playerchoice=="Snake"):
        print(f"{playername} wins this round {i}")
        player = player+1
        print(f"Choice of {playername} is {playerchoice} and choice of computer is {computerchoices}")
    elif (computerchoices=="Gun" and playerchoice=="Water"):
        print(f"{playername} wins this round {i}")
        player = player+1
        print(f"Choice of {playername} is {playerchoice} and choice of computer is {computerchoices}")
    i = i+1
    c = 1
if (computer>player):
    print(f"Computer wins the round by {computer}:{player}")
elif(player>computer):
    print(f"{playername} wins the round by {player}:{computer}")
elif(player==computer):
    print(f"A draw between computer and {playername} their respective points are {computer}:{player}")
