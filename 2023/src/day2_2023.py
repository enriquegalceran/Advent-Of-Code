import os
import re
import math


def main(path_=None, verbose=1):
    if path_ is None:
        data = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]
        # Solution = 8
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]
    if verbose > 0:
        print(data)
        print("\n")

    cube_distribution = {"red": 12, "green": 13, "blue": 14}

    part1_sol = get_score(data, cube_distribution, verbose)

    print(f"Solution Day 2, Part 1: {part1_sol}")

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2

    part_2_sol = get_power(data, verbose)

    print(f"Solution Day 2, Part 2: {part_2_sol}")


def get_power(data_, verbose=1):
    accum = 0
    for i in range(len(data_)):
        game = data_[i]
        game = parse_string_to_list(game)
        if verbose > 2:
            print(data_[i], "\n", game)
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        for _ in game:
            min_cubes = min_cube_compare(_, min_cubes)
        accum += math.prod(list(min_cubes.values()))
    return accum


def min_cube_compare(game_, min_cubes_):
    for i in range(len(game_)//2):
        if int(game_[i*2]) > min_cubes_[game_[i*2 + 1].strip(",")]:
            min_cubes_[game_[i*2 + 1].strip(",")] = int(game_[i*2])
    return min_cubes_


def get_score(data_, cubes, verbose=1):
    accum = 0
    for i in range(len(data_)):
        game = data_[i]
        game = parse_string_to_list(game)
        if verbose > 2:
            print(data_[i], "\n", game)
        game = [is_valid(_, cubes) for _ in game]
        if all(game):
            accum += i + 1
    return accum


def parse_string_to_list(game):
    game = game.split(":")[1]
    game = game.split(";")
    game = [_.strip() for _ in game]
    game = [[re.split(r"(\d+)", _)] for _ in game]
    game = [[x[1:] for x in _] for _ in game]
    game = [[[x.strip() for x in k] for k in _] for _ in game]
    game = [item for sublist in game for item in sublist]
    return game


def is_valid(game_, cubes_):
    for i in range(len(game_)//2):
        if int(game_[i*2]) > cubes_[game_[i*2 + 1].strip(",")]:
            return False
    return True


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day2_2023.txt"

    path = os.path.join(datapath, filename)
    main(path)
