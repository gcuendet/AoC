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
inverted_connectivity = {}


def orbits(k, _map):
    for conn in _map[k]:
        distance[conn] = distance[k] + 1
        inverted_connectivity[conn] = k
        yield conn, distance[conn]


def path_to_com(k):
    path  = []
    _k = k
    while _k != "COM":
        next = inverted_connectivity[_k]
        path.append(next)
        _k=next
    return path


def part_1(input_path):
    _map = read_input(input_path)

    number_of_orbits = 0
    list_of_name = ["COM"]
    index = 0
    while index < len(list_of_name):
        for name, o in orbits(list_of_name[index], _map):
            number_of_orbits += o
            list_of_name.append(name)
        index += 1
    return number_of_orbits


def jumps(path1, path2):
    for el in path1:
        if el in path2:
            common_node = el
            break
    return path1.index(common_node) + path2.index(common_node)


def part_2():
    path1 = path_to_com("YOU")
    path2 = path_to_com("SAN")
    return jumps(path1, path2)    


if __name__ == "__main__":
    args = parse_args()
    print(part_1(args.input))
    print(part_2())