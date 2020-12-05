#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2020/day/4

# input: https://adventofcode.com/2020/day/4/input


def read_input(filepath="04_input.txt"):
    passports = []
    with open(filepath, "r") as f:
        lines = f.readlines()
    pp = {}
    for line in lines:
        if line == "\n":
            passports.append(pp)
            pp = {}
            continue
        for entry in line.strip("\n").split(" "):
            k, v = entry.split(":")
            pp[k] = v
    return passports


def is_valid(passport, mandatory_field):
    for f in mandatory_field:
        if not f in passport.keys():
            return False
    return True


def part_one():
    passports = read_input()
    valid_count = 0
    for passport in passports:
        if is_valid(passport, ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
            valid_count += 1

    return valid_count


def part_two():
    pass


if __name__ == "__main__":
    print(part_one())
    print(part_two())
