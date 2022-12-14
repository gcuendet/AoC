#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2022/day/1


def parse_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()


def compute_max_sums(input_numbers):
    _sum = 0
    _max_sums = [-1e25, -1e25, -1e25]
    for line in input_numbers:
        if line and line != "\n":
            _sum += int(line)
        else:
            if _sum > _max_sums[2]:
                _max_sums[2] = _sum
            if _sum > _max_sums[1]:
                _max_sums[2] = _max_sums[1]
                _max_sums[1] = _sum
            if _sum > _max_sums[0]:
                _max_sums[1] = _max_sums[0]
                _max_sums[0] = _sum
            _sum = 0
    return _max_sums


if __name__ == "__main__":
    sums = compute_max_sums(parse_input("input_01.txt"))
    print(sums)
    print(sum(sums))
