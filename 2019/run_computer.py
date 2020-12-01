#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2019/day/5


import argparse
from intcode_computer import IntcodeComputer


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    return parser.parse_args()


def read_input(filepath):
    with open(filepath, "r") as f:
        return [int(code) for code in f.readline().split(",")]


if __name__ == "__main__":
    args = parse_args()
    memory = read_input(args.input)
    computer = IntcodeComputer(memory)
    computer.run()
