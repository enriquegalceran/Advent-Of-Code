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
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]
    data = [_.replace(".", "_") for _ in data]
    if verbose > 0:
        print(data)
        print("\n".join(data))

    coordinate_antenna_types, mapshape = parse_input_data(data)

    # Part 1
    # Test solution = 14
    antinodes = calculate_antinodes_positions(coordinate_antenna_types, mapshape, resonant=False)
    all_antinodes = add_antinodes_and_plot(antinodes, coordinate_antenna_types, mapshape, verbose)

    print(f"Solution Day 8 - Part 1: {all_antinodes}")

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2
    # Test solution: 34

    antinodes = calculate_antinodes_positions(coordinate_antenna_types, mapshape, resonant=True)
    all_antinodes = add_antinodes_and_plot(antinodes, coordinate_antenna_types, mapshape, verbose)
    print(f"Solution Day 8 - Part 2: {all_antinodes}")


def parse_input_data(data):
    mapshape = (len(data), len(data[0]))
    list_antenna_types = find_all_unique_antennas(data)
    coordinate_antenna_types = get_coordinates_from_map(data, list_antenna_types, mapshape)
    return coordinate_antenna_types, mapshape


def calculate_antinodes_positions(coordinate_antenna_types, mapshape, resonant):
    antinodes = {}
    for antenna_type, coordinates in coordinate_antenna_types.items():
        # For each pair of antennas, find the antinode
        antinodes[antenna_type] = []
        for a1 in coordinates:
            for a2 in coordinates:
                if a1 == a2:
                    continue
                if resonant:
                    antinodes_found = get_antinodes_resonant(a1, a2, mapshape)
                else:
                    antinodes_found = get_antinodes(a1, a2)
                for antin in antinodes_found:
                    if within_map(antin, mapshape):
                        antinodes[antenna_type].append(antin)
    return antinodes


def add_antinodes_and_plot(antinodes, coordinate_antenna_types, mapshape, verbose):
    map_with_antinodes = np.ones(mapshape, dtype=int) * -1
    for antenna_type, coordinates in coordinate_antenna_types.items():
        i_antenna = list(coordinate_antenna_types.keys()).index(antenna_type)
        for c in coordinates:
            map_with_antinodes[c[0], c[1]] = i_antenna
    for _, coordinates in antinodes.items():
        for c in coordinates:
            map_with_antinodes[c[0], c[1]] = -2
    if verbose > 0:
        print_map(map_with_antinodes)
    return (map_with_antinodes == -2).sum()


def get_antinodes_resonant(x1, x2, mapshape):
    antinodes = []
    direction = (x2[0] - x1[0], x2[1] - x1[1])
    antinode = x1
    while within_map(antinode, mapshape):
        antinodes.append(antinode)
        antinode = (antinode[0] + direction[0], antinode[1] + direction[1])
    antinode = (x1[0] - direction[0], x1[1] - direction[1])
    while within_map(antinode, mapshape):
        antinodes.append(antinode)
        antinode = (antinode[0] - direction[0], antinode[1] - direction[1])
    return antinodes


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
    l_max_data = len(str(map_data.max()))
    for i in range(map_data.shape[0]):
        tmp = [map2str[_]*l_max_data + " " if _ < 0 else f"{_:{l_max_data}} " for _ in map_data[i]]
        forest_print.append("".join(tmp))
    print("\n".join(forest_print))


def find_all_unique_antennas(data_):
    all_data = "".join(data_)
    antennas = re.findall(r"[a-z]|[A-Z]|[0-9]", all_data)
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
