#!/usr/bin/env python3
import collections
import itertools

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    return content

def find_adjecent(seat_id, adjrows):
    print(seat_id,adjrows)
    rid = seat_id[0]
    sid = seat_id[1]
    r = adjrows[rid]
    nb = []
    if sid == 0:
        s_start = sid
        s_end = sid + 2
    elif sid == len(r) - 1:
        s_start = sid - 1
        s_end = sid + 1
    else:
        s_start = sid - 1
        s_end = sid + 2

    if len(adjrows) == 2:
        # first row
        if rid == 0 and s_end != sid:
            nb += adjrows[rid+1][s_start:s_end]
        # last row
        if rid == 1 and s_start != sid:
            nb += adjrows[rid-1][s_start:s_end]
    else:
        nb += adjrows[rid-1][s_start:s_end]
        nb += adjrows[rid+1][s_start:s_end]

    nb += r[s_start:s_end]
    nb.remove(r[sid])
    print("neighbors",nb)
    return nb

def find_first_seat(o, seat_id, seats):
    rid,sid = seat_id
    valid_s = ["#","L"]
    s = None
    print(s)
    while s not in valid_s:
        if o in ["r","l"]:
            if o == "r":
                sid += 1
            else:
                sid -= 1
            s = seats[sid]
        else:
            if "u" in o:
                rid -= 1
            elif "d" in o:
                rid += 1
            elif "r" in o:
                sid += 1
            elif "l" in o:
                sid -= 1
            s = seats[rid][sid]
    print("sssss",s)


def find_first_adjecent(seat_id, rows):
    print(seat_id,rows)
    rid,sid = seat_id
    r = rows[rid]
    nb = []
    l_left = False if sid == 0 else True
    l_right = False if sid == len(r) - 1 else True
    l_up = False if rid == 0 else True
    l_down = False if rid == len(rows) - 1 else True

    if l_right:
        nb += find_first_seat("r",seat_id,r)
    if l_down:
        nb += find_first_seat("d",seat_id,rows)
    return

    if sid == 0:
        s_start = sid
        s_end = sid + 2
    elif sid == len(r) - 1:
        s_start = sid - 1
        s_end = sid + 1
    else:
        s_start = sid - 1
        s_end = sid + 2

    if len(rows) == 2:
        # first row
        if rid == 0 and s_end != sid:
            nb += rows[rid+1][s_start:s_end]
        # last row
        if rid == 1 and s_start != sid:
            nb += rows[rid-1][s_start:s_end]
    else:
        nb += rows[rid-1][s_start:s_end]
        nb += rows[rid+1][s_start:s_end]

    nb += r[s_start:s_end]
    nb.remove(r[sid])
    print("neighbors",nb)
    return nb


def dec11():
    rows = [ list(r) for r in get_input("input/dec11.tmp") ]
    prev_seatmap = []
    new_rows = rows.copy()
    while True:
        new_seatmap = []
        for rk,r in enumerate(rows):
            #print("seats:",r)
            new_rows[rk] = r.copy()
            for sk,s in enumerate(r):
                if s == ".":
                    continue
                if rk == 0:
                    arows = (r,rows[rk+1])
                    ark = 0
                elif rk == len(rows) - 1:
                    arows = (rows[rk-1],r)
                    ark = 1
                else:
                    arows = (rows[rk-1],r,rows[rk+1])
                    ark = 1
                a = find_first_adjecent((ark,sk),arows)
                return
                if s == "L" and a.count("#") == 0:
                    new_rows[rk][sk] = "#"
                if s == "#" and a.count("#") >= 4:
                    new_rows[rk][sk] = "L"
            new_seatmap += new_rows[rk]

        if prev_seatmap == new_seatmap:
            break
        prev_seatmap = new_seatmap.copy()
        rows = new_rows.copy()
    print(new_seatmap.count("#"))


if __name__ == '__main__':
    dec11()

