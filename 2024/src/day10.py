import os
import re
import numpy as np


def main(path_=None, verbose=1):
    if path_ is None:
        data = [
            "89010123",
            "78121874",
            "87430965",
            "96549874",
            "45678903",
            "32019012",
            "01329801",
            "10456732",
        ]
        # Solution: 5, 6, 5, 3, 1, 3, 5, 3, and 5 -> 36
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]
    data = np.array([[int(x) for x in _] for _ in data])
    if verbose > 0:
        print("Data:")
        print(data)

    trailheads = data == 0
    trailtops = data == 9
    coords_heads = []
    coords_tops = []


    which_tops_are_reachable = create_empty_list(data)

    id_top = 0
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i, j] == 9:
                coords_tops.append([i, j])
                id_top += 1
                which_tops_are_reachable[i][j].append(id_top)
            elif data[i, j] == 0:
                coords_heads.append([i, j])

    # Find down ladder
    for n in reversed(range(9)):
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                if data[i, j] != n:
                    continue
                # if value == n:
                # look for neighbours and their values
                coord = [i, j]
                valid_neighbours = ladder_neighbours(data, coord)
                value_neighbours = [data[_] for _ in valid_neighbours]
                for m in range(len(value_neighbours)):
                    if data[valid_neighbours[m]] == n + 1:
                        which_tops_are_reachable[i][j] = list(set(which_tops_are_reachable[i][j] + which_tops_are_reachable[valid_neighbours[m][0]][valid_neighbours[m][1]]))
    print(which_tops_are_reachable)

    # Measure how many *different* tops are reachable
    n_accessible = np.zeros_like(data, dtype=int)
    trail_heads = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            n_accessible[i, j] = len(which_tops_are_reachable[i][j])
            if trailheads[i, j]:
                trail_heads.append(len(which_tops_are_reachable[i][j]))
    solution_1 = sum(trail_heads)
    print(f"Solution Day 10 - Part 1: {solution_1}")


def ladder_neighbours(data, coords):
    directions = {"U": (-1, 0), "L": (0, -1), "R": (0, 1), "D": (1, 0)}
    outputs = []
    for direction, vect in directions.items():
        new_position = add_direction(coords, vect)
        if within_map(new_position, data.shape):
            outputs.append(new_position)
    return outputs


def add_direction(coord1, direction):
    return coord1[0] + direction[0], coord1[1] + direction[1]


def create_empty_list(matrix):
    return [[[] for x in range(matrix.shape[1])] for _ in range(matrix.shape[0])]


def within_map(coords, mapshape):
    if coords[0] < 0 or coords[1] < 0 or coords[0] >= mapshape[0] or coords[1] >= mapshape[1]:
        return False
    else:
        return True


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day10.txt"

    path = os.path.join(datapath, filename)
    main(path)
