import os
import numpy as np


def main(path_=None, verbose=0, part=1):
    # Read Data
    if path_ is None:
        data = [
            "3-5",
            "10-14",
            "16-20",
            "12-18",
            "",
            "1",
            "5",
            "8",
            "11",
            "17",
            "32"
        ]
    else:
        with open(path_, "r") as file:
            data = file.readlines()
        data = [x.strip() for x in data]

    split_idx = data.index("")
    good_id_ranges = data[:split_idx]
    produce_id = data[split_idx + 1:]
    produce_id = [int(_) for _ in produce_id]

    good_ranges = [_.split("-") for _ in good_id_ranges]
    good_ranges = [[int(x.strip()) for x in _] for _ in good_ranges]
    good_ranges = sorted(good_ranges, key=lambda x: x[0])

    if part == 1:
        is_fresh = []
        for produce in produce_id:
            for good in good_ranges:
                if good[0] <= produce <= good[1]:
                    is_fresh.append(produce)
                    break
                if good[0] > produce:
                    break
        print(is_fresh)
        print(len(is_fresh))

    if part == 2:
        min_fresh_value = [_[0] for _ in good_ranges]
        max_fresh_value = [_[1] for _ in good_ranges]

        total_fresh_id = 0

        for i, (min_, max_) in enumerate(good_ranges):
            print("i:", i, min_, max_)

            for j in range(i):
                if min_ <= good_ranges[j][1]:
                    print("j:", j, good_ranges[j], f"Overlap! moving {min_} to {good_ranges[j][1]}")
                    min_ = good_ranges[j][1] + 1
            if min_ > max_:
                print("complete overlap!, skipping...")
                continue

            elements_current = max_ - min_ + 1
            print(f"cleaned {i}: {min_}-{max_} -> {elements_current}")
            total_fresh_id += elements_current

        print("total:", total_fresh_id)


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day5.txt"

    path = os.path.join(datapath, filename)
    main(path, 1, 2)
