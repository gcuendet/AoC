import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    return parser.parse_args()


def read_input(filepath):
    with open(filepath, "r") as f:
        return [int(i) for i in f.readline()]


def row_major_image(input, height=6, width=25):
    n_channels = len(input) / (height * width)
    im = []
    for c in range(n_channels):
        channel_rows = []
        for y in range(height):
            start = c * height * width + y * width
            row = input[start : start + width]
            channel_rows.append(row)
        im.append(channel_rows)
    return im


def part1(im):
    min_zero = 1e9
    product = None
    for c in range(len(im)):
        channel = [item for sublist in im[c] for item in sublist]
        zero_count = channel.count(0)
        if zero_count < min_zero:
            min_zero = zero_count
            product = channel.count(1) * channel.count(2)
    return product


def part2(im, width, height):
    res = [[None for i in range(width)] for j in range(height)]

    for c in range(len(im)):
        for row in range(height):
            for col in range(width):
                if (res[row][col] is None) and (im[c][row][col] != 2):
                    res[row][col] = im[c][row][col]

    return ["".join([" " if (p == 0) else "*" for p in t]) for t in res]


if __name__ == "__main__":
    args = parse_args()
    width = 25
    height = 6
    flat_image = read_input(args.input)
    im = row_major_image(flat_image, height=height, width=width)
    print(part1(im))

    decoded = part2(im, width, height)
    for i in decoded:
        print(i)
