#!/usr/bin/env python3
import urllib.request
import re

def get_input_from_file(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    return content

def dec03(steps_right=3, steps_down=1):
    trees,hz_pos,vt_pos = 0,0,0
    pmap = [ list(i) for i in get_input_from_file("input/dec03") ]

    for i, row in enumerate(pmap[steps_down:]):
        if i == vt_pos:
            max_pos = len(row)-1
            if hz_pos+steps_right > max_pos:
                steps_left = max_pos - hz_pos
                hz_pos = steps_right - steps_left - 1
            else:
                hz_pos += steps_right
            trees += row[hz_pos] == "#"
            vt_pos = i + steps_down
    return trees


if __name__ == '__main__':
    print(dec03(3,1))

    s1 = dec03(1,1)
    s2 = dec03(3,1)
    s3 = dec03(5,1)
    s4 = dec03(7,1)
    s5 = dec03(1,2)
    print(s1 * s2 * s3 * s4 * s5)
