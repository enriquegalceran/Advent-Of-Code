import os
import re
import math


def main(path_=None, verbose=1):
    if path_ is None:
        data = [
            "",
        ]
        # Solution = 8
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]
    if verbose > 0:
        print(data)
        print("\n")










if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day3_2023.txt"

    path = os.path.join(datapath, filename)
    main(path, verbose=2)
