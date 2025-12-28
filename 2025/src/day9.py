import os
import numpy as np
import matplotlib.pyplot as plt


def main(path_=None, verbose=0, part=1):
    # Read Data
    if path_ is None:
        data = [
            "7, 1",
            "11, 1",
            "11, 7",
            "9, 7",
            "9, 5",
            "2, 5",
            "2, 3",
            "7, 3",
        ]
    else:
        with open(path_, "r") as file:
            data = file.readlines()
        data = [x.strip("\n") for x in data]

    data = [[int(x) for x in _.split(",")]for _ in data]
    x_values = [_[0] for _ in data]
    y_values = [_[1] for _ in data]

    if part == 1:

        max_area = 0
        for i in range(max(x_values)):
            p1 = data[i]
            for j in range(max(y_values)):
                p2 = data[j]
                dx = abs(p2[0] - p1[0]) + 1
                dy = abs(p2[1] - p1[1]) + 1
                area = dx * dy
                if area > max_area:
                    max_area = area

        print("Solution part1:", max_area)

    if part == 2:
        x_sorted = np.array(sorted(x_values))
        y_sorted = np.array(sorted(y_values))

        x_unique = np.unique(x_sorted)
        y_unique = np.unique(y_sorted)
        x_comp = np.arange(x_unique.size)
        y_comp = np.arange(y_unique.size)

        x_comp2orignal = {}
        x_original2comp = {}
        for comp, uniq in zip(x_comp, x_unique):
            x_comp2orignal[comp] = uniq
            x_original2comp[uniq] = comp
        y_comp2original = {}
        y_original2comp = {}
        for comp, uniq in zip(y_comp, y_unique):
            y_comp2original[comp] = uniq
            y_original2comp[uniq] = comp

        # x_new = np.zeros_like(x_values)
        # y_new = np.zeros_like(y_values)
        # for i, (x_old, y_old) in enumerate(zip(x_values, y_values)):
        #     x_new[i] = x_original2comp[x_old]
        #     y_new[i] = y_original2comp[y_old]

        data_comp = [[x_original2comp[_[0]], y_original2comp[_[1]]] for _ in data]

        data_comp_np = np.zeros((max(y_comp)+2, max(x_comp)+2), dtype=np.uint8)
        for i, p2 in enumerate(data_comp):
            p1 = data_comp[i-1]
            data_comp_np[p2[1], p2[0]] = 3
            if p1[0] == p2[0]:
                data_comp_np[min(p2[1], p1[1]):max(p2[1], p1[1]), p2[0]] = 3
            else:
                data_comp_np[p2[1], min(p2[0], p1[0]):max(p2[0], p1[0])] = 3

        print(data_comp_np)

        plt.imshow(data_comp_np, vmin=0, vmax=3, interpolation=None)
        plt.show()

        print("Looking at the compressed map, we can see the map and find a coordinate which is inside:"
              "X:middle of the compressed coordinates, Y:3/4 of the coompressed coordinates.")

        # Flood area:
        if path_ is None:
            starting_flood_coordinate = (1, 2)
        else:
            starting_flood_coordinate = (100, 50)

        data_comp_np[starting_flood_coordinate[0], starting_flood_coordinate[1]] = 1

        floodfill(data_comp_np, plot=False)

        plt.imshow(data_comp_np, vmin=0, vmax=3, interpolation=None)
        plt.show()

        # Search per pair
        max_area = 0
        max_area_region = None
        for i in range(len(data_comp)):
            print(f"{i}/{len(data_comp)}", end="\r", flush=True)
            x1, y1 = data_comp[i]
            for j in range(i, len(data_comp)):
                x2, y2 = data_comp[j]
                if x1 == x2:
                    xa = np.array([x1])
                elif x1 > x2:
                    xa = np.arange(x2, x1 + 1)
                else:
                    xa = np.arange(x1, x2 + 1)
                if y1 == y2:
                    ya = np.array([y1])
                elif y1 > y2:
                    ya = np.arange(y2, y1 + 1)
                else:
                    ya = np.arange(y1, y2 + 1)

                region = data_comp_np[np.ix_(ya, xa)]

                if np.all(region > 0):
                    p1 = data[i]
                    p2 = data[j]
                    dx = abs(p2[0] - p1[0]) + 1
                    dy = abs(p2[1] - p1[1]) + 1
                    area = dx * dy
                    if area > max_area:
                        max_area = area
                        max_area_region = np.ix_(ya, xa)
        print(max_area)

        data_comp_np[max_area_region] = 4

        plt.imshow(data_comp_np, vmin=0, vmax=4, interpolation=None)
        plt.show()


def floodfill(matrix, processing=1, finished=2, empty=0, plot=False, max_attempts=1000):

    # locate processing arrays
    i = 0
    if plot:
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ims = ax.imshow(matrix, vmin=0, vmax=3, interpolation=None)

    while i < max_attempts:
        idx_processing_x, idx_processing_y = np.where(matrix == processing)
        if len(idx_processing_x) == 0:
            break
        for pix_x, pix_y in zip(idx_processing_x, idx_processing_y):
            for ix in [-1, 0, 1]:
                for iy in [-1, 0, 1]:
                    if matrix[pix_x + ix, pix_y + iy] == empty:
                        matrix[pix_x + ix, pix_y + iy] = processing
            matrix[pix_x, pix_y] = finished
        if plot:
            ims.set_data(matrix)
            fig.canvas.draw()
            fig.canvas.flush_events()
            ax.set_title(i)
        i += 1
    if i == max_attempts:
        Warning("MAX ATTEMPTS REACHED!")
        print("Warning! MAX ATTEMPTS REACHED!")


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day9.txt"

    path = os.path.join(datapath, filename)
    main(path, 1, 2)
