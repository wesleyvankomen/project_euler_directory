#!/usr/bin/env python

def main():

    def collatz(num):
        highestValue = 0
        longest = 0
        chain = []
        for x in xrange(1, num):
            chain = produceChain(x)
            if(len(chain) > longest):
                longest = len(chain)
                highestValue = x
        return highestValue

    def produceChain(value):
        chain = [value]
        while(value != 1):
            if(value % 2 == 0):
                value = value / 2
            else:
                value = value * 3 + 1
            chain.append(value)
        return chain

    return collatz(1000000)

if __name__ == '__main__':
    main()
