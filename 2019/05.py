#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2019/day/5


from intcode_computer import IntcodeComputer


def read_input(filepath):
    with open(filepath, "r") as f:
        return [int(code) for code in f.readline().split(",")]


if __name__ == "__main__":
    filepath = "05_input.txt"
    memory = read_input(filepath)
    computer = IntcodeComputer(memory)
    computer.run()
