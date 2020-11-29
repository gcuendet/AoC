#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2019/day/3

# input: https://adventofcode.com/2019/day/3/input

import math
from codetiming import Timer


def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()


def move_left(pos, amount):
    pos_list = [(pos[0] - dx, pos[1]) for dx in range(1, amount + 1)]
    return list(pos_list), pos_list[-1]


def move_right(pos, amount):
    pos_list = [(pos[0] + dx, pos[1]) for dx in range(1, amount + 1)]
    return list(pos_list), pos_list[-1]


def move_up(pos, amount):
    pos_list = [(pos[0], pos[1] + dy) for dy in range(1, amount + 1)]
    return list(pos_list), pos_list[-1]


def move_down(pos, amount):
    pos_list = [(pos[0], pos[1] - dy) for dy in range(1, amount + 1)]
    return list(pos_list), pos_list[-1]


def wire_coordinates(instructions):
    """ Returns a set of coordinates (as pairs of integers) through which the wire is passing"""
    pos = (0, 0)
    path = [(0, 0)]

    for move in instructions:
        if move[0] == "R":
            new_path, pos = move_right(pos, int(move[1:]))
        if move[0] == "L":
            new_path, pos = move_left(pos, int(move[1:]))
        if move[0] == "U":
            new_path, pos = move_up(pos, int(move[1:]))
        if move[0] == "D":
            new_path, pos = move_down(pos, int(move[1:]))
        path.extend(new_path)
    return path


def intersect(wire_a, wire_b):
    return set(wire_a) & set(wire_b)


def closest_intersection(intersections):
    manhattan_dist = math.inf
    for intersect in intersections:
        dist = abs(intersect[0]) + abs(intersect[1])
        if dist < manhattan_dist and dist > 0:
            # closest_intersection = intersect
            manhattan_dist = dist
    return manhattan_dist


def fewest_steps_intersection(intersections, wire_a, wire_b):
    steps = math.inf
    for intersect in intersections:
        dist = wire_a.index(intersect) + wire_b.index(intersect)
        if dist < steps and dist > 0:
            steps = dist
    return steps


@Timer(name="part 1")
def part_one():
    instructions = read_input("03_input.txt")
    wire_a = wire_coordinates(instructions[0].split(","))
    wire_b = wire_coordinates(instructions[1].split(","))
    intersections = intersect(wire_a, wire_b)
    return closest_intersection(intersections)


@Timer(name="part 2")
def part_two():
    instructions = read_input("03_input.txt")
    wire_a = wire_coordinates(instructions[0].split(","))
    wire_b = wire_coordinates(instructions[1].split(","))
    intersections = intersect(wire_a, wire_b)
    return fewest_steps_intersection(intersections, wire_a, wire_b)


if __name__ == "__main__":
    print(part_one())
    print(part_two())
