isPrime = lambda n: reduce(lambda y,z: y and z, map(lambda c: False if n%c==0 else True, (i for i in range(2,n)))) if n>2 else True
primeFactors = lambda n: filter(lambda k: n%k==0 and isPrime(k), (x for x in range(2,n)))

n = int(raw_input())
print primeFactors(n)
