#!/usr/bin/env python3
import collections
import itertools
import math
import re
from operator import itemgetter

def get_range(i):
    try:
        s,e = i.split("-")
        return list(range(int(s),int(e) + 1))
    except ValueError:
        return []

def get_ranges(r):
    return list(range(r[0], r[1] + 1)) + list(range(r[2], r[3] + 1))

def get_input_v2(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    data = {}
    all_tickets = []
    for l in content:
        d = []
        fields = re.match("^(\w+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$", l)
        if fields:
            data[fields.group(1)] = get_ranges(list(map(int, fields.groups()[1:])))
        tickets = re.match("^([0-9]+.*)$", l)
        if tickets:
            all_tickets.append(list(map(int, tickets.group(1).split(","))))
    myticket = all_tickets[0]
    nearby = all_tickets[1:]
    return {"fields": data, "myticket": myticket, "nearby": nearby}

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    data = {"nearby": [], "valid_nearby": []}
    d = []
    for k,l in enumerate(content):
        s = l.split(":")
        if s[0] in ("class","row","seat"):
            for r in map(get_range, s[1].strip().split(" ")):
                if r != None:
                    d += r
            data[s[0]] = d
        elif s[0] == "your ticket":
            data["ticket"] = list(map(int, content[k + 1].split(",")))
            skip = k + 1
        else:
            if l[:1].isdigit() and k != skip:
                data["nearby"].append(list(map(int, l.split(","))))
    return data

def dec16():
    t = get_input_v2("input/dec16.tmp")
    all_fields = [ f for fields in t["fields"].values() for f in fields ]
    nonvalid = { k:nv for k,n in enumerate(t["nearby"]) for nv in n if nv not in all_fields }
    print(sum(nonvalid.values()))
    valid = [ v for k,v in enumerate(t["nearby"]) if k not in nonvalid.keys() ] 
    print(valid)



if __name__ == '__main__':
    dec16()
