class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop # stop defines the range (exclusive upper bound) in which we search for the primes
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):   # n starts from 2 to bound
            for x in range(2, n):   # check if there is a number x (1<x<n) that can divide n
                if n % x == 0:  # as long as we can find any such x, then n is not prime
                    break
            else:
                self.start = n + 1 # if no such x is found after exhausting all 1<x<n
                return n     # generate this prime
            raise StopIteration()