import os
import numpy as np
from functools import lru_cache


def main(path_=None, verbose=1):
    if path_ is None:
        data = [
            "AAAA",
            "BBCD",
            "BBCC",
            "EEEC"
        ]
        # Solution test 1: 40+32+4+24=140
        data = [
            "OOOOO",
            "OXOXO",
            "OOOOO",
            "OXOXO",
            "OOOOO",
        ]
        # Solution test 2: 756+4=772
        data = [
            "RRRRIICCFF",
            "RRRRIICCCF",
            "VVRRRCCFFF",
            "VVRCCCJFFF",
            "VVVVCJJCFE",
            "VVIVCCJJEE",
            "VVIIICJJEE",
            "MIIIIIJJEE",
            "MIIISIJEEE",
            "MMMISSJEEE",
        ]
        # Solution test 3: 1930
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]

    if verbose > 0:
        print("Data:")
        print("\n".join(data))

    regions = []
    map_id = np.ones(shape=(len(data), len(data[0])), dtype=int) * -1
    print(map_id)
    undefinded_i, undefinded_j = np.where(map_id == -1)
    for i, j in zip(undefinded_i, undefinded_j):
        if map_id[i, j] == -1:
            identify_region((i, j), data, map_id, regions)

    print(map_id)
    cost = cost_method1(map_id, regions)
    print(f"Solution Day 12 - Part 1 {cost}")
    print("here")


def cost_method1(map_id, regions):
    cost = 0
    for region in regions:
        fence, area = measure_fence_and_area(region, map_id)
        cost += fence * area
    return cost


def measure_fence_and_area(region_coords, map_id):
    region_id = map_id[region_coords[0][0], region_coords[0][1]]
    fence = 0
    for c in region_coords:
        neighbours = get_neighbours(c, map_id.shape)
        neighbours_ids = [map_id[n[0], n[1]] for n in neighbours]
        within_region = neighbours_ids.count(region_id)
        fence += 4 - within_region
    return fence, len(region_coords)





def identify_region(coords, data, map_id, regions):
    region_letter = data[coords[0]][coords[1]]
    region_id = len(regions)
    map_id[coords[0], coords[1]] = region_id
    adjacent = []
    within_region = [coords]
    searching = [coords]
    while len(searching) > 0:
        c = searching.pop(0)
        neighbours = get_neighbours(c, map_id.shape)
        for n in neighbours:
            if n not in adjacent and n not in within_region:
                if data[n[0]][n[1]] == region_letter:
                    within_region.append(n)
                    searching.append(n)
                    map_id[n[0], n[1]] = region_id
                else:
                    adjacent.append(n)
    regions.append(within_region)
    return




def get_neighbours(coords, mapshape):
    directions = {"U": (-1, 0), "L": (0, -1), "R": (0, 1), "D": (1, 0)}
    neighbours = []
    for d, c in directions.items():
        n = add_direction(coords, c)
        if within_map(n, mapshape):
            neighbours.append(n)
    return neighbours


def add_direction(coord1, direction):
    return coord1[0] + direction[0], coord1[1] + direction[1]


def within_map(coords, mapshape):
    if coords[0] < 0 or coords[1] < 0 or coords[0] >= mapshape[0] or coords[1] >= mapshape[1]:
        return False
    else:
        return True










if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day12.txt"

    path = os.path.join(datapath, filename)
    main(path)
