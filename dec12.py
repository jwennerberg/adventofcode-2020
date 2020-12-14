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

def new_pos(pos, waypoint, steps):
    for k in waypoint.keys():
        pos[k] += (waypoint[k] * steps)
    return pos

def new_waypoint(wp, direction, steps):
    new_wp = wp.copy()
    opp_dir = new_direction(direction,"L",180)
    for k in wp.keys():
        if k == direction:
            new_wp[k] = wp[k] + steps
        elif k == opp_dir:
            if wp[opp_dir] >= steps:
                new_wp[opp_dir] = wp[opp_dir] - steps
            else:
                new_wp[direction] = steps - wp[opp_dir]
                new_wp.pop(opp_dir, None)
    return new_wp

def rotate_waypoint(wp, turn, degrees):
    new_wp = {}
    for k in wp.keys():
        d = new_direction(k, turn, degrees)
        new_wp[d] = wp[k]
    return new_wp

def dec12():
    nav = [ (i[0],int(i[1:])) for i in get_input("input/dec12") ]
    pos = {"E":0,"W":0,"N":0,"S":0}
    pos2 = pos.copy()
    direction = "E"
    wp = {"E":10,"N":1}
    for a,v in nav:
        if a == "F":
            pos[direction] += v
            pos2 = new_pos(pos2, wp, v)
        elif a == "R" or a == "L":
            direction = new_direction(direction, a, v)
            wp = rotate_waypoint(wp, a, v)
        else:
            pos[a] += v
            wp = new_waypoint(wp, a, v)
    ew = max((pos["E"],pos["W"])) - min((pos["E"],pos["W"]))
    ns = max((pos["N"],pos["S"])) - min((pos["N"],pos["S"]))
    ew2 = max((pos2["E"],pos2["W"])) - min((pos2["E"],pos2["W"]))
    ns2 = max((pos2["N"],pos2["S"])) - min((pos2["N"],pos2["S"]))
    print(ew + ns)
    print(ew2 + ns2)

if __name__ == '__main__':
    dec12()
