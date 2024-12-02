import os


def main(path_=None, verbose=1):
    if path_ is None:
        data = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9],
        ]
    else:
        with open(path_, "r") as file:
            data = file.readlines()
        data = [x.strip().split() for x in data]
        data = [[int(k) for k in _] for _ in data]

    if verbose > 0:
        print("Data:")
        print(data)

    def is_decreasing(vector):
        for x in range(1, len(vector)):
            if vector[x] > vector[x - 1]:
                return False
        return True

    def is_increasing(vector):
        for x in range(1, len(vector)):
            if vector[x] < vector[x - 1]:
                return False
        return True

    def within_bounds(vector, lower, upper):
        for x in range(1, len(vector)):
            dif = abs(vector[x] - vector[x - 1])
            if dif > upper or dif < lower:
                return False
        return True

    def is_safe(vector, lower=1, upper=3):
        return (is_decreasing(vector) or is_increasing(vector)) and within_bounds(vector, lower, upper)

    safe = 0
    for i in range(len(data)):
        vector_i = data[i]
        decreasing = is_decreasing(vector_i)
        increasing = is_increasing(vector_i)
        bounds = within_bounds(vector_i, 1, 3)
        is_safe_ = is_safe(vector_i)
        if verbose > 0:
            print(f"Row {i}: Decreasing: {decreasing}, Increasing: {increasing}, Bounds: {bounds}, Safe: {is_safe_}")
        safe += is_safe_

    print(f"Solution Day 2, Part 1: {safe}")

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2

    def problem_dampener(vector):
        if is_safe(vector):
            return True, -1
        else:
            for x in range(len(vector)):
                vector2 = vector.copy()
                vector2.pop(x)
                if is_safe(vector2):
                    return True, x
            return False, -1

    is_safe_dampened = 0
    for i in range(len(data)):
        vector_i = data[i]
        is_safe_dampened_i, id_ = problem_dampener(vector_i)
        if verbose > 0:
            if id_ == -1:
                if is_safe_dampened_i:
                    print(f"Row {i}: {vector_i} - Is Safe!")
                else:
                    print(f"Row {i}: {vector_i} - Is Not Safe regardless of dampening!")
            else:
                dampened_vector_string = vector_i.copy()
                dampened_vector_string[id_] = "*" + str(dampened_vector_string[id_]) + "*"
                dampened_vector_string = str(dampened_vector_string).replace("'", "")
                print(f"Row {i}: {dampened_vector_string} - Is Safe! Dampening at {id_}!")
        is_safe_dampened += is_safe_dampened_i

    print(f"Solution Day 2, Part 2: {is_safe_dampened}")


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day2.txt"

    path = os.path.join(datapath, filename)
    main(path, verbose=0)
