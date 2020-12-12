#!/usr/bin/env python3
import collections

def get_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().splitlines()
    return content

def sum_exists(nums, n):
    for i in nums:
        p = n - i
        if p in nums:
            return True
    return False

def dec09():
    preamble_size = 25
    numbers = [ int(n) for n in get_input("input/dec09") ]
    pp = numbers[:preamble_size]

    for n in numbers[preamble_size:]:
        p = pp[-preamble_size:]
        if sum_exists(p, n):
            pp.append(n)
        else:
            invalid_n = n
            break
    print(invalid_n)

    for k,n in enumerate(numbers):
        i,sum_i = [n],n
        while sum_i < invalid_n:
            k += 1
            sum_i += numbers[k]
            i.append(numbers[k])
        if sum_i == invalid_n:
            break
    print(min(i) + max(i))


if __name__ == '__main__':
    dec09()
