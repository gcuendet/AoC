#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2019/day/1

# input: https://adventofcode.com/2019/day/1/input

import math
import urllib.request


def get_input(url, encoding="utf-8"):
    return [line.decode(encoding) for line in urllib.request.urlopen(url)]


def read_input(filepath):
    with open(filepath, 'r') as f:
        return [int(module) for module in f.readlines()]

def fuel_requirement(module_mass):
    return math.floor(module_mass / 3.) - 2


def part_one():
    lines = read_input("01_input.txt")
    total_fuel = 0
    for module in lines:
        total_fuel += fuel_requirement(module)
    return total_fuel


def part_two():
    lines = read_input("01_input.txt")
    total_fuel = 0
    for module in lines:
        fuel = fuel_requirement(module)
        while(fuel>0):
            total_fuel+=fuel
            fuel = fuel_requirement(fuel)
    return total_fuel

if __name__ == "__main__":
    print(part_one())
    print(part_two())
    
