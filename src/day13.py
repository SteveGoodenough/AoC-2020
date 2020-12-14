from time import time


def main():
    with open("data/day13.txt", "r") as f:
        data = f.read().splitlines()
        # data = [line.split() for line in f.readlines()]
        # data = f.read().split('\n\n')
        # data = [int(line) for line in f]

    time_start = time()
    print(count1(data))
    time_part1 = time()

    print(count2(data))
    time_part2 = time()

    print(f'Part one time: {1000*(time_part1-time_start):.0f}ms')
    print(f'Part two time: {1000*(time_part2-time_part1):.0f}ms')


# 1835
def count1(data):
    time = int(data[0])
    buses = [int(bus) for bus in data[1].split(',') if bus != 'x']
    the_bus = 0
    time_diff = 99999
    for bus in buses:
        if (bus_time_diff := bus - time % bus) < time_diff:
            time_diff = bus_time_diff
            the_bus = bus
    return the_bus * time_diff


#
def count2(data):
    return 3417


if __name__ == "__main__":
    main()
