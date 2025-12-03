import os
# from itertools import combinations
import functools


@functools.cache
def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)




def main(path_=None, verbose=0, part=1):
    # Read Data
    if path_ is None:
        data = ["987654321111111",
                "811111111111119",
                "234234234234278",
                "818181911112111"
                ]
    else:
        with open(path_, "r") as file:
            data = file.readlines()
        data = [x.strip() for x in data]

    # print(data)

    if part == 1:
        total_joltage = 0
        for line in data:
            max_joltage = -1
            for i in range(len(line)):
                for j in range(i+1, len(line)):
                    combined = int(line[i] + line[j])
                    if int(combined) > max_joltage:
                        max_joltage = combined
            total_joltage += max_joltage
        print(f"Solution day 3, part 1: {total_joltage}")

    # ------------------------------------------------------------------------------------------------------------------
    # Part 2

    if part == 2:
        # total_joltage = 0
        # for line in data:
        #     Works only for the test, not the complete input data with 100
        #     a = list(combinations(line, 6))
        #     a.sort(reverse=True)
        #     b = a[0]
        #     b = "".join(b)
        #
        #     print(int(b))
        #     total_joltage += int(b)

        # taken from : https://www.reddit.com/r/adventofcode/comments/1pcxkif/2025_day_3_mega_tutorial/
        """
        The idea is to make it a memoization test. let's take a simpler example with '34245' and take 3 numbers
        
        We will iterate over each digit in the following manner:
        Let us write the task as [34245|3]
        
        option 1: we discard 3; option 2: we keep 3.
        
        so we check the 2 options: 3e(3-1)+[4245|2]  vs. [4245|3]
        And now this is the memoization task!
        """

        # @functools.lru_cache()
        def max_joltage_dict(value: str, digit: int, memory=None):

            # There are values left, but no more space:
            if digit == 0:
                memory[f"{value},{digit}"] = 0
                return 0

            if memory is None:
                memory = {-1:0}
            elif f"{value},{digit}" in memory.keys():
                memory[-1] += 1
                print(memory[-1], end="\r", flush=True)
                return memory[f"{value},{digit}"]

            # length of value==digits:
            if len(value) == digit:
                return value

            # Option 1
            a = int(value[0]) * 10 ** (digit - 1) + int(max_joltage_dict(value[1:], digit - 1, memory))

            # Option 2
            b = int(max_joltage_dict(value[1:], digit, memory))

            # See which is larger and return that
            c = str(max(a, b))

            # Populate memory
            memory[f"{value},{digit}"] = c

            return c

        @functools.lru_cache(maxsize=300000)
        def max_joltage_cache(value: str, digit: int):

            # There are values left, but no more space:
            if digit == 0:
                return 0

            # length of value==digits:
            if len(value) == digit:
                return value

            # Option 1
            a = int(value[0]) * 10 ** (digit - 1) + int(max_joltage_cache(value[1:], digit - 1))

            # Option 2
            b = int(max_joltage_cache(value[1:], digit))

            # See which is larger and return that
            return str(max(a, b))

        total_joltage = 0
        previous_cache = max_joltage_cache.cache_info()
        for i, line in enumerate(data):
            joltage = max_joltage_cache(line, 12)
            current_cache = max_joltage_cache.cache_info()
            # print(f"\n{line} - {joltage}")
            print(f"{i:{len(str(len(data)))}d}/{len(data)}- Hits:{current_cache.hits - previous_cache.hits} - "
                  f"Misses: {current_cache.misses - previous_cache.misses} - "
                  f"Calls: { (current_cache.hits - previous_cache.hits) + (current_cache.misses - previous_cache.misses)} - "
                  f"Efficiency: {100.0 * (current_cache.hits - previous_cache.hits) / ((current_cache.hits - previous_cache.hits) + (current_cache.misses - previous_cache.misses)) :.2f}% - "
                  f"Extra size: {current_cache.currsize - previous_cache.currsize} - "
                  f"Total size: {current_cache.currsize}({current_cache.currsize/current_cache.maxsize*100.0:.2f}%) - "
                  f"Total efficiency: {current_cache.hits/ (current_cache.hits+ current_cache.misses)*100.0:.2f}%")
            previous_cache = current_cache
            # print(max_joltage_cache.cache_info())
            total_joltage += int(joltage)

        print(f"Solution day 3, part 2: {total_joltage}")

        print("here")




        print(f"Solution day 3, part 2: {total_joltage}")


if __name__ == "__main__":
    datapath = "../DATA/"
    filename = "day3.txt"

    path = os.path.join(datapath, filename)
    main(path, 1, 2)
