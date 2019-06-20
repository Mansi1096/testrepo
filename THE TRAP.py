start=dict()
start={
      "1":"make pairs & walk random.",
      "2":"stay there & install tents.",
      "3":"together explore it."
      }
quest1=dict()
quest1={
        "1":"Look for more in the same place.",
	"2":"Try to run back to the others.",
	"3":"Go to others and explain everything."
        }
quest2=dict()
quest2={
        "1":"Go find someone inside the bungalow.",
        "2":"Decide to stay there instead of living in tents.",
        "3":"Get back to the tents."
        }
quest3=dict()
quest3={
         "1":"Enter in the shape and see those things.",
         "2":"Ignore it and move forward in any direction.",
         "3":"Get back to tents."
         }
choice1=dict()
choice1={
         "1":"Open the books",
         "2":"Try to run back to others",
         "3":"Burn the book"
         }
choice2=dict()
choice2={
         "1":"Lights switch on/off automatically",
         "2":"Bats came from cupboard",
         "3":"Found the secret passage"
         }
di=dict()
di={
    "1":"Saw an occult in the cupboard",
    "2":"Saw a secret passage through store room"
    }
def starts():
    print("Welcome to THE TRAP!!!!\n")
    print("RULES and REGULATIONS:\n")
    print(" 1) Unexpected is the new cliche.\n"
          " 2) Never ever under any circumstances believe the game is over when the killer is dead.\n"
          " 3) Whatever happen DO NOT DIE.\n")
    print("Let's Begin The Game\n")
    print("You and your friends went to an unknown place for camping in a forest and decided to explore things nearby. What you choose to do:")
    print(start)
def quest():
    if answer == "1":
        print("A pair found a kind of farm house in middle of the forest and enters in it and found some dead cats.What will you do now??")
        print(quest1)
    elif answer == "2":
        print("While installing ,a sound came from the middle forest. First they ignore it but they can’t ignore it when it happens repeatedly and follow the sound where they found a bungalow.")
        print(quest2)
    elif answer == "3":
        print("While exploring you found some strange things(bones placed in a star shape) in the forest")
        print(quest3)
answer=input("WANT TO PLAY GAME OR NOT(yes/no)")
if answer == "yes":
    starts()
else:
    print("looser!!!!you already lost")
    exit()
answer=input("ENTER THE CHOICE:")
quest()
answer=input("ENTER THE CHOICE:")
if answer == "1":
    print("Found a room with books of black magic and some weird stuff.Now do something fast!!!!!")
    print(choice1)
    ans=input("Enter the choice:")
    if ans == "1":
        print("Oops!!!!!!! That books were possessed with black magic. You get stuck in the book.\n")
        print("Sorry you lost the game!!!! Bye Bye")
        exit()
    elif ans == "2":
        print("You don't understand you are in a HAUNTED HOUSE and you are stuck in it\n")
        print("Sorry you lost the game!!!! Bye Bye")
        exit()
    elif ans == "3":
        print("Somehow you arrange the fuel and fire and burn the books!!!!!! You Won\n")
        print("You didn't won really, go back to rule number 2 and read it carefully. I didn't really exist in these books. You can't get rid off me")
        print(di)
        ans=input("Enter the choice fast:")
        if ans == "1":
            print("You find a mantra in occult and succeed in getting away from there. WINNER WINNER CHICKEN DINNER!!!!")
        elif ans == "2":
            print("That was a trap!!!!!! you died actually.")
            exit()
elif answer == "2":
    print("Unfortunately you guys get stuck in the house")
    print(choice2)
    ans=input("Enter the choice:")
    if ans == "1":
        print("You realize that this house is haunted and there are some paranormal activities in this house.")
        print(di)
        ans=input("Enter the choice fast:")
        if ans == "1":
            print("You find a mantra in occult and succeed in getting away from there. WINNER WINNER CHICKEN DINNER!!!!")
        elif ans == "2":
            print("That was a trap!!!!!! you died actually.")
            exit()
    elif ans == "2":
        print("You look in the cupboard and a voice whispers-WELCOME TO THE TRAP,YOU WILL DIE ONE BY ONE.\n")
        print("You died one by one and you lost with 5 kills.")
        exit()
    elif ans == "3":
        print("This secret passage leads you to the other side of the house which connects on a road leading to the front gate of house. I think you won.\n")
        print("HEYYYY GUYSSS!!!!!! IT WAS JUST YOUR HALLUCINATION,YOU CAN'T GET AWAY FROM ME.NOW YOU DIE!!!!!!!")
        exit()
elif answer == "3":
    print("Do whatever you want to do you can't ignore it, you can't get out from the shape now,and while getting back to tents you lost your way!!!!!!Sorry you lost with 0 kills")
    exit()
elif answer == "3":
    print("They explain everything but no one trusts them. And they gets separated as the pair who went in the that house goes back to get some proof in order to gain the trusts but never returns back.\n")
    print(" get lost you morons you didn’t support them you lost")
    exit()



