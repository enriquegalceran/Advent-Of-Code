import os
import numpy as np


def main(path_=None):
    # Read Data
    if path_ is None:
        data = [
            [3, 4],
            [4, 3],
            [2, 5],
            [1, 3],
            [3, 9],
            [3, 3],
        ]
    else:
        with open(path_, "r") as file:
            data = file.readlines()
        data = [x.strip().split() for x in data]
        data = [[int(_[0]), int(_[1])] for _ in data]

    # Part 1

    left = np.zeros(len(data), dtype=int)
    right = np.zeros(len(data), dtype=int)

    for i in range(len(data)):
        left[i] = data[i][0]
        right[i] = data[i][1]

    left.sort()
    right.sort()

    dist = np.abs(left - right)

    print(f"Solution Day 1, Part 1: {dist.sum()}")

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2

    similarity_score = 0
    for i in range(len(data)):
        number = left[i]
        appearance = right == number
        n = np.sum(appearance)
        similarity_score += number * n

    print(f"Solution Day 1, Part 2: {similarity_score}")



if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day1.txt"

    path = os.path.join(datapath, filename)
    main(path)
