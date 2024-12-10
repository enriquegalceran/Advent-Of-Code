import os
import re
import numpy as np


def main(path_=None, verbose=1):
    if path_ is None:
        data = [
            "2333133121414131402",
        ]
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]
    # Concatenate everything
    data = "".join(data)
    if verbose > 0:
        print("Data:")
        print(data)

    # Part 1:
    # Solution test part 1: 1928
    expanded_file = expand_file(data)
    print("Expanded file")
    print_string(expanded_file)

    defragmented = defragment(expanded_file, verbose=verbose)
    print("Defragmented")
    print_string(defragmented)

    chksum = checksum(defragmented)

    print(f"Solution Day 9 - Part 1: {chksum}")

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2:
    # Part 2: solution test: 2858















    print("here")


def print_string(string, spacing=None):
    lmax = len(str(max(string)))
    if spacing is None:
        if lmax > 1:
            spacing = True
        else:
            spacing = False
    k = [str(_) for _ in string]
    k = ["_" * lmax + spacing*" " if _ == "-1" else " " * (lmax - len(_)) + _ + spacing * " " for _ in k]
    print("".join(k))


def expand_file(data, empty=-1):
    free = False
    expanded = []
    i = 0
    for n in data:
        if free:
            expanded += [empty] * int(n)
        else:
            expanded += [i] * int(n)
            i += 1
        free = not free
    return expanded


def defragment(expanded_data, empty=-1, verbose=1):
    back_counter = -1
    defragmented = expanded_data.copy()
    for i, value in enumerate(defragmented):
        if value == empty:
            if len(defragmented) + back_counter < i:
                break
            while defragmented[back_counter] == empty:
                back_counter -= 1
            # The second check for a edge case... Dirty, but works
            if len(defragmented) + back_counter < i:
                break
            defragmented[i] = defragmented[back_counter]
            defragmented[back_counter] = empty
            back_counter -= 1
        if verbose > 1:
            print(f"{i}:")
            # print_string(defragmented)
    return defragmented


def checksum(string, empty=-1):
    accum = 0
    for i, v in enumerate(string):
        if v != empty:
            accum += i*v
    return accum


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day9.txt"

    path = os.path.join(datapath, filename)
    main(path)
