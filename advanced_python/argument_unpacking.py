accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}

def add_balance(amount: float, name: str) -> float:
    """Function to update the balance of an account and return the new balance."""
    accounts[name] += amount
    return accounts[name]

"""
Imagine we’ve got a list of transactions that we’ve downloaded from our bank page; and they look somewhat like this:
"""

transactions = [
  (-180.67, 'checking'),
  (-220.00, 'checking'),
  (220.00, 'savings'),
  (-15.70, 'checking'),
  (-23.90, 'checking'),
  (-13.00, 'checking'),
  (1579.50, 'checking'),
  (-600.50, 'checking'),
  (600.50, 'savings'),
]

"""
If we now wanted to add them all to our accounts, we’d do something like this:
"""

for t in transactions:
    add_balance(t[0], t[1])


""" or as option"""
for t in transactions:
    add_balance(*t)  # passes each element of t as an argument in order

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

users = [
    { 'username': 'rolf', 'password': '123' },
    { 'username': 'tecladoisawesome', 'password': 'youaretoo' }
]

user_objects = map(User.from_dict, users)


"""
The option of using a list comprehension is slightly uglier, I feel:
"""

user_objects = [User.from_dict(u) for u in users]


#refactor class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

#use unpacking, because of users is dict use **
user = [User(**data) for data in users]

"""
If our data was not in dictionary format, like tuple here, we could do:
"""

users = [
    ('rolf', '123'),
    ('tecladoisawesome', 'youaretoo')
]

user_objects = [User(*data) for data in users]

