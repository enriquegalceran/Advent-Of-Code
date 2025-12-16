import os
import numpy as np


def main(path_=None, verbose=0, part=1):
    # Read Data
    if path_ is None:
        data = [
            ".......S.......",
            "...............",
            ".......^.......",
            "...............",
            "......^.^......",
            "...............",
            ".....^.^.^.....",
            "...............",
            "....^.^...^....",
            "...............",
            "...^.^...^.^...",
            "...............",
            "..^...^.....^..",
            "...............",
            ".^.^.^.^.^...^.",
            "...............",
        ]
    else:
        with open(path_, "r") as file:
            data = file.readlines()
        data = [x.strip("\n") for x in data]

    # replaced with "_" for beter visualization
    data = [x.replace(".", "_") for x in data]
    print("\n".join(data))

    s = data[0].index("S")
    data_np = np.zeros((len(data), len(data[0])), dtype=int)
    data_np[0, s] = -1
    data_np[1, s] = 1
    for i in range(data_np.shape[0]):
        for j in range(data_np.shape[1]):
            if data[i][j] == "^":
                data_np[i, j] = -1

    if part == 1:
        splits = 0
        for r in range(2, data_np.shape[0]):
            where_beam_previous = np.where(data_np[r-1, :] == 1)[0]
            where_splitter = np.where(data_np[r, :] == -1)[0]
            new_beams = np.zeros(data_np.shape[1], dtype=int)
            for beam in where_beam_previous:
                if beam in where_splitter:
                    splits += 1
                    if beam > 0:
                        new_beams[beam - 1] = 1
                    if beam < data_np.shape[1] - 1:
                        new_beams[beam + 1] = 1
                else:
                    new_beams[beam] = 1
            new_beams[np.where(data_np[r, :] == -1)] = -1
            data_np[r, :] = new_beams
            if verbose > 1:
                print(data_np)
        print("part 1: Total splits:", splits)

        data_print = []
        for k in range(data_np.shape[0]):
            tmp = []
            for j in range(data_np.shape[1]):
                if data_np[k, j] == 0:
                    tmp.append("_")
                elif data_np[k, j] == 1:
                    tmp.append("|")
                elif data_np[k, j] == -1:
                    tmp.append("^")
            data_print.append("".join(tmp))
        print("\n".join(data_print))

    if part == 2:
        for r in range(2, data_np.shape[0]):
            where_beam_previous = np.where(data_np[r-1, :] > 0)[0]
            where_splitter = np.where(data_np[r, :] == -1)[0]
            new_beams = np.zeros(data_np.shape[1], dtype=int)
            for beam in where_beam_previous:
                beam_path_options = data_np[r-1, beam]
                if beam in where_splitter:
                    if beam > 0:
                        new_beams[beam - 1] += beam_path_options
                    if beam < data_np.shape[1] - 1:
                        new_beams[beam + 1] += beam_path_options
                else:
                    new_beams[beam] += beam_path_options
            new_beams[np.where(data_np[r, :] == -1)] = -1
            data_np[r, :] = new_beams
            if verbose > 1:
                print(data_np)
        print(data_np)
        total_paths = data_np[-1, :].sum()
        print("part 2: Total paths:", total_paths)
        print("finished")



if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day7.txt"

    path = os.path.join(datapath, filename)
    main(path, 2, 2)
