import re, math

user, message = raw_input().split(':')

if '@primebot' in message:
    matches = re.search('([0-9j]+)', message)
    if matches:
        maxPrime = int(matches.group(1))
        sieve = [1 for i in range(maxPrime + 1)]
        rootMax = math.sqrt(maxPrime)

        p = 2
        while p <= rootMax:
          i = 2
          while i * p <= maxPrime:
            sieve[i * p] = 0
            i += 1

          p += 1
          while sieve[p] == 0:
            p += 1

        primes = filter(lambda x: sieve[x] == 1, range(2, maxPrime + 1))
        print primes
