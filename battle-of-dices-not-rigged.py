from dice import d6

print(" Welcome to Battle of Dices! ")

input("\nPress ENTER to start the game")

# --- Number of rounds ---
num_rounds_str= input("\nHow many rounds do you want to play?")
if num_rounds_str == "":
    num_rounds = 6

else: 
    num_rounds = int(num_rounds_str)

# --- Lists to store rolls ---
p1_rolls = []
p2_rolls = []

# --- Play the rounds ---
for r in range(num_rounds):
    input(f"\nPress ENTER to roll the dice for Round {r+1}...")
    player1_roll = d6()   # <-- call the function
    player2_roll = d6()
    p1_rolls.append(player1_roll)
    p2_rolls.append(player2_roll)
    print(f"Player 1 rolled: {player1_roll}")
    print(f"Player 2 rolled: {player2_roll}")
    print(f"Round {r+1} | Player 1 rolled: {player1_roll} | Player 2 rolled: {player2_roll}")

# --- Build the header row dynamically ---
header = f"| Round    | " + " | ".join(str(r) for r in range(1, num_rounds+1)) + " |"
sep = "-" * len(header)

# --- Print the summary table as a string (instead of just printing)---
summary = []
summary.append("\n Game Summary (using d6 dice):\n")
summary.append(sep)
summary.append(header)
summary.append(sep)
summary.append("| Player 1 | " + " | ".join(str(x) for x in p1_rolls) + " |")
summary.append(sep)
summary.append("| Player 2 | " + " | ".join(str(x) for x in p2_rolls) + " |")
summary.append(sep)

# --- Totals and winner ---
sum1 = sum(p1_rolls)
sum2 = sum(p2_rolls)

summary.append(f"\nPlayer 1 total: {sum1}")
summary.append(f"Player 2 total: {sum2}")

if sum1 > sum2:
    summary.append("Player 1 wins the battle! ")
elif sum2 > sum1:
    summary.append("Player 2 wins the battle! ")
else:
    summary.append("It’s a tie! ")

# --- Print summary to screen ---
print("\n".join(summary))

# --- Ask for filename and save to file ---
filename = input("\nEnter a filename to save the results (e.g., results.txt): ")
with open(filename, "w") as f:
    f.write("\n".join(summary))

print(f"\n Game summary saved to {filename}")
