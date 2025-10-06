from dice import d20,d100
 

# initialize scores
player1_wins = 0
player2_wins = 0
rounds_played= 0 #Count how many rounds have been played

print("🎲 Welcome to Battle of the Dices!")
print("First player to reach 3 wins is the Champion!\n")

#Pause before starting round 1 
input("\npress ENTER to roll the dice")

# 👉 loop runs until one player has 3 wins
while player1_wins < 3 and player2_wins < 3:
    rounds_played +=1 #count this round
    # roll dice (default is a D6, can be changed later)
    player1_roll = d20() + d100()
    player2_roll = d20() + d100()

    print(f"\n--- {rounds_played}---")
    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    # check round winner
    if player1_roll > player2_roll:
        print("Player 1 wins this round!")
        player1_wins += 1
    elif player2_roll > player1_roll:
        print("Player 2 wins this round!")
        player2_wins += 1
    else:
        print("It’s a tie!")

    # show current score
    print("Score: Player 1 =", player1_wins, "Player 2 =", player2_wins, "\n")

    # pause for user
    input("Press ENTER to continue...")

# after loop ends → announce champion
if player1_wins == 3:
    print(f"\n Player 1 is the Battle of Dices Champion after {rounds_played} rounds!") 
else:
    print(f"\n Player 2 is the Battle of Dices Champion after {rounds_played} rounds! ")
