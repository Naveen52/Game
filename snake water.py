import os

import random
print("Hello thus is a snake water gun game")
times=1
userpoint = 0
opponent=0
while(times<=10):
    list= ["snake", "water", "gun"]
    A =random.choice(list)
    times = times +1
    user=input("S for Snake,W for Water,G for Gun")
    if user ==  "S"   and A == "water":
        print("snake drinks water,you won")
        print(f"you entered {user},and opponent entered {A}")
        userpoint= userpoint+1
        print(f"your point is {userpoint}")

    elif user ==  "S"   and A == "snake":
        print(f"you entered {user},and opponent entered {A}")
        print("Both chooses same")
        print("tie")

    elif user ==  "S"   and random.choice(list) == "gun":
        print(f"you entered {user},and opponent entered {A}")
        opponent=opponent+1
        print("Your snake killed ")

    elif user == "W" and random.choice(list) == "water":
        print(f"you entered {user},and opponent entered {A}")

        print("you choose same component")
        print("tie")

    elif user == "W" and random.choice(list) == "snake":
        print(f"you entered {user},and opponent entered {A}")
        opponent=opponent+1
        print("Snake drinks your water")

    elif user == "W" and random.choice(list) == "gun":
        print(f"you entered {user},and opponent entered {A}")
        userpoint=userpoint+1
        print("Gun drops in water ")

    elif user == "G" and random.choice(list) == "water":
        print(f"you entered {user},and opponent entered {A}")
        opponent=opponent+1
        print("Water takes your gun")

    elif user == "G" and random.choice(list) == "snake":
        print(f"you entered {user},and opponent entered {A}")
        userpoint=userpoint+1
        print("You killed the snake")

    elif user == "G" and random.choice(list) == "gun":
        print(f"you entered {user},and opponent entered {A}")
        print("same component ")
        print("tie")
    else:
        print("you have entered a wrong input")
    print(11-times," attempts left")

if userpoint == opponent:
    print("oops there is a tie")
print("You won" if userpoint>opponent else print("Computer wins"))
print("YOUR POINTS", userpoint)
print("COMPUTER POINTS", opponent)
if times>10:
    print("Thank you")