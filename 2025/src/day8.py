import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from math import sqrt


def get_distance(x1, x2):
    return sqrt(sum([(x1[i]-x2[i])**2 for i in range(3)]))


def get_row_col(k, n, m=None):
    if m is None:
        m = n
    row = k // m
    col = k % m
    return row, col


def main(path_=None, verbose=0, part=1):
    # Read Data
    if path_ is None:
        data = ["162,817,812",
                "57,618,57",
                "906,360,560",
                "592,479,940",
                "352,342,300",
                "466,668,158",
                "542,29,236",
                "431,825,988",
                "739,650,466",
                "52,470,668",
                "216,146,977",
                "819,987,18",
                "117,168,530",
                "805,96,715",
                "346,949,466",
                "970,615,88",
                "941,993,340",
                "862,61,35",
                "984,92,344",
                "425,690,689",
                ]
        total_n_connections = 10
    else:
        with open(path_, "r") as file:
            data = file.readlines()
        data = [x.strip("\n") for x in data]
        total_n_connections = 1000

    # replaced with "_" for beter visualization
    data = [[int(x) for x in _.split(",")] for _ in data]
    n_points = len(data)
    print(data)

    print("Finished Loading")

    if part == 1:
        distances = np.full((n_points, n_points), np.inf)
        for i in range(n_points):
            x1 = data[i]
            for j in range(i, n_points):
                x2 = data[j]
                if i == j:
                    distances[i, j] = np.inf
                    continue
                dist = get_distance(x1, x2)
                distances[i, j] = dist
        print("Finished calculating distances")
        current_n_of_networks = 0
        member_of_network = np.ones(n_points, dtype=int) * -1
        pairs_of_connections = []

        distance_values, index_distances = np.unique(distances, return_index=True)

        single_network = False
        i_connection = 0
        while not single_network:
            dist_i = distance_values[i_connection]
            index_i = index_distances[i_connection]
            connection1, connection2 = get_row_col(index_i, n_points)
            network1 = member_of_network[connection1]
            network2 = member_of_network[connection2]
            if network1 == -1 and network2 == -1:
                if verbose > 0:
                    print(f"{i_connection}: new network! {connection1}({data[connection1]}) + {connection2}({data[connection2]}) ({dist_i:.3f}) [{current_n_of_networks}]")
                member_of_network[connection1] = current_n_of_networks
                member_of_network[connection2] = current_n_of_networks
                pairs_of_connections.append((data[connection1], data[connection2]))
                current_n_of_networks += 1
            elif network1 == network2:
                if verbose > 0:
                    print(f"{i_connection}: both [{connection1}({data[connection1]}) + {connection2}({data[connection2]})] already connected to network {network1}!")
            elif network1 != network2 and network1 != -1 and network2 != -1:
                if verbose > 0:
                    print(f"{i_connection}: two networks are merging! {connection1}({data[connection1]})[{network1}] + {connection2}({data[connection2]})[{network2}] Moving [{network2}] into [{network1}]")
                pairs_of_connections.append((data[connection1], data[connection2]))
                member_of_network[member_of_network == network2] = network1
            else:
                if network1 == -1:
                    member_of_network[connection1] = network2
                    pairs_of_connections.append((data[connection1], data[connection2]))
                    if verbose > 0:
                        print(f"{i_connection}: Network {network2} grew! Adding {connection1}({data[connection1]}) to {connection2}({data[connection2]})  ({dist_i:.3f})")
                elif network2 == -1:
                    member_of_network[connection2] = network1
                    pairs_of_connections.append((data[connection1], data[connection2]))
                    if verbose > 0:
                        print(f"{i_connection}: Network {network1} grew! Adding {connection2}({data[connection2]}) to {connection1}({data[connection1]})  ({dist_i:.3f})")
                else:
                    raise ValueError("Should not be here neither!")
            if i_connection == total_n_connections:
                print("\n\n\nAll connections for part 1 are made!")
                networks, idx_in_network, n_in_network = np.unique(member_of_network[member_of_network >= 0],
                                                                   return_counts=True, return_index=True)
                not_connected = (member_of_network == -1).sum()
                n_in_network, networks, idx_in_network = zip(
                    *sorted(zip(n_in_network, networks, idx_in_network), reverse=True))

                print("Name of networks:", networks)
                print("Number of elements in each network:", n_in_network)
                print("Not connected:", not_connected)
                print("Solution part1:", n_in_network[0] * n_in_network[1] * n_in_network[2], "\n\n\n")

            network_unique = np.unique(member_of_network)
            if network_unique.size == 1:
                single_network = True
            i_connection += 1


        networks, idx_in_network, n_in_network = np.unique(member_of_network[member_of_network >= 0],
                                                           return_counts=True, return_index=True)
        not_connected = (member_of_network == -1).sum()
        n_in_network, networks, idx_in_network = zip(
            *sorted(zip(n_in_network, networks, idx_in_network), reverse=True))
        n_networks = len(networks)

        print("Name of networks:", networks)
        print("Number of elements in each network:", n_in_network)
        print("Not connected:", not_connected)
        print("Last pair:", connection1, connection2)
        print("Coordinates las pair:", data[connection1], data[connection2])
        print("Solution part2:", data[connection1][0] * data[connection2][0])
        print(f"Total cable distance: {sum([get_distance(*_) for _ in pairs_of_connections]):,.3f}")

        xs = np.array([_[0] for _ in data])
        ys = np.array([_[1] for _ in data])
        zs = np.array([_[2] for _ in data])

        cmap = matplotlib.cm.get_cmap('Spectral')

        markersize = 25
        linewidth = 5

        pairs_of_connections_network = np.zeros(len(pairs_of_connections), dtype=int)
        for i_p, pair in enumerate(pairs_of_connections):
            p1 = pair[0]
            idx_p1 = data.index(p1)
            pairs_of_connections_network[i_p] = member_of_network[idx_p1]
        pairs_of_connections_array = np.array(pairs_of_connections)

        fig = plt.figure(figsize=(20, 20))
        ax = fig.add_subplot(projection='3d')
        for i_n, n in enumerate(networks):
            color_n = cmap(i_n/n_networks)
            mask_current_network = member_of_network == n
            mask_current_pair = pairs_of_connections_network == n
            xs_n = xs[mask_current_network]
            ys_n = ys[mask_current_network]
            zs_n = zs[mask_current_network]
            ax.scatter(xs_n, ys_n, zs_n, color=color_n, s=markersize)
            pairs_in_network = pairs_of_connections_array[mask_current_pair]
            for pairs in pairs_in_network:
                ax.plot([pairs[0][0], pairs[1][0]], [pairs[0][1], pairs[1][1]], zs=[pairs[0][2], pairs[1][2]], linewidth=linewidth, color=color_n)
        mask_current_network = member_of_network == -1
        xs_n = xs[mask_current_network]
        ys_n = ys[mask_current_network]
        zs_n = zs[mask_current_network]
        ax.scatter(xs_n, ys_n, zs_n, color="black", s=markersize)
        plt.show()

        print("finished")


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day8.txt"

    path = os.path.join(datapath, filename)
    main(path, 1, 1)
