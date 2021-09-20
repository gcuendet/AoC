#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2019/day/6

import argparse
from collections import defaultdict


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    return parser.parse_args()


def read_input(filepath):
    connectivity = defaultdict(list)
    with open(filepath, "r") as f:
        for l in f.readlines():
            (center, orbits) = l.strip().split(")")
            connectivity[center].append(orbits)
    return connectivity


distance = {"COM": 0}


def orbits(k, _map):
    for conn in _map[k]:
        distance[conn] = distance[k] + 1
        yield conn, distance[conn]


if __name__ == "__main__":
    args = parse_args()
    _map = read_input(args.input)

    number_of_orbits = 0
    list_of_name = ["COM"]
    index = 0
    while index < len(list_of_name):
        for name, o in orbits(list_of_name[index], _map):
            number_of_orbits += o
            list_of_name.append(name)
        index += 1
    print(number_of_orbits)
