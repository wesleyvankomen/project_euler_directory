#!/usr/bin/env python
from datetime import datetime, timedelta

def timer(func):
    def time(*args, **kw):
        start = datetime.now()
        result = func(*args, **kw)
        end = datetime.now()
        run_time = str((end - start).total_seconds())
        print(func.__name__ + " ran in " + run_time + " seconds")
        return result
    return time


@timer
def calculate_primes(max):
    primes = [2]
    for num in xrange(3, max+1):
        prime = True
        for div in xrange(3, (int(num ** (0.5)) +1)):
            if((num % div) == 0):
                prime = False
                break
        if(prime):
            primes.append(num)
    return primes

@timer
def get_primes(max_prime = "million"):

    primes = []

    if max_prime:
        if max_prime == "billion":
            r = open('./primes_to_billion.txt', 'r')

        elif max_prime == "ten billion":
            r = open('./primes_to_ten_billion.txt', 'r')

        elif max_prime == "million":
            r = open('./primes_to_million.txt', 'r')

    else:
        r = open('./primes_to_million', 'r')

    try:
        for line in r:
            line = line.replace('[', '')
            line = line.replace(']', '')
            nums = line.split(',')
            for num in nums:
                primes.append(int(num))
    except:
        return False
    return primes

@timer
def isprime(num):
    if (num % 2 == 0):
        return False
    else:
        for x in xrange(3, (num ** .5)):
            if (num % x == 0):
                return False
        return True
@timer
def print_primes(file, max):
    printer = open(file, 'w')
    primes = calculate_primes(max)
    printer.write(str(primes))
    printer.close()

def main():
    print("----Running Euler Utility----")
    calculate_primes(10000)
    #print(len(get_primes("million")))
    #print(len(get_primes("billion")))
    #print_primes('primes_list_billion.txt', 1000000000)
    print"------Utility Complete------"
    #print_primes('primes_to_million.txt', 1000000)
if __name__ == "__main__":
    main()
