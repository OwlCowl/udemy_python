""" Concerning books
[
    {
    'name': 'Clean',
    'author': 'Robert Hey',
    'read': True
    }
]
"""
import json

books_file = 'books.json'


def create_book_table():
    with open(books_file, 'w') as file:
        return json.dump([], file)


def get_all_books():
    with open(books_file, 'r') as file:
        #json is a list
        return json.load(file)


#open json and write book in it
def add_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books()

