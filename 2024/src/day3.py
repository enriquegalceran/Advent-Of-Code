import os
import re


def main(path_=None, verbose=1):
    if path_ is None:
        data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]
            data = "".join(data)
    if verbose > 0:
        print(data)
        print("\n")

    accum = mult_and_add(data, verbose)

    print(f"Solution Day 3, Part 1: {accum}")

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2
    if path_ is None:
        data2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        if verbose > 0:
            print(data2)
            print("\n")
    else:
        data2 = data

    # Split between do() and don't()
    a = re.split(r"(do\(\))", data2)
    b = [re.split(r"(don't\(\))", _) for _ in a]
    b = [item for sublist in b for item in sublist]
    if verbose > 0:
        print(b)
        print("")

    # Split between mul() and undo()
    calculate = True
    accum_total = 0
    if verbose > 0:
        print("Calculate starts True")
        print("Current accumulated value: 0")
    for i, fragment in enumerate(b):
        if verbose > 1:
            print(f"\nFragment={i} - Calculate={calculate}:\n{fragment}")
        if fragment == "don't()":
            if verbose > 1:
                print(f"Calculate goes from {calculate} to False")
            calculate = False
        elif fragment == "do()":
            if verbose > 1:
                print(f"Calculate goes from {calculate} to True")
            calculate = True
        elif calculate:
            accum_total += mult_and_add(fragment, verbose)
            print(f"Current accumulated value: {accum_total}")

    print(f"\n\nSolution Day 3, Part 2: {accum_total}")


def mult_and_add(data, verbose=1):
    ocurrences = re.findall(r"mul\((\d+),(\d+)\)", data)
    accum = 0
    for case in ocurrences:
        l1 = len(case[0])
        l2 = len(case[1])
        if 4 > l1 > 0 and 4 > l2 > 0:
            x = int(case[0])
            y = int(case[1])
            print(f"mul({x},{y}) = {x * y}")
            accum += x * y
        elif verbose > 0:
            print(f"Invalid input: {case}")
    return accum


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day3.txt"

    path = os.path.join(datapath, filename)
    main(path, verbose=2)
