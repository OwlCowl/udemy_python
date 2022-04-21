# Ask a user for a list of 3 friends
# For each friend we will tell if they are nearby
# For each friends in the same city we will save them in 'nearby_friends.txt'

#hint: readlines()

user_input = input('Please input your three friends: ')

with open('people.txt') as openfile:
    nearby_friends = open('nearby_friends.txt', 'w')
    for line in openfile:
        for part in line:
            search = [word for word in user_input.split(",")]
            if part in user_input:
                nearby_friends.write(part)
    nearby_friends.close()
openfile.close()


#Second option
friends = input('Enter three friend names, separated by commas (no spaces, please): ').split(',')

people = open('people.txt', 'r')
#strip to delete all symbols before and after
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()








