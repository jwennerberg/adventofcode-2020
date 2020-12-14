#!/usr/bin/env python3
import collections
import itertools
import math
import re
import itertools
from operator import itemgetter

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    return content

def get_combinations(bits):
    comb = []
    for i in list(itertools.product([0,1], repeat=bits.count("X"))):
        s = "".join(bits)
        for ii in i:
            s = s.replace("X",str(ii), 1)
        comb.append(int("".join(s),2))
    return comb

def decode(bitmask, value):
    vb = format(value,"b").zfill(36)
    result = list(vb)
    for k,v in enumerate(bitmask):
        if v == "X":
            continue
        result[int(k)] = v
    return int("".join(result),2)

def decode_v2(bitmask, value):
    vb = format(value,"b").zfill(36)
    result = list(vb)
    for k,v in enumerate(bitmask):
        if v == "X":
            result[k] = v
        elif int(v) == 0:
            continue
        else:
            result[int(k)] = v
    return get_combinations(result)

def dec14():
    lines = get_input("input/dec14")
    mem,mem2 = {},{}
    for l in lines:
        k,v = l.partition("=")[::2]
        v = v.strip()
        if k.startswith("mem"):
            addr = re.search("mem\[([0-9]*)\].*", k).group(1)
            result = decode(mask,int(v))
            result2 = decode_v2(mask,int(addr))
            mem[addr] = result
            for m in result2:
                mem2[m] = int(v)
        else:
            mask = v.strip()
    print(sum(mem.values()))
    print(sum(mem2.values()))

if __name__ == '__main__':
    dec14()
