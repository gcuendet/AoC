#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2020/day/3

# input: https://adventofcode.com/2020/day/3/input


def read_input(filepath="03_input.txt"):
    terrain_map = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            terrain_map.append([True if el == "#" else False for el in line])
    return terrain_map


def count_trees(terrain_map, slope_num=1, slope_denum=3):
    x = 0
    trees = 0
    map_width = len(terrain_map[0])
    for y, line in enumerate(terrain_map[::slope_num]):
        if line[(x + slope_denum * y) % (map_width - 1)]:
            trees += 1
    return trees


def part_one():
    terrain_map = read_input()
    return count_trees(terrain_map)


def part_two():
    terrain_map = read_input()
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    prod = 1
    for slope_num, slope_denum in slopes:
        prod *= count_trees(terrain_map, slope_num, slope_denum)
    return prod


if __name__ == "__main__":
    print(part_one())
    print(part_two())
