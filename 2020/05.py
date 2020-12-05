#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2020/day/5

# input: https://adventofcode.com/2020/day/5/input


def read_input(filepath="05_input.txt"):
    boarding_passes = []
    with open(filepath, "r") as f:
        lines = f.readlines()
    for line in lines:
        boarding_passes.append(line.strip())
    return boarding_passes


def to_binary(code, zero="0", one="1"):
    res = 0
    for i, c in enumerate(code[::-1]):
        res += 2 ** i if c == one else 0
    return res


def seat_ids(codes):
    all_sid = []
    for code in codes:
        row = to_binary(code[:7], "F", "B")
        seat = to_binary(code[7:], "L", "R")
        sid = row * 8 + seat
        all_sid.append(sid)
    return all_sid


def part_one():
    codes = read_input()
    all_sid = seat_ids(codes)
    return max(all_sid)


def part_two():
    codes = read_input()
    all_sid = seat_ids(codes)
    min_sid = min(all_sid)
    max_sid = max(all_sid)
    return set(range(min_sid, max_sid)) - set(all_sid)


if __name__ == "__main__":
    print(part_one())
    print(part_two())
