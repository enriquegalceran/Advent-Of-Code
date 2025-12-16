import os
import numpy as np


def main(path_=None, verbose=0, part=1):
    # Read Data
    if path_ is None:
        data = ["123 328  51 64 ",
                " 45 64  387 23 ",
                "  6 98  215 314",
                "*   +   *   +  "]
    else:
        with open(path_, "r") as file:
            data = file.readlines()
        data = [x.strip("\n") for x in data]

    if part == 1:
        data = [x.strip() for x in data]
        data = [_.split() for _ in data]
        operators = data[-1]
        data = [[int(x) for x in _] for _ in data[:-1]]
        n_operations = len(operators)
        n_elements = len(data)
        print(data)
        total_sum = 0
        for i in range(n_operations):
            operation = operators[i]
            if operation == "+":
                tmp = 0
            elif operation == "*":
                tmp = 1
            else:
                raise ValueError("operator is not + or *")
            for j in range(n_elements):
                if operation == "+":
                    tmp += data[j][i]
                elif operation == "*":
                    tmp *= data[j][i]
                else:
                    raise ValueError("operator is not + or *")

            total_sum += tmp
            print(f"For column{i}, the result is {tmp}")
        print(f"Total value: {total_sum}")

    if part == 2:
        # Now we read right to left
        ncolumns = len(data[0])
        n_rows = len(data) - 1

        # Find separations:
        separations = []
        for c in reversed(range(ncolumns)):
            column_values = "".join([_[c] for _ in data])
            if column_values == " "*(n_rows + 1):
                separations.append(c)
        rev_separations = list(reversed(separations))
        rev_separations += [len(data[0])]

        total_sum = 0
        for k, sep in enumerate(rev_separations):
            # Define start and stop
            if k == 0:
                start = 0
            else:
                start = rev_separations[k-1]+1
            end = sep

            # Get each element we need to multiply
            elements = []
            for j in range(start, end):
                elements.append(int("".join([_[j] for _ in data[:-1]])))
            operator = data[-1][start]

            # Perform the actual operation
            if operator == "+":
                tmp = 0
                for _ in elements:
                    tmp += _
            elif operator == "*":
                tmp = 1
                for _ in elements:
                    tmp *= _
            else:
                raise ValueError("Wrong operator")

            # Add to total
            total_sum += tmp
            if verbose > 0:
                print(k, start, end, elements, operator)

        print(f"Total sum: {total_sum}")


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day6.txt"

    path = os.path.join(datapath, filename)
    main(path, 1, 2)
