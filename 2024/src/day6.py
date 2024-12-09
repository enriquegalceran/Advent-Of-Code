import os
import numpy as np


def main(path_=None, verbose=1):
    if path_ is None:
        data = [
            "....#.....",
            ".........#",
            "..........",
            "..#.......",
            ".......#..",
            "..........",
            ".#..^.....",
            "........#.",
            "#.........",
            "......#...",
        ]
        # Solution = 41
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]

    # Replace "." with "_" so that it is printed correctly
    data = [_.replace(".", "_") for _ in data]
    if verbose > 0:
        print(data)
        print("\n".join(data))
        print("")

    # Find Guard and size of map
    dir_dict = {
        "^": 0,
        ">": 1,
        "V": 2,
        "<": 3,
    }
    dir_movement = {
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1),
    }
    dir_sign = {
        0: "^",
        1: ">",
        2: "V",
        3: "<",
    }
    map_forest, guard_coordinates, direction = create_map(data, dir_dict)
    guard_in_map = True

    distinct_squares, _ = find_way_through_forest(dir_movement, dir_sign, direction, guard_coordinates, guard_in_map,
                                                  map_forest, verbose)

    print(f"Solution day 6 - Part 1: {distinct_squares}")

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2

    # Reset + create a tree
    map_forest_start, guard_coordinates_start, direction_start = create_map(data, dir_dict)

    # Create Trees
    accum = 0
    list_obstacles = []
    for i in range(map_forest.shape[0]):
        for j in range(map_forest.shape[1]):
            print(f"{i:3}/{map_forest.shape[0]} - {j:3}/{map_forest.shape[1]} - {accum}/{i*map_forest.shape[0]+j}",
                  end="\r", flush=True)
            if map_forest_start[i, j] != -2:
                continue
            map_copy = map_forest_start.copy()
            map_copy[i, j] = -1
            _, loop = find_way_through_forest(dir_movement, dir_sign, direction_start, guard_coordinates_start, True,
                                              map_copy, 0, only_draw_loop=True, obstacle=(i, j))
            if loop:
                accum += 1
                list_obstacles.append((i, j))

    print(list_obstacles)
    print(f"Solution day 6 - Part 2: {accum}")


def find_way_through_forest(dir_movement, dir_sign, direction, guard_coordinates_, guard_in_map, map_forest, verbose,
                            only_draw_loop=False, obstacle=None):
    max_steps = 10000
    steps = 0
    already_passed = [["" for i in range(map_forest.shape[1])] for j in range(map_forest.shape[0])]
    loop = False
    while guard_in_map and steps < max_steps:
        new_coords = (
            guard_coordinates_[0] + dir_movement[direction][0], guard_coordinates_[1] + dir_movement[direction][1])
        guard_in_map = within_map(new_coords, map_forest.shape)
        if guard_in_map:
            # Check if tree
            if map_forest[new_coords] == -1:
                # Need to turn instead of move
                # First, turn right
                direction = (direction + 1) % 4
                # now calculate the step
                new_coords = (guard_coordinates_[0] + dir_movement[direction][0],
                              guard_coordinates_[1] + dir_movement[direction][1])
            map_forest[guard_coordinates_] = steps
            if str(direction) in already_passed[new_coords[0]][new_coords[1]]:
                loop = True
                break
            already_passed[guard_coordinates_[0]][guard_coordinates_[1]] += str(direction)
            map_forest[new_coords] = -3
        guard_coordinates_ = new_coords
        steps += 1
        if verbose > 1:
            print_map(map_forest, direction, dir_sign)
    distinct_squares = (map_forest >= 0).sum() + 1
    if (not only_draw_loop or loop) and verbose > 0:
        if obstacle is not None:
            map_forest[obstacle[0], obstacle[1]] = -4
        print_map(map_forest, direction, dir_sign)
        print(map_forest)
    return distinct_squares, loop


def print_map(map_forest, direction, dir_sign):
    map2str = {-2: " ", -1: "#", -3: dir_sign[direction], -4: "O"}
    forest_print = []
    for i in range(map_forest.shape[0]):
        tmp = [map2str[_] if _ < 0 else "X" for _ in map_forest[i]]
        forest_print.append("".join(tmp))
    print("\n".join(forest_print))


def create_map(data_, dir_dict):
    str2map = {"_": -2, "#": -1, "^": -3}
    map_forest = np.zeros(shape=[len(data_), len(data_[0])], dtype=int)
    direction = None
    guard_coordinates = None
    for i in range(len(data_)):
        for j in range(len(data_[0])):
            if data_[i][j] in dir_dict.keys():
                map_forest[i, j] = -3
                direction = dir_dict[data_[i][j]]
                guard_coordinates = (i, j)
            else:
                map_forest[i, j] = str2map[data_[i][j]]
    return map_forest, guard_coordinates, direction


def within_map(coords, mapshape):
    if coords[0] < 0 or coords[1] < 0 or coords[0] >= mapshape[0] or coords[1] >= mapshape[1]:
        return False
    else:
        return True


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day6.txt"

    path = os.path.join(datapath, filename)
    main(path)
