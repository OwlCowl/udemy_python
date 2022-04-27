# def greet():
#     print('Hello')
#
#
# def before_and_after(func):
#     print('Before')
#     func()
#     print('After')
#
#
#
# before_and_after(lambda: 5)
# before_and_after(greet)

movies = [{"name": "Rodney", "director": "Dangerfield"},
          {"name": "Still", "director": "Standing"},
          {"name": "Back", "director": "Midnight"}]

def find_movie(looking_for: str, finder):
    found = []
    for movie in movies:
        if finder(movie) == looking_for:
            found.append(movie)
    return found


find_by = input("What property are we searching by? ")
looking_for = input("What are you looking for? ")
movies = find_movie(looking_for, lambda movie: movie[find_by])
print(movies or 'Not find')

