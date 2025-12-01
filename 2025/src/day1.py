import os


def main(path_=None, verbose=0):
    # Read Data
    if path_ is None:
        data = [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82"
        ]
    else:
        with open(path_, "r") as file:
            data = file.readlines()
        data = [x.strip() for x in data]
    starting_position = 50
    print(data)

    # Each time it moves to the right, it adds that value. Each time it moves to the left, it removes that value.
    # We need to count the amount of times it points at ZERO.
    print(f"Starting position: {starting_position}")
    position = starting_position
    count_zeros = 0
    for i, code in enumerate(data):
        if code[0] == "L":
            position -= int(code[1:])
        else:
            position += int(code[1:])

        # # If negative, add 100
        # while position < 0:
        #     position += 100
        #
        # # If above 99, subtract 100
        # while position > 100:
        #     position -= 100
        # All this can be done much more efficiently with a simple 'mod' function:
        position %= 100

        if position == 0:
           count_zeros += 1
        if verbose > 0:
            print(f"Code: {code}. New position: {position}")

    print(f"Final tally of zeros: {count_zeros}")

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # Part 2:

    # Count every zero
    print("PART 2")

    print(f"Starting position: {starting_position}")
    position = starting_position
    position_before = position
    count_zeros = 0
    count_zeros_before = 0
    for i, code in enumerate(data):
        if code[0] == "L":
            position -= int(code[1:])
        else:
            position += int(code[1:])

        # Exactly zero
        if position == 0:
            count_zeros += 1
        # any other number
        elif 0 < position < 100:
            pass
        # Above/Below 99/0
        else:
            if position < 0:
                # If negative, add 100 and count +1
                while position < 0:
                    position += 100
                    count_zeros += 1
                # If after all these turns, it stops at zero, add one
                if position == 0:
                    count_zeros += 1
            # If above 99, subtract 100 and count +1
            while position >= 100:
                position -= 100
                count_zeros += 1

        # When turning left STARTING from zero, there will be a zero counted twice. Remove one of them.
        if position_before == 0 and code[0] == "L":
            count_zeros -= 1

        diff_with_before = count_zeros - count_zeros_before
        count_zeros_before = count_zeros
        position_before = position
        if verbose > 0:
            print(f"Code: {code}. New position: {position} - passed through 0: {diff_with_before}")

    print(f"Final tally of zeros: {count_zeros}")





    print("pause here")


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day1.txt"

    path = os.path.join(datapath, filename)
    main(path, 1)
