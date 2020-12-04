#!/usr/bin/env python3

def get_input_from_file(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    return content

def dec01_1():
    i = list(map(int, get_input_from_file("input/dec01")))
    for a in i:
        b = 2020 - a
        if b in i:
            return a * b
    return None

def dec01_2():
    i = list(map(int, get_input_from_file("input/dec01")))
    for a in i:
        for aa in i:
            b = 2020 - (a + aa)
            if b in i:
                return a * aa * b
    return None

if __name__ == '__main__':
    print(dec01_1())
    print(dec01_2())
