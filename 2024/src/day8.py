import os
import re
import numpy as np


def main(path_=None, verbose=1):
    if path_ is None:
        data = [
            "............",
            "........0...",
            ".....0......",
            ".......0....",
            "....0.......",
            "......A.....",
            "............",
            "............",
            "........A...",
            ".........A..",
            "............",
            "............",
        ]
        # Solution = 14
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]
    data = [_.replace(".", "_") for _ in data]
    if verbose > 0:
        print(data)
        print("\n".join(data))

    mapshape = (len(data), len(data[0]))
    list_antenna_types = find_all_unique_antennas(data)
    coordinate_antenna_types = get_coordinates_from_map(data, list_antenna_types, mapshape)

    antinodes = {}
    total_antinodes = 0
    for antenna_type, coordinates in coordinate_antenna_types.items():
        # For each pair of antennas, find the antinode
        antinodes[antenna_type] = []
        for a1 in coordinates:
            for a2 in coordinates:
                if a1 == a2:
                    continue
                antinode1, antinode2 = get_antinodes(a1, a2)
                if within_map(antinode1, mapshape):
                    antinodes[antenna_type].append(antinode1)
                    total_antinodes += 1
                if within_map(antinode2, mapshape):
                    antinodes[antenna_type].append(antinode2)
                    total_antinodes += 1

    map_with_antinodes = np.ones(mapshape, dtype=int) * -1
    for antenna_type, coordinates in coordinate_antenna_types.items():
        i_antenna = list(coordinate_antenna_types.keys()).index(antenna_type)
        for c in coordinates:
            map_with_antinodes[c[0], c[1]] = i_antenna
    for _, coordinates in antinodes.items():
        for c in coordinates:
            map_with_antinodes[c[0], c[1]] = -2
    print_map(map_with_antinodes)
    all_antinodes = (map_with_antinodes == -2).sum()

    print(f"Solution Day 8 - Part 1: {all_antinodes}")

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2
    # Solution Test: Same input, solution now 34















    print("here")











def get_antinodes(x1, x2):
    direction = (x2[0] - x1[0], x2[1] - x1[1])
    antinode1 = (x2[0] + direction[0], x2[1] + direction[1])
    antinode2 = (x1[0] - direction[0], x1[1] - direction[1])
    return antinode1, antinode2


def get_coordinates_from_map(data, list_antenna_types, mapshape):
    coordinate_antenna_types = {}
    for antenna_type in list_antenna_types:
        coordinate_antenna_types[antenna_type] = []
    for i in range(mapshape[0]):
        for j in range(mapshape[1]):
            if data[i][j] != "_":
                coordinate_antenna_types[data[i][j]].append((i, j))
    return coordinate_antenna_types


def print_map(map_data):
    map2str = {-1: "_", -2: "#"}
    forest_print = []
    for i in range(map_data.shape[0]):
        tmp = [map2str[_] if _ < 0 else str(_) for _ in map_data[i]]
        forest_print.append("".join(tmp))
    print("\n".join(forest_print))


def find_all_unique_antennas(data_):
    all_data = "".join(data_)
    antennas = re.findall("[a-z]|[A-Z]|[0-9]", all_data)
    return list(set(antennas))


def within_map(coords, mapshape):
    if coords[0] < 0 or coords[1] < 0 or coords[0] >= mapshape[0] or coords[1] >= mapshape[1]:
        return False
    else:
        return True


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day8.txt"

    path = os.path.join(datapath, filename)
    main(path)
