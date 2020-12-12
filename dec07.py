#!/usr/bin/env python3
import re
import collections

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    return content

def find_bags(all_bags, name, parent=None):
    try:
        bags_to_check = all_bags[name]["bags"]
    except KeyError:
        print(name, "contains no bags")
        return
    for c in bags_to_check:
        print(c,parent)
        find_bags(all_bags, c[1], name)
        #print(c2)
        #total += c[0] * c2["total"]
        #print("total += %d * %d" % (c[0],c2["total"]))
        #more_bags_to_check += c2["bags"]


def dec07():
    can_contain = {}
    contains = {}
    for i in get_input("input/dec07"):
        r = re.match("^(.*) bags contain (.*)$", i)
        if r.group(2).startswith("no"):
            pass
        else:
            ob = []
            total = 0
            for o in r.group(2).split(","):
                ob_m = re.match("([0-9]*) ([\w]+ [\w]+) .*$", o.strip())
                try:
                    can_contain[ob_m.group(2)].append(r.group(1))
                except KeyError:
                    can_contain[ob_m.group(2)] = [r.group(1)]
                try:
                    total += int(ob_m.group(1))
                    contains[r.group(1)]["bags"].append([int(ob_m.group(1)),ob_m.group(2)])
                    contains[r.group(1)]["total"] = total
                except KeyError:
                    contains[r.group(1)] = {"bags": [ [int(ob_m.group(1)),ob_m.group(2)] ], "total": int(ob_m.group(1))}

    n1 = can_contain["shiny gold"]
    n2,n3,n4,n5,n6,n7,n8,n9 = [],[],[],[],[],[],[],[]
    #print(n1,len(n1))
    #print("------------------")
    c1 = contains["shiny gold"]
    print(c1)
    #print(contains["dotted magenta"])
    print("------------------")
    find_bags(contains, "shiny gold")
    return

    more_bags_to_check = []
    even_more_bags_to_check = []
    total = 1
    levels = {}
    for c in c1["bags"]:
        print(c)
        c2 = contains[c[1]]
        print(c2)
        #total += c[0] * c2["total"]
        #print("total += %d * %d" % (c[0],c2["total"]))
        more_bags_to_check += c2["bags"]
        #print(total)
    print(more_bags_to_check)
    print("----------------------")
    for c in more_bags_to_check:
        print(c)
        if c[1] in contains.keys():
            c2 = contains[c[1]]
            print(c2)
            #print("total += %d * %d" % (c[0],c2["total"]))
            even_more_bags_to_check += c2["bags"]
        else:
            print(c[1],"no_bags")
    print(even_more_bags_to_check)



    print(total)
    return
    more_bags = []
    while len(set(prev)) == len(set(n_bags)):
        for n in n1:
            if n in bags.keys():
                n2 += bags[n]
    return
    for m in n2:
        if m in bags.keys():
            n3 += bags[m]
    for m in n3:
        if m in bags.keys():
            n4 += bags[m]
    for m in n4:
        if m in bags.keys():
            n5 += bags[m]
    for m in n5:
        if m in bags.keys():
            n6 += bags[m]
    for m in n6:
        if m in bags.keys():
            n7 += bags[m]
    for m in n7:
        if m in bags.keys():
            n8 += bags[m]
    for m in n8:
        if m in bags.keys():
            n9 += bags[m]
    print(n2,len(set(n2 + n1)))
    print(n3,len(set(n3 + n2 + n1)))
    print(n4,len(set(n4 + n3 + n2 + n1)))
    print(n5,len(set(n5 + n4 + n3 + n2 + n1)))
    print(n6,len(set(n6 + n5 + n4 + n3 + n2 + n1)))
    print(n7,len(set(n7 + n6 + n5 + n4 + n3 + n2 + n1)))
    print(n8,len(set(n8 + n7 + n6 + n5 + n4 + n3 + n2 + n1)))
    print(n9,len(set(n9 + n8 + n7 + n6 + n5 + n4 + n3 + n2 + n1)))
    #print(len(set(more_bags)))

def dec07_bak():
    bags = {}
    for i in get_input("input/dec07"):
        r = re.match("^(.*) bags contain (.*)$", i)
        if r.group(2).startswith("no"):
            pass
        else:
            ob = []
            for o in r.group(2).split(","):
                ob_m = re.match("([0-9]*) ([\w]+ [\w]+) .*$", o.strip())
                try:
                    bags[ob_m.group(2)].append(r.group(1))
                except KeyError:
                    bags[ob_m.group(2)] = [r.group(1)]
    n1 = bags["shiny gold"]
    n2,n3,n4,n5,n6,n7,n8,n9 = [],[],[],[],[],[],[],[]
    print(n1,len(n1))
    more_bags = []
    for n in n1:
        if n in bags.keys():
            #more_bags += bags[n]
            #print(n,len(bags[n]))
            #print(bags[n])
            n2 += bags[n]
    print("n111111")
    for m in n2:
        if m in bags.keys():
            n3 += bags[m]
    for m in n3:
        if m in bags.keys():
            n4 += bags[m]
    for m in n4:
        if m in bags.keys():
            n5 += bags[m]
    for m in n5:
        if m in bags.keys():
            n6 += bags[m]
    for m in n6:
        if m in bags.keys():
            n7 += bags[m]
    for m in n7:
        if m in bags.keys():
            n8 += bags[m]
    for m in n8:
        if m in bags.keys():
            n9 += bags[m]
    print(n2,len(set(n2 + n1)))
    print(n3,len(set(n3 + n2 + n1)))
    print(n4,len(set(n4 + n3 + n2 + n1)))
    print(n5,len(set(n5 + n4 + n3 + n2 + n1)))
    print(n6,len(set(n6 + n5 + n4 + n3 + n2 + n1)))
    print(n7,len(set(n7 + n6 + n5 + n4 + n3 + n2 + n1)))
    print(n8,len(set(n8 + n7 + n6 + n5 + n4 + n3 + n2 + n1)))
    print(n9,len(set(n9 + n8 + n7 + n6 + n5 + n4 + n3 + n2 + n1)))
    #print(len(set(more_bags)))

if __name__ == '__main__':
    dec07()
