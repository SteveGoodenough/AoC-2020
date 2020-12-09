from itertools import combinations
from time import time


def main():
    with open("data/day9.txt", "r") as f:
        data = [int(line) for line in f]

    time_start = time()
    print(count1(data, 25))
    time_part1 = time()

    print(count2(data, 25))
    time_part2 = time()

    print(f'Part one time: {1000*(time_part1-time_start):.0f}ms')
    print(f'Part two time: {1000*(time_part2-time_part1):.0f}ms')


# 400480901
def count1(data, preamble):
    for i in range(preamble, len(data)):
        for j in (combinations(data[i-preamble:i], 2)):
            if j[0]+j[1] == data[i]:
                j = None
                break
        if j is not None:
            return data[i]


# 67587168
def count2(data, preamble):
    inv = count1(data, preamble)
    for i in range(preamble, len(data)):
        total = 0
        j = i
        while total <= inv:
            total += data[j]
            if total == inv:
                return min(data[j:i+1]) + max(data[j:i+1])
            j -= 1


if __name__ == "__main__":
    main()
