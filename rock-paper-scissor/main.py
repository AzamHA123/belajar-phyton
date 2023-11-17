from random import randint

b = True

while b == True :
    title = "rps game"
    print(title)
    print(f"{'=' * len(title)}")

    weapon = ("r","p","s")

    player = input("choose (r|p|s)")
    computer = weapon[randint(0,2)]

    if player == computer:
        print("player uses, ", player)
        print("computer uses, ", computer)
        print("it's a draw")

    elif player == "r" :
        if computer== "p":
            print("player uses, ", player)
            print("computer uses, ", computer)
            print("computer wins")
        elif computer == "s" :
            print("player uses, ", player)
            print("computer uses, ", computer)
            print("player wins")

    elif player == "p" :
        if computer == "r" :
            print("player uses, ", player)
            print("computer uses, ", computer)
            print("player wins")
        elif computer == "s" :
            print("player uses, ", player)
            print("computer uses, ", computer)
            print("computer wins")

    elif player == "s" :
        if computer == "p" :
            print("player uses, ", player)
            print("computer uses, ", computer)
            print("player wins") 
        elif computer == "r" :
            print("player uses, ", player)
            print("computer uses, ", computer)
            print("computer wins")

    else :
        print(player, "is not a weapon")
    


