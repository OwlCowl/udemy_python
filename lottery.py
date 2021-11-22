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

new_list = []
name_list = []

for i in players:
    name_list.append(i['name'])

for params in players:
    for name, numbers in params.items():
        numbers_matched = list(lottery_numbers.intersection(set(numbers)))
        numbers_matched1 = 100 ** len(numbers_matched)
    new_list.append(numbers_matched1)

zip_func = dict(zip(name_list,new_list))

max_key = max(zip_func, key=zip_func.get)
print(f'{max_key} won {zip_func[max_key]}')