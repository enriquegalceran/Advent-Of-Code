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
                found_something = False
                for j in range(1, klength//+1):
                    if klength % j == 0:
                        parts = [kstr[x:x+j] for x in range(0, klength, j)]
                        parts_set = list(set(parts))
                        if len(parts_set) == 1:
                            invalid_ids.append(k)
                            found_something = True
                    if found_something:
                        break
        print(f"Number of invalid elements: {len(invalid_ids)}. Sum of them: {sum(invalid_ids)}")


    print("pause here")


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day2.txt"

    path = os.path.join(datapath, filename)
    main(path, 1, 2)
