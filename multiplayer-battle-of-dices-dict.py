import random
import copy

# Simulate dice roll (since we don't have the dice module)
def rollD6():
    return random.randint(1, 6)

# Dictionary Template for storing player information:
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}

# List to store the dicts for each player:
players = []

# Game variables
rounds = 0
gameover = False
winning_score = 3

print("*** Multiplayer Battle of Dices ***")

# Get number of players
try:
    number_of_players = int(input("How many players? "))
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

# Main game loop
while not gameover:
    rounds += 1
    print(f"\n=== Round {rounds} ===")
    
    # Dice roll for each player in the current round:
    current_rolls = []
    
    # Roll dice for each player
    for each_player in players:
        roll = rollD6()
        each_player["rolls"].append(roll)
        current_rolls.append(roll)
        print(f"Player {each_player['name']} rolled: {roll}")
    
    input("\nPress ENTER to continue...")
    
    # Find winners of the round
    max_roll = max(current_rolls)
    winners = []
    
    # Search for all players who got the highest roll
    for each_player in players:
        if each_player["rolls"][-1] == max_roll:
            each_player["wins"] += 1
            winners.append(each_player['name'])
    
    print(f"Winners of this round: {winners}")
    
    # Check if there is/are winner(s)
    for each_player in players:
        if each_player["wins"] >= winning_score:
            print(f"\n{each_player['name']} is the newest Battle of Dices Champion!")
            gameover = True
    
    if not gameover:
        print("This heated Battle of Dices is still going on! Who will win in the end?")

# Save results to file
filename = input("\nEnter the filename to save the results: ")
with open(filename, "w") as file:
    # Player Information:
    file.write("Player Information:\n")
    
    # Save each player information
    for each_player in players:
        file.write(
            f"Name: {each_player['name']}\n"
            f"* E-mail: {each_player['email']}\n"
            f"* Country: {each_player['country']}\n"
            f"* Wins: {each_player['wins']}\n\n"
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

print("\nGame over! Results saved successfully.")