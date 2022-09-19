import random
score = 0
computer_score = 0
print("Welcome to Camille's Rock Paper Scissors Tornament!")
print("- \nTake your pick...\n-")
#Create the loop for the game: Include options, 'random' choice module, input
while True:
#present the acceptable options.
    choices = ["rock", "paper", "scissors"]
#present the selections: inputs by player, and random select by computer (or 2nd player if 2-player).
    computer = random.choice(choices)
    player = input("rock, paper, or scissors?: ").lower()
#print the selections.
    print("computer: ",computer)
    print("player: ",player)
#create the conditional statements: 
    #account for alternative input, account for a tie/draw, account for wins per hand/selection, end game mechanism.
#incorporate accumulative scoring - ensure it can be concatenated with string data.
    if player not in choices:
        print("You Cheated!\nPlay fair and choose from rock, paper, or scissors next time ;)...")
    if player == computer:
        print("Draw!")
    elif player == "rock":
        if computer == "paper":
            print("Computer Wins!")
            computer_score = computer_score + 1
            print("Computer score is: "+str(computer_score))
        if computer == "scissors":
            print("Player Wins!")
            score = score + 1
            print("your score is: "+str(score))
    elif player == "paper":
        if computer == "scissors":
            print("Computer Wins!")
            computer_score = computer_score + 1
            print("computer score is: "+str(computer_score))
        if computer == "rock":
            print("Player Wins")
            score = score + 1
            print("your score is: "+str(score))
    elif player == "scissors":
        if computer == "rock":
            print("Computer Wins!")
            computer_score = computer_score + 1
            print("computer score is: "+str(computer_score))
        if computer == "paper":
            print("Player Wins!")
            score = score + 1
            print("your score is: "+str(score))
#create the breaking mechanism to end or continue the game.
    play_again = input("Play Again (Y/N): ").upper()
    if play_again != "Y":
        break
#display the game stats.
print("Game Over! Thanks for playing\n" + "__________________________\n" +"FINAL SCORES\n" + "Player " + str(score) + " - " + 
str(computer_score) + " Computer" + "\n__________________________")
#ANNOUNCEMENT: I'm making this into a PyGame with a GUI
print("\nupdate:\n".upper() + 
"PyGame version AND a new game in the works!\nStay tuned!")