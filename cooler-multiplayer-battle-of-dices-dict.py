# cooler-multiplayer-battle-of-dices-dict.py - Task 16: Enhanced version with file save

import random
import copy

# Simulate dice roll
def rollD6():
    return random.randint(1, 6)

# Dictionary Template for storing player information:
player_info = {
    "name": "",
    "email": "",
    "country": "", 
    "wins": 0,
    "rolls": [],
    "total_score": 0,
    "best_roll": 0
}

# List to store the dicts for each player:
players = []

# Game variables
rounds = 0
gameover = False
winning_score = 3

print("*** COOLER Multiplayer Battle of Dices ***")
print("==========================================")

# Get number of players
try:
    number_of_players = int(input("How many players? "))
    if number_of_players < 2:
        print("Need at least 2 players!")
        exit()
except:
    print("Please enter a valid number!")
    exit()

# Get player information
for i in range(number_of_players):
    # Make a deep copy of the template for this player:
    player = copy.deepcopy(player_info)
    
    print(f"\n--- Player {i+1} ---")
    player["name"] = input("What is your name? ")
    player["email"] = input("What is your e-mail? ")
    player["country"] = input("What is your country? ")
    
    players.append(player)

# Display player lineup
print("\n==========================================")
print("PLAYER LINEUP:")
for i, player in enumerate(players):
    print(f"  {i+1}. {player['name']} ({player['country']})")
print("==========================================")

# Main game loop
while not gameover:
    rounds += 1
    print(f"\nROUND {rounds}")
    print("------------------------------")
    
    # Dice roll for each player in the current round:
    current_rolls = []
    
    # Roll dice for each player
    for each_player in players:
        input(f"{each_player['name']}, press ENTER to roll the dice...")
        roll = rollD6()
        each_player["rolls"].append(roll)
        each_player["total_score"] += roll
        
        # Track best roll
        if roll > each_player["best_roll"]:
            each_player["best_roll"] = roll
            
        current_rolls.append(roll)
        print(f"   {each_player['name']} rolled: {roll}")
    
    # Find winners of the round
    max_roll = max(current_rolls)
    winners = []
    
    # Search for all players who got the highest roll
    for each_player in players:
        if each_player["rolls"][-1] == max_roll:
            each_player["wins"] += 1
            winners.append(each_player['name'])
    
    print(f"\nRound Winners: {', '.join(winners)}")
    
    # Display current standings
    print("\nCURRENT STANDINGS:")
    for each_player in players:
        print(f"   {each_player['name']}: {each_player['wins']} wins | Best roll: {each_player['best_roll']} | Total score: {each_player['total_score']}")
    
    # Check if there is/are winner(s)
    champions = []
    for each_player in players:
        if each_player["wins"] >= winning_score:
            champions.append(each_player['name'])
            gameover = True
    
    if champions:
        print(f"\nCHAMPION{'S' if len(champions) > 1 else ''}: {', '.join(champions)}")
        print("THE BATTLE IS OVER!")
    elif not gameover:
        print("\nThe battle continues! Next round...")

# Final statistics
print("\n==========================================")
print("FINAL STATISTICS:")
print("==========================================")

for each_player in players:
    if each_player["rolls"]:
        avg_roll = sum(each_player["rolls"]) / len(each_player["rolls"])
    else:
        avg_roll = 0
        
    print(f"\n{each_player['name']} ({each_player['country']}):")
    print(f"  Wins: {each_player['wins']}")
    print(f"  Rolls: {each_player['rolls']}")
    print(f"  Best roll: {each_player['best_roll']}")
    print(f"  Average roll: {avg_roll:.2f}")
    print(f"  Email: {each_player['email']}")

# Save results to file (from Task 14/Lecture 7)
filename = input("\nEnter the filename to save the results: ")
with open(filename, "w") as file:
    # Player Information:
    file.write("Player Information:\n")
    
    # Save each player information
    for each_player in players:
        file.write(
            f"Name: {each_player['name']}\n"
            f"Email: {each_player['email']}\n"
            f"Country: {each_player['country']}\n"
            f"Wins: {each_player['wins']}\n"
            f"Best Roll: {each_player['best_roll']}\n"
            f"Total Score: {each_player['total_score']}\n\n"
        )
    
    file.write("\nGame rounds:\n")
    
    # Round history
    for r in range(rounds):
        # Start with empty text for this round
        rolls_str = ""
        # Go through each player and build the string step by step
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"
            # Add a comma and space unless it's the last player
            if i < len(players) - 1:
                rolls_str += ", "
        # Now write the full round info to the file
        file.write(f"Round {r+1}: {rolls_str}\n")

print(f"\nGame completed after {rounds} rounds!")
print(f"Results saved to {filename}!")