#!/usr/bin/env python3

def get_input_from_file(input_file):
    with open(input_file, "r") as f:
        content = f.read().split("\n\n")
    return content

def dec04():
    valid = 0
    all_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
    required = list(all_fields)
    required.remove('cid')

    passport_data = [ i.replace('\n',' ').strip().split(' ') for i in get_input_from_file("input/dec04") ]
    for p in passport_data:
        pd = {}
        for f in p:
            k,v = f.split(':', 1)
            pd[k] = v
        fields = set(pd.keys())
        if "cid" in fields:
            fields.remove("cid")
        valid += fields == set(required)
    return valid

if __name__ == '__main__':
    print(dec04())
