#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2022/day/3


def parse_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()


def duplicated_item(a, b):
    return "".join(set(a).intersection(set(b)))


def common_item(a, b, c):
    return "".join(set(a).intersection(set(b)).intersection(set(c)))


def convert_ascii_to_priority(val):
    if val >= 97:
        return val - 96
    else:
        return val - 64 + 26


def solve(rucksacks):
    total_priority = 0
    for r in rucksacks:
        s = int(len(r) / 2)
        ascii_val = ord(duplicated_item(r[:s], r[s:]))
        total_priority += convert_ascii_to_priority(ascii_val)
    return total_priority


def solve_B(rucksacks):
    total_priority = 0
    n_group = int(len(rucksacks) / 3)
    for g in range(n_group):
        ascii_val = ord(
            common_item(
                rucksacks[3 * g].strip(),
                rucksacks[3 * g + 1].strip(),
                rucksacks[3 * g + 2].strip(),
            )
        )
        total_priority += convert_ascii_to_priority(ascii_val)
    return total_priority


if __name__ == "__main__":
    print(solve(parse_input("input_03.txt")))
    print(solve_B(parse_input("input_03.txt")))
