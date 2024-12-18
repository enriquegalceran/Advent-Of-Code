import os
from functools import lru_cache


def main(path_=None, verbose=1):
    if path_ is None:
        # data = [
        #     "0 1 10 99 999",
        # ]
        # Solution test 1: 1 -> "1 2024 1 0 9 9 2021976"
        data = [
            "125 17",
        ]
        # Solution test 2: 6->22; 25 -> 55312
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]
    data = "".join(data)
    data = [int(_) for _ in data.split(" ")]
    if verbose > 0:
        print("Data:")
        print(data)

    # One Iteration

    new_list, nlist = blink(data, 25, verbose=0)

    print(f"Solution Day 11 - Part 1: {nlist}")

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2
    # Memoization

    sol2 = blink_cache_wrapper(data, 75)
    print(blink_cache_recursive.cache_info())
    print(f"Solution Day 11 - Part 1: {sol2}")


@lru_cache(maxsize=None)
def blink_cache_recursive(input_val, blinks_remaining):
    """
    After fighting for two days, I looked the solution up and adapted it a little bit to my code:
    https://github.com/RD-Dev-29/advent_of_code_24/blob/main/code_files/day11.py

    The idea is that you don't need to know the values, just the number of stones remaining after X blinks.
    It goes down until it blinks all 75 times and measures how many stones there are...
    ... thus, the only "non-recurrent" return is "if you finished blinking (blinks_remaining==0), you only have the
    input stone"

    :param input_val:
    :param blinks_remaining:
    :return:
    """
    if blinks_remaining == 0:
        return 1

    if input_val == 0:
        return blink_cache_recursive(1, blinks_remaining - 1)

    if len(str(input_val)) % 2 == 0:
        n = len(str(input_val))
        left = int(str(input_val)[:n//2])
        right = int(str(input_val)[n//2:])
        return blink_cache_recursive(left, blinks_remaining - 1) + blink_cache_recursive(right, blinks_remaining - 1)
    else:
        return blink_cache_recursive(input_val * 2024, blinks_remaining - 1)


@lru_cache(maxsize=None)
def blink_cache_recursive2(input_val, blinks_remaining):
    """
    Now that I learned of lru_cache, I am trying again my previous attempt

    It works, but storing enormous lists slows down the code so so so much (it does not store the final length, but
    the actual values...)

    :param input_val:
    :param blinks_remaining:
    :return:
    """
    if blinks_remaining == 0:
        return [input_val]

    if input_val == 0:
        k = [blink_cache_recursive2(1, blinks_remaining - 1)]
        return list(flatten(k))
    n_input = len(str(input_val))
    if n_input % 2 == 0:
        left = int(str(input_val)[:n_input//2])
        right = int(str(input_val)[n_input//2:])
        k = [blink_cache_recursive2(left, blinks_remaining - 1), blink_cache_recursive2(right, blinks_remaining - 1)]
        return list(flatten(k))
    else:
        k = [blink_cache_recursive2(input_val * 2024, blinks_remaining - 1)]
        return list(flatten(k))


def blink_cache_wrapper2(data, blinks):
    # For every element in the list, calculate the stones that will stay there
    input2outputstones = []
    for x in data:
        input2outputstones.append(blink_cache_recursive2(x, blinks))
    flattened_outputs = list(flatten(input2outputstones))
    print("Solution:", flattened_outputs)
    return sum(flattened_outputs)


def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i




def blink_cache_wrapper(data, blinks):
    # For every element in the list, calculate the stones that will stay there
    input2outputstones = [0] * len(data)
    for i, x in enumerate(data):
        input2outputstones[i] = blink_cache_recursive(x, blinks)
    return sum(input2outputstones)


def blink(input_list: list, blinks: int, verbose=0):
    if verbose > 0:
        print("Initial arrangement:")
        print(input_list)
    new_list = input_list.copy()
    for i in range(blinks):
        print(f"{i}/{blinks} - {len(new_list)}")
        new_list = blink_once(new_list)
        if verbose > 0:
            print(f"After {i + 1} blinks:")
            print(new_list)
    return new_list, len(new_list)


def blink_once(input_list: list):
    new_list = []
    for i, element in enumerate(input_list):
        # Rule 1
        if element == 0:
            new_list.append(1)
        # Rule 2
        elif len(str(element)) % 2 == 0:
            len_ele = len(str(element))
            new_list.append(int(str(element)[:len_ele // 2]))
            new_list.append(int(str(element)[len_ele // 2:]))
        # Rule 3
        else:
            new_list.append(element * 2024)
    return new_list




if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day11.txt"

    path = os.path.join(datapath, filename)
    main(path)
