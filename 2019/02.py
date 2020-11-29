#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2019/day/2

# input: https://adventofcode.com/2019/day/2/input


def read_input(filepath):
    with open(filepath, "r") as f:
        return [int(code) for code in f.readline().split(",")]


def run_code(memory):
    instruction_pointer = 0
    while instruction_pointer < len(memory):
        opcode = memory[instruction_pointer]
        if opcode == 99:
            return memory

        p_addr = [memory[instruction_pointer + i] for i in range(1, 4)]
        if opcode == 1:
            memory[p_addr[2]] = memory[p_addr[0]] + memory[p_addr[1]]
        elif opcode == 2:
            memory[p_addr[2]] = memory[p_addr[0]] * memory[p_addr[1]]
        else:
            raise (RuntimeError("Unknown code. Should be 1, 2, or 99"))
        instruction_pointer += 4


def noun_verb(noun, verb):
    memory = read_input("02_input.txt")
    memory[1] = noun
    memory[2] = verb
    memory = run_code(memory)
    return memory[0]


def part_one():
    memory = read_input("02_input.txt")
    # restore gravity assist program
    memory[1] = 12
    memory[2] = 2
    res = run_code(memory)
    return res[0]


def part_two():
    """ Brute force solution """
    memory = read_input("02_input.txt")
    for n in range(0, 100):
        for v in range(0, 100):
            res = noun_verb(n, v)
            if res == 19690720:
                return 100 * n + v


if __name__ == "__main__":
    print(part_one())
    print(part_two())
