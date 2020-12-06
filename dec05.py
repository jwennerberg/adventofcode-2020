#!/usr/bin/env python3
import re

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    return content

def dec05():
    seat_ids = []
    all_seats = list(range(128 * 8))
    for i in get_input("input/dec05"):
        start,end = 0,127
        for pos,char in enumerate(i):
            section_size = end - start
            if char in ["F","L"]:
                end -= (section_size + 1) / 2
            elif char in ["B","R"]:
                start += (section_size + 1) / 2
            if pos == 6:
                row = end
                start,end = 0,7
        column = end
        seat_ids.append(int(row * 8 + column))

    for s in list(set(all_seats) - set(seat_ids)):
        if (s - 1) in seat_ids and (s + 1) in seat_ids:
            my_seat = s

    print(max(seat_ids))
    print(my_seat)

if __name__ == '__main__':
    dec05()
