import time
import timeit


#decorator
def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end-start)


def powers(limit):
    return [x**2 for x in range(limit)]

measure_runtime(lambda: powers(5000000))

#return how long it will take to run
print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))



