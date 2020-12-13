#!/usr/bin/env python3
import collections
import itertools
import math
from operator import itemgetter

def to_int(n):
    try:
        return int(n)
    except ValueError:
        return n

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    l = list(map(to_int, content[1].split(",")))
    return (int(content[0]),l)

def dec13():
    earliest,lines = get_input("input/dec13")
    departures = { (l * (math.ceil(earliest / l))): l for l in lines if l != "x" }
    next_dep = min(departures.keys())
    return departures[next_dep] * (next_dep - earliest)


if __name__ == '__main__':
    print(dec13())
