#!/usr/bin/env python3
import re

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().split("\n\n")
    return content

def dec06():
    n_yes = 0
    for i in get_input("input/dec06"):
        n_yes += len(set(i.replace("\n","")))
    print(n_yes)


if __name__ == '__main__':
    dec06()
