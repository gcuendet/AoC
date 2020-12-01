#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2019/day/1

# input: https://adventofcode.com/2019/day/1/input

import math
from codetiming import Timer


def read_input(filepath="01_input.txt"):
    with open(filepath, "r") as f:
        lines = f.readlines()
    return [int(l) for l in lines]


def product_of_sum(items, target=2020):
    for i in items:
        if (target - i) in items:
            return i * (target - i)
    

@Timer()
def part_one():
    items = read_input()
    return product_of_sum(items)
    

@Timer()
def part_two():
    items = read_input()
    for i in items:
        sol = product_of_sum([el for el in items if el != i], target=(2020-i))
        if sol:
            return i * sol


if __name__ == "__main__":
    print(part_one())
    print(part_two())
