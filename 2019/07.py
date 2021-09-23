import argparse
from intcode_computer import IntcodeComputer
import copy
from itertools import permutations


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    return parser.parse_args()


def read_input(filepath):
    with open(filepath, "r") as f:
        return [int(code) for code in f.readline().split(",")]


def part1(memory):
    max_thrust = 0
    for perm in permutations([0, 1, 2, 3, 4]):
        computers = [
            IntcodeComputer(copy.deepcopy(memory), [perm[i]]) for i in range(5)
        ]

        new_input = 0
        for comp in computers:
            comp.add_input(new_input)
            new_input = comp.run()
            max_thrust = max(new_input, max_thrust)
    return max_thrust


def part2(memory):
    max_thrust = 0
    for perm in permutations([5, 6, 7, 8, 9]):
        computers = [
            IntcodeComputer(copy.deepcopy(memory), [perm[i]]) for i in range(5)
        ]

        new_input = 0
        while all([not c.finished for c in computers]):
            for i, comp in enumerate(computers):
                comp.add_input(new_input)
                new_input = comp.run()
                max_thrust = max(new_input, max_thrust)
    return max_thrust


if __name__ == "__main__":
    args = parse_args()
    memory = read_input(args.input)
    print(part1(memory))
    print(part2(memory))
