#!/usr/bin/env python3
import collections
import itertools
import math
from operator import itemgetter

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().split(",")
    return list(map(int, content))

def dec15_v2(n_number = 30000000):
    starting_n = get_input("input/dec15")
    n = starting_n[-1]
    numbers = { n:k for k,n in enumerate(starting_n[:-1]) }
    for i in range(len(numbers),n_number):
        last = n
        if n in numbers.keys():
            diff = i - numbers[n]
            numbers[n] = i
            n = diff
        else:
            numbers[n] = i
            n = 0
    print(last)

def dec15():
    starting_n = get_input("input/dec15.tmp")
    spoken = starting_n.copy()
    for i in range(len(starting_n),300000):
        last = spoken[-1]
        if spoken.count(last) == 1:
            spoken.append(0)
        else:
            ind = [ k for k,v in enumerate(spoken) if v == last ]
            diff = ind[-2:][1] - ind[-2:][0]
            spoken.append(diff)
    print(spoken[-1])

if __name__ == '__main__':
    dec15_v2(2020)
    dec15_v2(30000000)
