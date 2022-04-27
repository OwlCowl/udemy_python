#iterator - but not iterable
#iterator - get next value, iterable - go over all the values of the iterator
# Generator = Iterator
# Iterator != Generator

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    #to make italso iterable object and then we may delete FirstHundredGenerato
    def __iter__(self):
        return self

my_gen = FirstHundredGenerator()
# print(my_gen.number)
# my_gen.__next__()
# print(my_gen.number)


class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()

# iterable when object had __iter__(self)
print(sum(FirstHundredIterable()))
print(sum(FirstHundredGenerator()))
# for i in FirstHundredIterable():
#     print(i)

#iterables = if have __iter__, __len__ and __getitem__
