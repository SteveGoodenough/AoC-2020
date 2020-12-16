from time import time


def main():
    with open("data/day16.txt", "r") as f:
        # data = f.read().splitlines()
        # data = [line.split() for line in f.readlines()]
        data = f.read().split('\n\n')
        # data = [int(line) for line in f]

    time_start = time()
    print(count1(data))
    time_part1 = time()

    print(count2(data))
    time_part2 = time()

    print(f'Part one time: {1000*(time_part1-time_start):.0f}ms')
    print(f'Part two time: {1000*(time_part2-time_part1):.0f}ms')


# 22057
def count1(data):
    numbers, tickets = parse_data(data)
    total = 0
    for ticket in tickets:
        for value in ticket.split(','):
            if int(value) not in numbers:
                total += int(value)
    return total


def parse_data(data):
    numbers = []
    for line in data[0].split('\n'):
        _, r1, r2, r3, r4 = line.replace(' or', ':').replace('-', ':').split(':')
        numbers += [i for i in range(int(r1), int(r2)+1)]
        numbers += [i for i in range(int(r3), int(r4)+1)]
    tickets = data[2].split()[2:]
    return numbers, tickets


def count2(data):
    return 0


if __name__ == "__main__":
    main()
