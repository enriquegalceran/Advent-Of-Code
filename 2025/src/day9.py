import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# from math import sqrt


def main(path_=None, verbose=0, part=1):
    # Read Data
    if path_ is None:
        data = [
            "7, 1",
            "11, 1",
            "11, 7",
            "9, 7",
            "9, 5",
            "2, 5",
            "2, 3",
            "7, 3",
        ]
    else:
        with open(path_, "r") as file:
            data = file.readlines()
        data = [x.strip("\n") for x in data]

    data = [[int(x) for x in _.split(",")]for _ in data]
    n_tiles = len(data)
    max_size = max([x for _ in data for x in _])

    # data_np = np.zeros((max_size+1, max_size+1), dtype=np.int8)
    # for point in data:
    #     data_np[point[1], point[0]] = 1
    # print(data_np)

    print("here")

    max_area = 0
    for i in range(n_tiles):
        p1 = data[i]
        for j in range(1, n_tiles):
            p2 = data[j]
            dx = abs(p2[0]-p1[0]) + 1
            dy = abs(p2[1]-p1[1]) + 1
            area = dx*dy
            if area > max_area:
                max_area = area

    print("Solution part1:", max_area)




if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day9.txt"

    path = os.path.join(datapath, filename)
    main(path, 1, 1)
