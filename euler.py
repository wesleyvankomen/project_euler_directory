#!/usr/bin/env python
import os
import re

def main():

    #populate a list of available projects to run
    available = []
    files = []
    for file in os.listdir("complete"):
        num = re.findall(r'\d+', file)

        if(num):
            files.append(file)
            if not int(num[0]) in available:
                available.append(int(num[0]))

    available.sort()

    running = True

    while(running):

        display = str(available).strip('[]')
        print('The following projects can be run: %s' % display)

        command = raw_input("enter the problem number to run it\n")

        if int(command) in available:
            file = 'complete/problem_' + command + '.py'
            print(file)
            print(os.system(file))

        else:
            print("that problem could not be found!")


if (__name__ == "__main__"):
    main()

