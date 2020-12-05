#!/usr/bin/env python3
import re

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().split("\n\n")
    return content

def dec04():
    n_valid_fields = 0
    n_valid_data = 0
    fields = {'byr': { 'regexp': '^[0-9]{4}$', 'min': 1920, 'max': 2002 },
            'iyr': { 'regexp': '^[0-9]{4}$', 'min': 2010, 'max': 2020 },
            'eyr': { 'regexp': '^[0-9]{4}$', 'min': 2020, 'max': 2030 },
            'hgt': { 'regexp': '^[0-9]+(cm|in)$', 'min': { 'cm': 150, 'in': 59 }, 'max': { 'cm': 193, 'in': 76 } },
            'hcl': { 'regexp': '^#[0-9a-f]{6}$' },
            'ecl': { 'regexp': '^(amb|blu|brn|gry|grn|hzl|oth)$' },
            'pid': { 'regexp': '^[0-9]{9}$' } }

    passport_data = [ i.replace('\n',' ').strip().split(' ') for i in get_input("input/dec04") ]
    for p in passport_data:
        pd = {}
        f_match = 0
        for f in p:
            k,v = f.split(':', 1)
            if k != "cid":
                pd[k] = v
        if set(pd.keys()) == set(fields.keys()):
            n_valid_fields += 1
            for k in pd.keys():
                if re.match(fields[k]['regexp'], pd[k]) == None:
                    continue
                if k == 'hgt':
                    s = re.search('^([0-9]+)([a-z]{2})$', pd[k])
                    f_match += int(s.group(1)) >= fields[k]['min'][s.group(2)] and int(s.group(1)) <= fields[k]['max'][s.group(2)]
                else:
                    if 'min' in fields[k].keys() and 'max' in fields[k].keys():
                        f_match += int(pd[k]) >= fields[k]['min'] and int(pd[k]) <= fields[k]['max']
                    else:
                        f_match += 1
            n_valid_data += f_match == len(pd.keys())
    print(n_valid_fields)
    print(n_valid_data)

if __name__ == '__main__':
    dec04()
