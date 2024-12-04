import os
import re


def main(path_=None, verbose=1):
    if path_ is None:
        data = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"
        ]
        # Solution = 18
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]
    if verbose > 0:
        print(data)
        print("\n".join(data))

    rows = find_horizontal(data)
    cols = find_vertical(data)
    diag_pos = find_diagonal_pos(data)
    diag_neg = find_diagonal_neg(data)
    total = rows + cols + diag_pos + diag_neg
    print(f"Solution Day 4, Part 1: {total}")


def find_diagonal_pos(data_):
    nrows = len(data_)
    ncols = len(data_[0])
    accum = 0
    # Right half
    r = 0
    for c in reversed(range(ncols)):
        diag = ""
        for k in range(ncols - c):
            diag += data_[k][c + k]
        if len(diag) < 4:
            continue
        a = re.findall("XMAS", diag)
        b = re.findall("SAMX", diag)
        accum += len(a) + len(b)
    # Left half
    for r in range(1, nrows):
        diag = ""
        for k in range(nrows - r):
            diag += data_[r + k][k]
        if len(diag) < 4:
            break
        a = re.findall("XMAS", diag)
        b = re.findall("SAMX", diag)
        accum += len(a) + len(b)
    return accum


def find_diagonal_neg(data_):
    nrows = len(data_)
    ncols = len(data_[0])
    accum = 0
    # Left half
    r = 0
    for c in reversed(range(ncols)):
        diag = ""
        for k in range(c+1):
            diag += data_[k][c-k]
        if len(diag) < 4:
            break
        a = re.findall("XMAS", diag)
        b = re.findall("SAMX", diag)
        accum += len(a) + len(b)
    # Right half
    for r in range(1, nrows):
        diag = ""
        for k in range(nrows - r):
            diag += data_[r + k][ncols - k -1]
        if len(diag) < 4:
            break
        a = re.findall("XMAS", diag)
        b = re.findall("SAMX", diag)
        accum += len(a) + len(b)
    return accum


def find_vertical(data_):
    ncols = len(data_[0])
    accum = 0
    for c in range(ncols):
        col = "".join([row[c] for row in data_])
        a = re.findall("XMAS", col)
        b = re.findall("SAMX", col)
        accum += len(a) + len(b)
    return accum


def find_horizontal(data_):
    accum = 0
    for row in data_:
        a = re.findall("XMAS", row)
        b = re.findall("SAMX", row)
        accum += len(a) + len(b)
    return accum


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day4.txt"

    path = os.path.join(datapath, filename)
    main(path)
