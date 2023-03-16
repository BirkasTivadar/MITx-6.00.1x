"""
Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

Hints
Ideas about the problem
Have the generator keep a list of the primes it's generated. A candidate number x is prime if (x % p) != 0 for all earlier primes p.
"""


def genPrimes():
    nextPrime = 2
    primes = [2]
    yield nextPrime
    while True:
        isPrime = True
        nextPrime += 1
        for prime in primes:
            if nextPrime % prime == 0:
                isPrime = False
        if isPrime:
            yield nextPrime
            primes.append(nextPrime)
