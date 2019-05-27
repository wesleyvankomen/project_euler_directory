#!/usr/bin/env python
print(
"""
If we list all the natural numbers below 10 that are multiples

of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of allthe multiples of 3 or 5 below 1000.
""")



def main():
    def multiples():
        sum = 0
        for x in range(0, 1000):
            if(x % 3 == 0):
                sum += x
            elif(x % 5 == 0):
                sum += x
            else:
                continue
        return sum
    return multiples()



if __name__ == '__main__':
    print ('Answer: ' + str(main()))
