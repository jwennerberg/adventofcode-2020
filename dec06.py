#!/usr/bin/env python3
import collections

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().split("\n\n")
    return content

def dec06():
    n_yes = 0
    n_all_yes = 0
    for i in get_input("input/dec06"):
        g = i.replace("\n", "")
        n_yes += len(set(g))
        answers = collections.Counter(list(g))
        for k in answers:
            if answers[k] == len(i.splitlines()):
                n_all_yes += 1
    print(n_yes)
    print(n_all_yes)


if __name__ == '__main__':
    dec06()
