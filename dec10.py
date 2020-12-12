#!/usr/bin/env python3
import collections
import itertools

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    return content

def dec10():
    adapters = [ int(n) for n in get_input("input/dec10.tmp") ]
    adapters.append(0)
    adapters.sort()
    diffs = []
    for k,v in enumerate(adapters):
        print(k,v)
        try:
            diffs.append(adapters[k + 1] - v)
        except IndexError:
            diffs.append(3)
    print(diffs)
    print(diffs.count(1) * diffs.count(3))
    return


    #for k,v in enumerate(a):
    #    diff = a[k + 1] - v§
    #for b,c in itertools.combinations(a, 2):
    #    print(b,c)
    for b,c in itertools.permutations(a,2):
        print(b,c)

if __name__ == '__main__':
    dec10()
