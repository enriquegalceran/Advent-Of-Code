import os
from itertools import product


def main(path_=None, verbose=1):
    if path_ is None:
        data = [
            "190: 10 19",
            "3267: 81 40 27",
            "83: 17 5",
            "156: 15 6",
            "7290: 6 8 6 15",
            "161011: 16 10 13",
            "192: 17 8 14",
            "21037: 9 7 18 13",
            "292: 11 6 16 20",
        ]
        # Solution = 190, 3267 and 292 -> 3749
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]
    if verbose > 0:
        print(data)
        print("\n".join(data))

    operation_dict = {0: "+", 1: "*"}

    valid_solutions1, correct_id1 = calculate_combinations(data, operation_dict)

    print(f"Solution Day 7 - Part 1: {valid_solutions1}")

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2
    # Demo part 2 solution = 11387

    operation_dict[2] = ""

    valid_solutions2, correct_id2 = calculate_combinations(data, operation_dict, correct_id1)

    print(f"Solution Day 7 - Part 2: {valid_solutions2}")


def calculate_combinations(data_, operation_dict, already_correct=None):
    valid_solutions = 0
    correct_id = []
    for i, case in enumerate(data_):
        print(f"{i}/{len(data_)}", end="\r", flush=True)
        if already_correct is None:
            pass
        elif i in already_correct:
            valid_solutions += int(case.split(": ")[0])
            continue
        question, options = case.split(": ")
        options = options.split(" ")
        question = int(question)
        options = [int(_) for _ in options]
        r = len(options) - 1
        combinations = all_possible_combinations(r, operation_dict)
        for c in combinations:
            tmp = calculate_combination(c, operation_dict, options, r)
            if tmp == question:
                valid_solutions += tmp
                correct_id.append(i)
                break
    print("")
    return valid_solutions, correct_id


def calculate_combination(c, operation_dict, options, r):
    tmp = options[0]
    for x in range(r):
        s = f"{tmp}{operation_dict[c[x]]}{options[x + 1]}"
        tmp = eval(s)
    return tmp


def all_possible_combinations(r, iterable):
    return [_ for _ in product(iterable, repeat=r)]








if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day7.txt"

    path = os.path.join(datapath, filename)
    main(path)
