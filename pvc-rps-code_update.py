import random

#Create the loop for the game: Include options, 'random' choice module, input
#present the acceptable options.
#present the selections: inputs by player, and random select by computer (or 2nd player if 2-player).
#print the selections.
#create the conditional statements: 
    #account for alternative input, account for a tie/draw, account for wins per hand/selection, end game mechanism.
#incorporate accumulative scoring - ensure it can be concatenated with string data.
#create the breaking mechanism to end or continue the game.
#display the game stats.

score = 0
computer_score = 0
Round = 1
print("Welcome to Camille's Rock Paper Scissors Tournament!")
print("- \nTake your pick...")
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    print("\nround ".upper() + str(Round))
    player = input("rock, paper, or scissors?: ").lower()
    print("\nComputer chose: ",computer.upper())
    print("Player chose: ",player.upper())
    if player not in choices:
        print("You Cheated!\nPlay fair and choose from rock, paper, or scissors next time ;)...")
    if player == computer:
        Round += 1
        print("\nDraw!".upper())
    elif player == "rock":
        if computer == "paper":
            print("\nComputer Wins!".upper())
            computer_score += 1
            Round += 1
            print("Computer score is: "+str(computer_score))
        if computer == "scissors":
            print("\nPlayer Wins!".upper())
            score += 1
            Round += 1
            print("Your score is: "+str(score))
    elif player == "paper":
        if computer == "scissors":
            print("\nComputer Wins!".upper())
            computer_score += 1
            Round += 1
            print("Computer score is: "+str(computer_score))
        if computer == "rock":
            print("\nPlayer Wins".upper())
            score += 1
            Round += 1
            print("Your score is: "+str(score))
    elif player == "scissors":
        if computer == "rock":
            print("\nComputer Wins!".upper())
            computer_score += 1
            Round += 1
            print("Computer score is: "+str(computer_score))
        if computer == "paper":
            print("\nPlayer Wins!".upper())
            score += 1
            Round += 1
            print("Your score is: "+str(score))
    play_again = input("\nPlay Again (Y/N): ").upper()
    if play_again != "Y":
        break

print("\nGame Over! Thanks for playing\n" + "__________________________\n" + "Rounds Played: ".upper() + str(Round) + "\n " +
"\nFINAL SCORES\n" + "Player " + str(score) + " - " + str(computer_score) + " Computer" + "\n__________________________")
print("\nupdate:\n".upper() + 
"\nPyGame version AND a new game in the works!\nStay tuned!")

#ANNOUNCEMENT: I'm making this into a PyGame with a GUI.
