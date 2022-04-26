friends = ['Rolf', 'Jose', 'Ruin', 'Ola']
start_with_r = filter(lambda name: name.startswith('R'), friends)
print(list(start_with_r))

#generator comprehension
another_start_with_r = (name for name in friends if name.startswith('R'))
g = another_start_with_r
print(g)

#generator
def iterable_func(func, iterable):
    for i in iterable:
        if func(i):
            yield i

