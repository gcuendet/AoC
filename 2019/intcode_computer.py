#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2019/


class IntcodeComputer:
    def __init__(self, memory):
        self.memory = memory
        self.instruction_pointer = 0
        self.opcodes = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            99: self.end,
        }
        self.finished = False

    def value(self, val, mode):
        return self.memory[val] if mode == 0 else val

    def get_one_value(self):
        mode = self.memory[self.instruction_pointer]
        mode_a = mode // 100 % 10
        a = self.memory[self.instruction_pointer + 1]
        self.instruction_pointer += 2
        return a, mode_a

    def get_three_values(self):
        mode = self.memory[self.instruction_pointer]
        mode_c = mode // 10000 % 10
        mode_b = mode // 1000 % 10
        mode_a = mode // 100 % 10
        a = self.memory[self.instruction_pointer + 1]
        b = self.memory[self.instruction_pointer + 2]
        c = self.memory[self.instruction_pointer + 3]
        self.instruction_pointer += 4
        return [a, b, c], [mode_a, mode_b, mode_c]

    def add(self):
        [a, b, c], [mode_a, mode_b, mode_c] = self.get_three_values()
        if mode_c == 0:
            self.memory[c] = self.value(a, mode_a) + self.value(b, mode_b)

    def multiply(self):
        [a, b, c], [mode_a, mode_b, mode_c] = self.get_three_values()
        if mode_c == 0:
            self.memory[c] = self.value(a, mode_a) * self.value(b, mode_b)

    def input(self):
        a, mode_a = self.get_one_value()
        if mode_a == 0:
            self.memory[a] = int(input())

    def output(self):
        a, mode_a = self.get_one_value()
        if mode_a == 0:
            print(self.memory[a])

    def end(self):
        self.finished = True

    def run(self):
        while not self.finished and self.instruction_pointer < len(self.memory):
            code = self.memory[self.instruction_pointer] % 100
            self.opcodes[code]()
