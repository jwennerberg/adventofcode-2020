#!/usr/bin/env python3
import collections

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    return content

def next_val(val, change):
    if change.startswith("-"):
        return int(val) - int(change[1:])
    else:
        return int(val) + int(change[1:])

def dec08():
    instr = [ line.split() for line in get_input("input/dec08.tmp") ]
    accumulator = 0
    known_pos = []
    flipped = False
    pos = 0
    while True:
        if pos in known_pos:
            break
        i = instr[pos]
        print(i,pos)
        if i[0] == "acc":
            if (pos + 1) not in known_pos:
                accumulator = next_val(accumulator, i[1])
            np = pos + 1
        elif i[0] == "jmp":
            np = next_val(pos, i[1])
        elif i[0] == "nop":
            np = pos + 1
        else:
            print("Warning: unknown instruction")
        known_pos.append(pos)
        pos = np
    print(accumulator)

if __name__ == '__main__':
    dec08()
