#!/usr/bin/env python

def main():

    def findTriangleOfFactor(num):
        triangle = 1
        series = 2
        factors = []

        while(num > len(factors)):
            triangle += series
            series += 1
            factors = factor(triangle)
        return triangle

    def factor(num):
        primes = []
        for x in xrange(1, int(num ** (0.5) + 1)):
            if (num % x == 0):
                new = num / x
                if((not (x in primes)) and (not (new in primes))):
                    if(x == (new)):
                        primes.append(x)
                    else:
                        primes.append(x)
                        primes.append(new)
        return primes

    return findTriangleOfFactor(500)

if __name__ == '__main__':
    main()
