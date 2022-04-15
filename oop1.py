my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99]
}


def average_grade(student):
    return sum(student['grades'])/len(student['grades'])

print(average_grade(my_student))

class Movie():
    def __init__(self, director, name):
        self.director = director
        self.name = name

    def print_info(self):
        return f'{self.name} by {self.director}'

my_movie = Movie('The Matrix', 'Wachowski')
my_movie.print_info()

class Garage():
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

Lubos = Garage()
Lubos.cars.append('Ford')
Lubos.cars.append('Fiesta')
print(Lubos[1])
print(len(Lubos))


# We have a class called Club, and it is initialized like this (no need to change):
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __len__(self):
        return len(self.players)

    def __getitem__(self, item):
        return self.players[item]

    def __repr__(self):
        return f'Club {self.name}: {self.players}'

    def __str__(self):
        return f'Club {self.name} with {len(self)} players'








