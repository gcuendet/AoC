#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2019/


class IntcodeComputer:
    def __init__(self, memory, inputs=[]):
        self.memory = memory
        self.inputs = inputs[::-1]
        self.instruction_pointer = 0
        self.opcodes = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            99: self.end,
        }
        self.finished = False

    def value(self, val, mode):
        return self.memory[val] if mode == 0 else val

    def get_one_value(self, jump=True):
        mode = self.memory[self.instruction_pointer]
        mode_a = mode // 100 % 10
        a = self.memory[self.instruction_pointer + 1]
        if jump:
            self.instruction_pointer += 2
        return a, mode_a

    def get_two_values(self, jump=True):
        mode = self.memory[self.instruction_pointer]
        mode_b = mode // 1000 % 10
        mode_a = mode // 100 % 10
        a = self.memory[self.instruction_pointer + 1]
        b = self.memory[self.instruction_pointer + 2]
        if jump:
            self.instruction_pointer += 3
        return [a, b], [mode_a, mode_b]

    def get_three_values(self, jump=True):
        mode = self.memory[self.instruction_pointer]
        mode_c = mode // 10000 % 10
        mode_b = mode // 1000 % 10
        mode_a = mode // 100 % 10
        a = self.memory[self.instruction_pointer + 1]
        b = self.memory[self.instruction_pointer + 2]
        c = self.memory[self.instruction_pointer + 3]
        if jump:
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
            self.memory[a] = int(self.get_inputs())

    def output(self):
        a, mode_a = self.get_one_value()
        return self.value(a, mode_a)

    def jump_if_true(self):
        [a, b], [mode_a, mode_b] = self.get_two_values(False)
        if self.value(a, mode_a):
            self.instruction_pointer = self.value(b, mode_b)
        else:
            self.instruction_pointer += 3

    def jump_if_false(self):
        [a, b], [mode_a, mode_b] = self.get_two_values(False)
        if self.value(a, mode_a) == 0:
            self.instruction_pointer = self.value(b, mode_b)
        else:
            self.instruction_pointer += 3

    def less_than(self):
        [a, b, c], [mode_a, mode_b, mode_c] = self.get_three_values()
        if mode_c == 0:
            self.memory[c] = 1 if self.value(a, mode_a) < self.value(b, mode_b) else 0

    def equals(self):
        [a, b, c], [mode_a, mode_b, mode_c] = self.get_three_values()
        if mode_c == 0:
            self.memory[c] = 1 if self.value(a, mode_a) == self.value(b, mode_b) else 0

    def end(self):
        self.finished = True

    def get_inputs(self):
        return self.inputs.pop() if self.inputs else None

    def run(self):
        val = None
        while (
            not self.finished
            and val is None
            and self.instruction_pointer < len(self.memory)
        ):
            code = self.memory[self.instruction_pointer] % 100
            ret = self.opcodes[code]()
            val = ret if ret is not None else val
        return val

    def add_input(self, value):
        self.inputs = [value] + self.inputs
