#!/usr/bin/env python
from datetime import datetime, timedelta
import euler

def print_line(len):
    for x in range(0,len):
        print('-')

# decorator function that displays the time taken to execute
def timer(func):
    def time(*args, **kw):
        start = datetime.now()
        result = func(*args, **kw)
        end = datetime.now()
        run_time = str((end - start).total_seconds())
        print(func.__name__ + " ran in " + run_time + " seconds")
        return result
    return time

# improved prime calculation algorithm
@timer
def calculate_primes(max):
    # helper function for trial calculation algorithm
    def check_prime(num):
        if num % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    primes = [2, 3]
    for num in xrange(5, max+1, 2):
        if check_prime(num):
            primes.append(num)
    return primes

# returns all the primes upto the input value
@timer
def calculate_primes_classic(max):
    primes = [2]
    for num in xrange(3, max+1, 2):
        prime = True
        for div in xrange(3, (int(num ** (0.5)) +1)):
            if((num % div) == 0):
                prime = False
                break
        if(prime):
            primes.append(num)
    return primes

# uses pre-calculated list of primes upto million, billion, or ten billion
@timer
def get_primes(max_prime = "million"):

    primes = []

    if max_prime == "billion":
        r = open('./prime/primes_to_billion.txt', 'r')

    else:
        r = open('./primes/primes_to_million.txt', 'r')

    try:
        for line in r:
            line = line.replace('[', '')
            line = line.replace(']', '')
            nums = line.split(',')
            for num in nums:
                primes.append(int(num))
    except:
        print('could not find file to open')
        return False
    return primes

#checks to see if a single number is a prime.
@timer
def is_prime(num):
    #select the most efficient prime list to check
    if num < 1000000:
        primes = (get_primes("million"))
    elif num < 1000000000:
        primes = get_primes("billion")
    else:
        print('that number is too big!')
    #check if number is in selected prime list
    if num in primes:
        return True
    else:
        return False

# uses print_primes to repopulate main 3 prime number files
# -WARNING- this may take a long time to compute
def make_prime_files():
    print_primes('primes/primes_to_million.txt', 1000000)
    print_primes('primes/primes_to_billion.txt', 1000000000)

# use this function to print a new list of prime numbers to a specified file.
def print_primes(file, max):
    printer = open(file, 'w')
    primes = calculate_primes(max)
    printer.write(str(primes))
    printer.close()

# main method will make prime files
def main():
    print("----Running Euler Utility----")

    print(get_primes())

    print"------Utility Complete------"
if __name__ == "__main__":
    main()
