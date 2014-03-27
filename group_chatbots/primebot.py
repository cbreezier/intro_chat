import re, math

user, message = raw_input().split(':')

if '@primebot' in message:
  matches = re.search('([0-9]+)', message)
  if matches:
    maxPrime = int(matches.group(1))
    rootMax = int(math.sqrt(maxPrime))
    primes = [i for i in range(2, maxPrime + 1)]
    for p in range (2, rootMax):
      if p in primes:
        primes = [i for i in primes if i == p or i % p != 0]
    print primes
  else:
    print "@"+user, "That's not a valid number..."
