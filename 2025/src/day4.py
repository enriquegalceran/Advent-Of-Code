import os
import numpy as np


def get_neighbours(data_, x_, y_, size_):
    def get_min_max_filter(k, lim):
        if k == 0:
            min_ = 0
        else:
            min_ = -1
        if k < size_[0] - 1:
            max_ = 1
        else:
            max_ = 0
        return min_, max_

    minx, maxx = get_min_max_filter(x_, size_[0])
    miny, maxy = get_min_max_filter(y_, size_[1])

    neighbours = data_[(x_ + minx):(x_ + maxx + 1), (y_ + miny):(y_ + maxy + 1)]

    return neighbours.sum() - 1


def iterate_over_data(data_, ):
    accessible = 0
    data_cleaned = data_.copy()
    size_ = data_.shape
    for row in range(size_[0]):
        for col in range(size_[1]):
            if data_[row, col] == 1:
                local_neighbours = get_neighbours(data_, row, col, size_)
                if local_neighbours < 4:
                    accessible += 1
                    data_cleaned[row, col] = 0
    return accessible, data_cleaned


def main(path_=None, verbose=0, part=1):
    # Read Data
    if path_ is None:
        data = ["..@@.@@@@.",
                "@@@.@.@.@@",
                "@@@@@.@.@@",
                "@.@@@@..@.",
                "@@.@@@@.@@",
                ".@@@@@@@.@",
                ".@.@.@.@@@",
                "@.@@@.@@@@",
                ".@@@@@@@@.",
                "@.@.@@@.@."]
    else:
        with open(path_, "r") as file:
            data = file.readlines()
        data = [x.strip() for x in data]

    print("\n".join(data))

    size = (len(data), len(data[0]))
    data_np = np.zeros(size, dtype=np.int8)
    match = "@"
    for i in range(size[0]):
        for j in range(size[1]):
            if data[i][j] == match:
                data_np[i, j] = 1
            else:
                data_np[i, j] = 0

    if part == 1:

        n_accessible, _ = iterate_over_data(data_np)

        print(n_accessible)


    if part == 2:

        cleanable = True
        total_accessible = 0
        while cleanable:
            n_accessible, data_np = iterate_over_data(data_np)
            if verbose:
                print(data_np)
                print(f"Removed: {n_accessible}")
            total_accessible += n_accessible
            if n_accessible == 0:
                break
        print(f"total removed: {total_accessible}")
        print("here")

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2

    if part == 2:
        pass


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day4.txt"

    path = os.path.join(datapath, filename)
    main(path, 1, 2)
