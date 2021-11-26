import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

list_with_points = []
name_list = []

name_list = [i['name'] for i in players]

for params in players:
    numbers_matched = [lottery_numbers.intersection(set(numbers))for name, numbers in params.items()]
    calculated_points = 100 ** len(numbers_matched)
    list_with_points.append(calculated_points)

zip_func = dict(zip(name_list, list_with_points))

max_key = max(zip_func, key=zip_func.get)
print(f'{max_key} won {zip_func[max_key]}')

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

top_player = players[0]  # start by saying "the top matching player is the first one"

for player in players:  # Go over each player
    matched_numbers = len(player["numbers"].intersection(lottery_numbers))  # Calculate how many numbers they matched
    if matched_numbers > len(
            top_player["numbers"].intersection(lottery_numbers)):  # If they matched more than the current top player...
        top_player = player  # Say this player is the new top player

# Calculate their winnings using the formula!
winnings = 100 ** len(top_player["numbers"].intersection(lottery_numbers))

print(f"{top_player['name']} won {winnings}.")