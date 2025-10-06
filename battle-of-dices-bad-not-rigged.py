import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins=0
player2_wins=0


player1_roll = random.randint(1, 12)
player2_roll = random.randint(1, 12)

# Round 1
print("\n--- Round 1 ---")
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: " ,  player1_roll)
print("Player 2 rolled: " ,  player2_roll)



if player1_roll > player2_roll:
    round_winner = "Player 1"
    player1_wins += 1
    print("Player 1 wins this round!")
elif player2_roll > player1_roll:
    round_winner = "Player 2"
    player2_wins += 1
    print("Player 2 wins this round!") 
else:
    player1_roll == player2_roll
    print("It's a tie")       


input("\nPress ENTER to continue...")

# We can print the game score:
print("The game score is Player 1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
print("Score: Player 1=", player1_wins, "Player 2=", player2_wins) 

input("\nPress ENTER to continue...")

#Round 2




player1_roll = random.randint(1, 12)
player2_roll = random.randint(1, 12)


print("\n--- Round 2 ---")
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: " ,  player1_roll)
print("Player 2 rolled: " ,  player2_roll)



if player1_roll > player2_roll:
    round_winner = "Player 1"
    player1_wins += 1
    print("Player 1 wins this round!")
elif player2_roll > player1_roll:
    round_winner = "Player 2"
    player2_wins += 1
    print("Player 2 wins this round!") 
else:
    player1_roll == player2_roll
    print("It's a tie")       


input("\nPress ENTER to continue...")

# We can print the game score:
print("The game score is Player 1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
print("Score: Player 1=", player1_wins, "Player 2=", player2_wins) 

input("\nPress ENTER to continue...")



#Update wins


# So far so good right? But how to check who got the highest roll?




#Round 3

player1_roll = random.randint(1,12) 
player2_roll = random.randint(1,12)
 
print("\n--- Round 3 ---")
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: " ,  player1_roll)
print("Player 2 rolled: " ,  player2_roll)



if player1_roll > player2_roll:
    round_winner = "Player 1"
    player1_wins += 1
    print("Player 1 wins this round!")
elif player2_roll > player1_roll:
    round_winner = "Player 2"
    player2_wins += 1
    print("Player 2 wins this round!") 
else:
    player1_roll == player2_roll
    print("It's a tie")       


input("\nPress ENTER to continue...")

# We can print the game score:
print("The game score is Player 1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
print("Score: Player 1=", player1_wins, "Player 2=", player2_wins) 

input("\nPress ENTER to continue...")

# Now we need to check if either player won.

if player1_wins == 3:
        print("Player 1 managed to secure the win and has become the new Champion! ")
        exit()

elif player2_wins == 3:
        print("Player 2 managed to secure the win and has become the new Champion! ")
        exit()
else:
        print("This exciting Battle of Dices is still going on! Who will win in the end? ")

 
 #Round 4

player1_roll = random.randint(1,12) 
player2_roll = random.randint(1,12)

print("\n--- Round 4 ---")
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: " ,  player1_roll)
print("Player 2 rolled: " ,  player2_roll)



if player1_roll > player2_roll:
    round_winner = "Player 1"
    player1_wins += 1
    print("Player 1 wins this round!")
elif player2_roll > player1_roll:
    round_winner = "Player 2"
    player2_wins += 1
    print("Player 2 wins this round!") 
else:
    player1_roll == player2_roll
    print("It's a tie")       


input("\nPress ENTER to continue...")

# We can print the game score:
print("The game score is Player 1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
print("Score: Player 1=", player1_wins, "Player 2=", player2_wins) 

input("\nPress ENTER to continue...")

# Now we need to check if either player won.

if player1_wins == 3:
        print("Player 1 managed to secure the win and has become the new Champion! ")
        exit()

elif player2_wins == 3:
        print("Player 2 managed to secure the win and has become the new Champion! ")
        exit()
else:
        print("This exciting Battle of Dices is still going on! Who will win in the end? ")

#Round 5

player1_roll = random.randint(1,12) 
player2_roll = random.randint(1,12)

print("\n--- Round 5 ---")
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: " ,  player1_roll)
print("Player 2 rolled: " ,  player2_roll)



if player1_roll > player2_roll:
    round_winner = "Player 1"
    player1_wins += 1
    print("Player 1 wins this round!")
elif player2_roll > player1_roll:
    round_winner = "Player 2"
    player2_wins += 1
    print("Player 2 wins this round!") 
else:
    player1_roll == player2_roll
    print("It's a tie")       


input("\nPress ENTER to continue...")

# We can print the game score:
print("The game score is Player 1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
print("Score: Player 1=", player1_wins, "Player 2=", player2_wins) 

input("\nPress ENTER to continue...")

# Now we need to check if either player won.

if player1_wins == 3:
        print("Player 1 managed to secure the win and has become the new Champion! ")
        exit()

elif player2_wins == 3:
        print("Player 2 managed to secure the win and has become the new Champion! ")
        exit()
else:
        print("This exciting Battle of Dices is still going on! Who will win in the end? ")

#Round 6

player1_roll = random.randint(1,12) 
player2_roll = random.randint(1,12)

print("\n--- Round 6 ---")
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: " ,  player1_roll)
print("Player 2 rolled: " ,  player2_roll)



if player1_roll > player2_roll:
    round_winner = "Player 1"
    player1_wins += 1
    print("Player 1 wins this round!")
elif player2_roll > player1_roll:
    round_winner = "Player 2"
    player2_wins += 1
    print("Player 2 wins this round!") 
else:
    player1_roll == player2_roll
    print("It's a tie")       


input("\nPress ENTER to continue...")

# We can print the game score:
print("The game score is Player 1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
print("Score: Player 1=", player1_wins, "Player 2=", player2_wins) 

input("\nPress ENTER to continue...")

# Now we need to check if either player won.

if player1_wins == 3:
        print("Player 1 managed to secure the win and has become the new Champion! ")
        exit()

elif player2_wins == 3:
        print("Player 2 managed to secure the win and has become the new Champion! ")
        exit()
else:
        print("This exciting Battle of Dices is still going on! Who will win in the end? ")

#Round 7

player1_roll = random.randint(1,12) 
player2_roll = random.randint(1,12)

print("\n--- Round 7 ---")
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: " ,  player1_roll)
print("Player 2 rolled: " ,  player2_roll)



if player1_roll > player2_roll:
    round_winner = "Player 1"
    player1_wins += 1
    print("Player 1 wins this round!")
elif player2_roll > player1_roll:
    round_winner = "Player 2"
    player2_wins += 1
    print("Player 2 wins this round!") 
else:
    player1_roll == player2_roll
    print("It's a tie")       


input("\nPress ENTER to continue...")

# We can print the game score:
print("The game score is Player 1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
print("Score: Player 1=", player1_wins, "Player 2=", player2_wins) 

input("\nPress ENTER to continue...")

# Now we need to check if either player won.

if player1_wins == 3:
        print("Player 1 managed to secure the win and has become the new Champion! ")
        exit()

elif player2_wins == 3:
        print("Player 2 managed to secure the win and has become the new Champion! ")
        exit()
else:
        print("This exciting Battle of Dices is still going on! Who will win in the end? ")

#Round 8

player1_roll = random.randint(1,12) 
player2_roll = random.randint(1,12)

print("\n--- Round 8 ---")
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: " ,  player1_roll)
print("Player 2 rolled: " ,  player2_roll)



if player1_roll > player2_roll:
    round_winner = "Player 1"
    player1_wins += 1
    print("Player 1 wins this round!")
elif player2_roll > player1_roll:
    round_winner = "Player 2"
    player2_wins += 1
    print("Player 2 wins this round!") 
else:
    player1_roll == player2_roll
    print("It's a tie")       


input("\nPress ENTER to continue...")

# We can print the game score:
print("The game score is Player 1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
print("Score: Player 1=", player1_wins, "Player 2=", player2_wins) 

input("\nPress ENTER to continue...")

# Now we need to check if either player won.

if player1_wins == 3:
        print("Player 1 managed to secure the win and has become the new Champion! ")
        exit()

elif player2_wins == 3:
        print("Player 2 managed to secure the win and has become the new Champion! ")
        exit()
else:
        print("This exciting Battle of Dices is still going on! Who will win in the end? ")

#Round 9

player1_roll = random.randint(1,12) 
player2_roll = random.randint(1,12)

print("\n--- Round 9 ---")
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: " ,  player1_roll)
print("Player 2 rolled: " ,  player2_roll)



if player1_roll > player2_roll:
    round_winner = "Player 1"
    player1_wins += 1
    print("Player 1 wins this round!")
elif player2_roll > player1_roll:
    round_winner = "Player 2"
    player2_wins += 1
    print("Player 2 wins this round!") 
else:
    player1_roll == player2_roll
    print("It's a tie")       


input("\nPress ENTER to continue...")

# We can print the game score:
print("The game score is Player 1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
print("Score: Player 1=", player1_wins, "Player 2=", player2_wins) 

input("\nPress ENTER to continue...")

# Now we need to check if either player won.

if player1_wins == 3:
        print("Player 1 managed to secure the win and has become the new Champion! ")
        exit()

elif player2_wins == 3:
        print("Player 2 managed to secure the win and has become the new Champion! ")
        exit()
else:
        print("This exciting Battle of Dices is still going on! Who will win in the end? ")

#Round 10

player1_roll = random.randint(1,12) 
player2_roll = random.randint(1,12)

print("\n--- Round 10 ---")
input("\nPress ENTER to roll the dice...")

print("Player 1 rolled: " ,  player1_roll)
print("Player 2 rolled: " ,  player2_roll)



if player1_roll > player2_roll:
    round_winner = "Player 1"
    player1_wins += 1
    print("Player 1 wins this round!")
elif player2_roll > player1_roll:
    round_winner = "Player 2"
    player2_wins += 1
    print("Player 2 wins this round!") 
else:
    player1_roll == player2_roll
    print("It's a tie")       


input("\nPress ENTER to continue...")

# We can print the game score:
print("The game score is Player 1 ", player1_wins, " vs. ", player2_wins, " Player 2.")
print("Score: Player 1=", player1_wins, "Player 2=", player2_wins) 

input("\nPress ENTER to continue...")

# Now we need to check if either player won.

if player1_wins == 3:
        print("Player 1 managed to secure the win and has become the new Champion! ")
        exit()

elif player2_wins == 3:
        print("Player 2 managed to secure the win and has become the new Champion! ")
        exit()
else:
        print("This exciting Battle of Dices is still going on! Who will win in the end? ")



 



    

 