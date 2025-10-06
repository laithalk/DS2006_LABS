import random

# Simulate dice roll
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

print("*** BUGGED Multiplayer Battle of Dices ***")

# Get number of players
try:
    number_of_players = int(input("How many players? "))
except:
    print("Please enter a valid number!")
    exit()

# Get player information - USING SHALLOW COPY (THE BUG!)
for i in range(number_of_players):
    # BUG: Using shallow copy instead of deepcopy
    player = player_info.copy()  # THIS IS THE BUG!
    
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
        each_player["rolls"].append(roll)  # BUG APPEARS HERE!
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

# Show the bug clearly
print("\n=== BUG DEMONSTRATION ===")
print("Notice how all players have the SAME rolls list:")
for i, player in enumerate(players):
    print(f"Player {i+1} ({player['name']}): rolls = {player['rolls']}")