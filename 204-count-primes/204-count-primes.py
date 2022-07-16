class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True]*n
        i = 2
        count = 0
        while i*i < n:
            if primes[i]:
                j = i
                while j*i < n:
                    primes[j*i] = False
                    j += 1
            i += 1
        for i in range(2, len(primes)):
            if primes[i]:
                count += 1
        return count