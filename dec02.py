#!/usr/bin/env python3
import re

def get_input_from_file(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    return content

def dec02(indata='input/dec02'):
    valid1,valid2 = 0, 0
    for i in get_input_from_file(indata):
        a,p = i.split(':')
        b,char = a.split(' ')
        pwd = p.strip()
        lo,hi = map(int, b.split('-'))
        m = pwd.count(char)
        valid_pos = [ vp.end() for vp in re.finditer(char, pwd) ]
        valid1 += m >= lo and m <= hi
        valid2 += (lo in valid_pos and hi not in valid_pos) or (hi in valid_pos and lo not in valid_pos)
    print(valid1)
    print(valid2)

if __name__ == '__main__':
    dec02()
