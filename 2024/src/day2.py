import os
import numpy as np


def main(path_=None):
    if path_ is None:
        data = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9],
        ]
    else:
        with open(path_, "r") as file:
            data = file.readlines()
        data = [x.strip().split() for x in data]
        data = [[int(k) for k in _] for _ in data]

    print("Data:")
    print(data)

    def is_decreasing(vector):
        for x in range(1, len(vector)):
            if vector[x] > vector[x - 1]:
                return False
        return True

    def is_increasing(vector):
        for x in range(1, len(vector)):
            if vector[x] < vector[x - 1]:
                return False
        return True

    def within_bounds(vector, lower, upper):
        for x in range(1, len(vector)):
            dif = abs(vector[x] - vector[x - 1])
            if dif > upper or dif < lower:
                return False
        return True

    def is_safe(vector, lower=1, upper=3):
        return (is_decreasing(vector) or is_increasing(vector)) and within_bounds(vector, lower, upper)

    safe = 0
    for i in range(len(data)):
        vector_i = data[i]
        decreasing = is_decreasing(vector_i)
        increasing = is_increasing(vector_i)
        bounds = within_bounds(vector_i, 1, 3)
        is_safe_ = is_safe(vector_i)
        print(f"Row {i}: Decreasing: {decreasing}, Increasing: {increasing}, Bounds: {bounds}, All: {is_safe_}")
        safe += is_safe_

    print(f"Solution Day 2, Part 1: {safe}")


    print("here")










if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day2.txt"

    path = os.path.join(datapath, filename)
    main(None)
