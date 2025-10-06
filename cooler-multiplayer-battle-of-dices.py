import random

def print_header():
    print("\n" + "="*50)
    print(" COOLER MULTIPLAYER BATTLE OF DICES ".center(50))
    print("="*50)

def print_round_header(round_num):
    print("\n" + "-"*40)
    print(f"ROUND {round_num}".center(40))
    print("-"*40)

def print_summary(player_names, player_rolls, num_rounds, scores):
    print("\n" + "="*50)
    print(" FINAL GAME SUMMARY ".center(50))
    print("="*50)

    # Print header row
    print(f"{'Player':<12}", end="")
    for r in range(1, num_rounds+1):
        print(f"R{r:2}", end=" ")
    print(" Wins")  # extra column for total wins

    # Print each player's rolls + total wins
    for i, rolls in enumerate(player_rolls):
        print(f"{player_names[i]:<12}", end="")
        for roll in rolls:
            print(f"{roll:3}", end=" ")
        print(f"   {scores[i]}")

    # Decide overall winner(s)
    max_wins = max(scores)
    winners = [player_names[i] for i, score in enumerate(scores) if score == max_wins]

    print("\n" + "-"*50)
    if len(winners) == 1:
        print(f" The overall winner is {winners[0]} with {max_wins} wins!")
    else:
        print(f" It's an overall tie between: {', '.join(winners)} with {max_wins} wins each!")
    print("-"*50)

print_header()

# Ask number of players and rounds
num_players = int(input("Enter number of players: "))
num_rounds = int(input("Enter number of rounds: "))

# Get player names
player_names = []
for i in range(num_players):
    name = input(f"Enter name for Player {i+1}: ")
    player_names.append(name)

# Initialize rolls (nested list) and scores
player_rolls = [[] for _ in range(num_players)]
scores = [0] * num_players  # count wins

# Play rounds
for round_num in range(1, num_rounds + 1):
    input(f"\n Press ENTER to play Round {round_num}...")  # pause
    print_round_header(round_num)
    rolls = []

    for i in range(num_players):
        roll = random.randint(1, 6)
        player_rolls[i].append(roll)
        rolls.append((i, roll))
        print(f"{player_names[i]:<12} rolled  {roll}")

    # Determine round winner(s)
    highest_roll = max(rolls, key=lambda x: x[1])[1]
    winners = [i for i, roll in rolls if roll == highest_roll]

    if len(winners) == 1:
        print(f" Winner: {player_names[winners[0]]}")
        scores[winners[0]] += 1
    else:
        tied_names = [player_names[i] for i in winners]
        print(f" Tie between: {', '.join(tied_names)}")

# Print final summary + overall winner
print_summary(player_names, player_rolls, num_rounds, scores)

