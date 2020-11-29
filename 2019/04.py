#!/usr/bin/env python3

# Source of the puzzle:
# https://adventofcode.com/2019/day/4


from codetiming import Timer


INPUT_FROM = 284639
INPUT_TO = 748759


def has_6_digits(number):
    return number > 99999 and number < 1000000


def is_in_range(number):
    return number >= INPUT_FROM and number <= INPUT_TO


def has_two_equal_adjacent_digit(number):
    n = str(number)
    return n[0] == n[1] or n[1] == n[2] or n[2] == n[3] or n[3] == n[4] or n[4] == n[5]


def has_two_equal_adjacent_digit_not_part_of_a_bigger_group(number):
    n1 = number // 100000
    n2 = number // 10000 % 10
    n3 = number // 1000 % 10
    n4 = number // 100 % 10
    n5 = number // 10 % 10
    n6 = number % 10
    return (
        (n1 == n2 and n2 != n3)
        or (n2 == n3 and n1 != n2 and n3 != n4)
        or (n3 == n4 and n2 != n3 and n4 != n5)
        or (n4 == n5 and n3 != n4 and n5 != n6)
        or (n5 == n6 and n4 != n5)
    )


def always_increase(number):
    n = str(number)
    return (
        int(n[0]) <= int(n[1])
        and int(n[1]) <= int(n[2])
        and int(n[2]) <= int(n[3])
        and int(n[3]) <= int(n[4])
        and int(n[4]) <= int(n[5])
    )


@Timer()
def part_one():
    solution_count = 0
    for i in range(INPUT_FROM, INPUT_TO + 1):
        if has_two_equal_adjacent_digit(i) and always_increase(i):
            solution_count += 1
    return solution_count


@Timer()
def part_two():
    solution_count = 0
    for i in range(INPUT_FROM, INPUT_TO + 1):
        if has_two_equal_adjacent_digit_not_part_of_a_bigger_group(
            i
        ) and always_increase(i):
            solution_count += 1
    return solution_count


if __name__ == "__main__":
    print(part_one())
    print(part_two())
