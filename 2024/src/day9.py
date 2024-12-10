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

    expanded_file_2 = expand_file(data)

    list_of_cases = defragment_without_splitting(expanded_file_2, verbose)
    if verbose > 0:
        print("Defragmented without splitting:")
        print_string(list_of_cases)

    output2 = checksum(list_of_cases)

    print(f"Solution Day 9 - Part 2: {output2}")


def defragment_without_splitting(input_list, verbose):
    bit_str = get_bit_str(input_list)
    backtrack = -1
    while True:
        if input_list[backtrack] != -1:
            id_to_search = input_list[backtrack]
            length = 1
            while input_list[backtrack - length] == id_to_search:
                length += 1
            first_empty = find_empty_space(bit_str[:backtrack], length)
            if first_empty is not None:
                input_list[first_empty.start():first_empty.end()] = input_list[(len(bit_str) + backtrack - length + 1):
                                                                               (len(bit_str) + backtrack + 1)]
                input_list[(len(bit_str) + backtrack - length + 1): (len(bit_str) + backtrack + 1)] = [-1] * length
                bit_str = get_bit_str(input_list)
            if verbose > 1:
                print_string(input_list)
            backtrack -= length
        else:
            backtrack -= 1
        if re.search(r"1", bit_str[:backtrack]) is None:
            break
    return input_list


def get_bit_str(list_data):
    a = ["1" if _ == -1 else "0" for _ in list_data]
    return "".join(a)


def find_empty_space(bit_str, length):
    # Only the first iteration:
    match = re.search("1" * length, bit_str)
    return match


def print_string(string, spacing=None):
    lmax = len(str(max(string)))
    if spacing is None:
        if lmax > 1:
            spacing = True
        else:
            spacing = False
    k = [str(_) for _ in string]
    k = ["_" * lmax + spacing*" " if int(_) < 0 else " " * (lmax - len(_)) + _ + spacing * " " for _ in k]
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
