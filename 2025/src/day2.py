import os
import re


def main(path_=None, verbose=0, part=1):
    # Read Data
    if path_ is None:
        data = ["11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"]
    else:
        with open(path_, "r") as file:
            data = file.readlines()
        data = [x.strip() for x in data]
    data = data[0].split(",")
    print(data)

    if part == 1:
        invalid_ids = []

        for i, value in enumerate(data):
            print(value)
            left, right = value.split("-")
            for k in range(int(left), int(right)+1):
                kstr = str(k)
                klength = len(kstr)
                if klength % 2 == 0:
                    if kstr[:(klength//2)] == kstr[(klength//2):]:
                        print("invalid!:", k)
                        invalid_ids.append(k)

            print(left, right)

        print("solution part1:", sum(invalid_ids))
        print("here")
    # a = re.search('[0-9]{2}', kstr)

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2

    if part == 2:
        invalid_ids = []
        for i, value in enumerate(data):
            print(value)
            left, right = value.split("-")
            for k in range(int(left), int(right)+1):
                kstr = str(k)
                klength = len(kstr)
                for j in range(1, klength):
                    if klength % j == 0:
                        repeated = False
                        for l in range(klength//j - 1):
                            if kstr[(l*j):((l+1)*j)] != kstr[((l+1)*j):((l+2)*j)]:
                                break



    print("pause here")


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day2.txt"

    path = os.path.join(datapath, filename)
    main(None, 1, 2)
