#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2019/day/1

# input: https://adventofcode.com/2019/day/1/input


def is_valid(password: str, policy):
    key = policy[0]
    count = password.count(key)
    if count >= policy[1][0] and count <= policy[1][1]:
        return True
    return False


def is_valid_2(password: str, policy):
    key = policy[0]
    # != is equivalent to logical XOR :)
    if (password[policy[1][0] - 1] == key) != (password[policy[1][1] - 1] == key):
        return True
    return False


def read_input(filepath="02_input.txt"):
    input_list = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            parts = line.split(" ")
            _min, _max = parts[0].split("-")[0:2]
            key = parts[1].strip(":")
            password = str(parts[2])
            input_list.append((password, (key, (int(_min), int(_max)))))
    return input_list


def part_one():
    input_list = read_input()
    valid = 0
    for password, policy in input_list:
        if is_valid(password, policy):
            valid += 1
    return valid


def part_two():
    input_list = read_input()
    valid = 0
    for password, policy in input_list:
        if is_valid_2(password, policy):
            valid += 1
    return valid


if __name__ == "__main__":
    print(part_one())
    print(part_two())
