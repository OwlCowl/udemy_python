def hundred_list():
    nums = []
    i = 0
    while i<101:
        nums.append(f'{i}')
        i+=1
    final = '\n'.join(nums)
    return final

#generator funs
def generator_func():
    nums = []
    i = 0
    while i<100:
        yield i
        i += 1

g = generator_func()
print(next(g))
print(next(g))
print(list(g))

