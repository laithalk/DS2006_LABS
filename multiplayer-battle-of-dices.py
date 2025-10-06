import random

print("Welcome to Multiplayer Battle of Dices")

#Ask for numbers of players and rounds
num_players = int(input("Enter number of players:"))
num_rounds = int(input("Enter number of rounds:"))

#Get player names
player_names = []

for i in range(num_players):
    name = input(f"Enter name for Player {i+1}: ")
    player_names.append(name)


#initalize rolls - a nested list (one empty list for each player)
player_rolls = [[] for _ in range(num_players)]

#Game loop
for round_num in range(1, num_rounds + 1):
    print(f"\n--- Round {round_num}---")
    rolls = []

    for i in range(num_players):
        roll = random.randint(1,6)
        player_rolls [i].append(roll)
        rolls.append((i,roll))
        print(f"{player_names[i]}rolled {roll}")


#Determine round winner(s)
highest_roll = max(rolls, key=lambda x: x[1])[1]
winners = [player_names[i] for i, roll in rolls if roll == highest_roll]

if len(winners) ==1:
    print(f"{winners[0]}wins this round!")
else:
    print(f"It's a tie between:{','.join(winners)}")


#Game summary
print("\n==== Game Summary ====")
print("Round:",end="")
for r in range(1, num_rounds + 1):
    print()

for i, rolls in enumerate(player_rolls):
    print(f"{player_names[i]:<8}:",end= " ")
    for roll in rolls:
        print(f"{roll:4}", end="")
    print()