from collections import defaultdict, OrderedDict, namedtuple, deque


def task1() -> defaultdict:
    unknown = defaultdict(lambda: 'Unknown')
    unknown['Allan'] = 'Manchester'
    return unknown

print(task1()['Allan'])

def task2(arg_od: OrderedDict):
    """
    - takes in an OrderedDict `arg_od`
    - Remove the first and last entry in `arg_od`.
    - Move the entry with key name `Bob` to the end of `arg_od`.
    - Move the entry with key name `Dan` to the start of `arg_od`.
    - You may assume that `arg_od` would always contain the keys `Bob` and `Dan`,
        and they won't be the first or last entry initially.
    """
    first = arg_od.popitem(last=False)
    last = arg_od.popitem(last=True)
    move_end = arg_od.move_to_end('Bob', last = True)
    move_first = arg_od.move_to_end('Bob', last = False)
    return arg_od

def task3(name: str, club: str) -> namedtuple:
    """
    - create a `namedtuple` with type `Player`, and it will have two fields, `name` and `club`.
    - create a `Player` `namedtuple` instance that has the `name` and `club` field set by the given arguments.
    - return the `Player` `namedtuple` instance you created.
    """
    Player = namedtuple('Player', ['name', 'club'])
    player_instance = Player(name, club)
    return player_instance

def task4(arg_deque: deque):
    """
    - Manipulate the `arg_deque` in any order you preferred to achieve the following effect:
        -- remove last element in `deque`
        -- move the fist (left most) element to the end (right most)
        -- add an element `Zack`, a string, to the start (left)
    """
    arg_deque.pop()  # remove last element
    arg_deque.append(arg_deque.popleft())  # remove first element and append it to last
    arg_deque.appendleft('Zack')  # add Zack to start



