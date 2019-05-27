#!/usr/bin/env python

def main():

    def findPrime(num):
        primeSum = 2
        current = 3
        while(current < num):
            add = checkPrime(current)
            if(add):
                primeSum += current
            current += 2
        return primeSum

    def checkPrime(num):
        for x in xrange(3, (int(num ** (0.5) + 1))):
            if(num % x == 0):
                return False

        return True

    return findPrime(2000000)

if __name__ == '__main__':
    main()


