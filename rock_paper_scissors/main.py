import random


while True:
    choices = (["R", "P", "S"])

    computer = random.choice(choices)
    player = None

    while player not in choices:
        print("error")
        player = input("R = rock, P = paper, S = scissors?: ")

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
    

    elif player == "R":
        if computer == "P":
                print("computer: ", computer)
                print("player: ", player)
                print(" You lose!")
        else: 
                print("computer: ", computer)
                print("player: ", player)
                print(" You win!")
        break

    elif player == "S":
        if computer == "R":
                print("computer: ", computer)
                print("player: ", player)
                print(" You lose!")
        else: 
                print("computer: ", computer)
                print("player: ", player)
                print(" You win!")
        break

    elif player == "P":
        if computer == "S":
                print("computer: ", computer)
                print("player: ", player)
                print(" You lose!")
        else:
                print("computer: ", computer)
                print("player: ", player)
                print(" You win!") 
        break



