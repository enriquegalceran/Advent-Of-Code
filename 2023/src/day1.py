import os
import re


def main(path_=None, verbose=1):
    if path_ is None:
        data = [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet"]
        # Solution = 142
    else:
        with open(path_, "r") as file:
            data = file.readlines()
            data = [_.strip() for _ in data]
    if verbose > 0:
        print(data)
        print("\n")

    cal = get_calibration(data)

    print(f"Solution Day 1, Part 1: {cal}")

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2

    if path_ is None:
        data = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]
        # Solution = 281

    written_numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }

    cal2 = get_cal_text(data, written_numbers)

    print(f"Solution Day 1, Part 2: {cal2}")


def get_cal_text(data_, written_numbers_):
    r_string = r"(?=(\d|" + "|".join(written_numbers_.keys()) + "))"
    accum = 0
    for line in data_:
        # There are some overlaps (eigthtwothree should return 8,2,3)
        matches = re.findall(r_string, line)
        numbers = [match for match in matches]
        numbers = [str(written_numbers_[_]) if _ in written_numbers_ else _ for _ in numbers]
        value = int(numbers[0] + numbers[-1])
        accum += value
    return accum


def get_calibration(data_):
    accum = 0
    for line in data_:
        numbers = re.findall(r"\d", line)
        value = int(numbers[0] + numbers[-1])
        accum += value
    return accum


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day1.txt"

    path = os.path.join(datapath, filename)
    main(path)
