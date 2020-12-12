#!/usr/bin/env python3
import collections
import itertools

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    return content

def new_direction(current_dir, turn, degrees):
    directions = ("E","S","W","N")
    old_idx = directions.index(current_dir)
    steps = int(degrees / 90)
    if turn == "R":
        if old_idx + steps > len(directions) - 1:
            new_idx = old_idx + steps - len(directions)
        else:
            new_idx = old_idx + steps
    else:
        new_idx = old_idx - steps
    return directions[new_idx]

def dec12():
    nav = [ (i[0],int(i[1:])) for i in get_input("input/dec12") ]
    pos = {"E":0,"W":0,"N":0,"S":0}
    direction = "E"
    for a,v in nav:
        if a == "F":
            pos[direction] += v
        elif a == "R" or a == "L":
            direction = new_direction(direction, a, v)
        else:
            pos[a] += v
    if pos["E"] > pos["W"]:
        ew = pos["E"] - pos["W"]
    else:
        ew = pos["W"] - pos["E"]
    if pos["N"] > pos["S"]:
        ns = pos["N"] - pos["S"]
    else:
        ns = pos["S"] - pos["N"]
    return ew + ns


if __name__ == '__main__':
    print(dec12())

