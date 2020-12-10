from time import time


def main():
    with open("data/day10.txt", "r") as f:
        data = [int(line) for line in f]

    time_start = time()
    print(count1(data))
    print(count1alt(data))
    time_part1 = time()

    print(count2(data))
    time_part2 = time()

    print(f'Part one time: {1000*(time_part1-time_start):.0f}ms')
    print(f'Part two time: {1000*(time_part2-time_part1):.0f}ms')


# 76 x 32 = 2432
def count1(data):
    previous_jolts = 0
    total1 = 0
    total3 = 1
    for jolts in sorted(data):
        if (jolts-previous_jolts) == 1:
            total1 += 1
        else:
            total3 += 1
        previous_jolts = jolts
    return total1 * total3


def count1alt(data):
    previous_jolts = 0
    total = 10000
    for jolts in sorted(data):
        total += 1 if (jolts-previous_jolts) == 1 else 10000
        previous_jolts = jolts
    return total // 10000 * total % 10000


# 453551299002368
def count2(data):
    sorted_data = [0] + sorted(data)
    arrangements = {}
    arrangements[0] = 1
    for i in range(1, len(sorted_data)):
        arrangements[i] = 0
        for j in range(i - 1, -1, -1):
            if sorted_data[i] - sorted_data[j] > 3:
                break
            arrangements[i] += arrangements[j]
    return arrangements[len(sorted_data)-1]


if __name__ == "__main__":
    main()
