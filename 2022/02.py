def parse_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()


elf = {"A": "X", "B": "Y", "C": "Z"}
# for part 1
figure_points = {"X": 1, "Y": 2, "Z": 3}
# for part 2
outcome = {"X": 0, "Y": 3, "Z": 6}
reverse_figure_points = {v: k for k, v in figure_points.items()}


def round_score_A(elf_play, self_play):
    diff = (figure_points[self_play] - figure_points[elf[elf_play]]) % 3
    # diff is 0 (it's a draw), 1 (it's a victory), or 2 (it's a loss)
    result = 3 if diff == 0 else (0 if diff == 2 else 6)
    return result + figure_points[self_play]


def round_score_B(elf_play, outcome_round):
    self_play = figure_points[elf[elf_play]] + (int(outcome[outcome_round] / 3) - 1)
    if self_play == 0:
        self_play = 3
    if self_play == 4:
        self_play = 1
    return outcome[outcome_round] + self_play


def scores(rounds):
    total_score_A = 0
    total_score_B = 0
    for r in rounds:
        total_score_A += round_score_A(*r.strip().split(" "))
        total_score_B += round_score_B(*r.strip().split(" "))
    return total_score_A, total_score_B


if __name__ == "__main__":
    print(scores(parse_input("input_02.txt")))
