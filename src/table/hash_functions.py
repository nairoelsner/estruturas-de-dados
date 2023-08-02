def calculateHash(key, tableLength):
    return key % tableLength

def findNextPrimeNumber(n):
    primeNumbers = [2]
    i = 3
    while primeNumbers[-1] <= n:
        isPrime(i, primeNumbers)
        i += 1
    return primeNumbers[-1]

def isPrime(n, primeNumbers):
    for prime in primeNumbers:
        if n % prime == 0:
            return False
    primeNumbers.append(n)