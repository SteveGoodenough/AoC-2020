from time import time
from collections import defaultdict


def main():
    with open("data/day16.txt", "r") as f:
        # data = f.read().splitlines()
        # data = [line.split() for line in f.readlines()]
        data = f.read().split('\n\n')
        # data = [int(line) for line in f]

    time_start = time()
    print(count1(data))
    time_part1 = time()

    # print(count2(data))
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


def parse_data2(data):
    num = defaultdict(str)
    fields = []
    for index, line in enumerate(data[0].split('\n')):
        field, r1, r2, r3, r4 = line.replace(' or', ':').replace('-', ':').split(':')
        fields.append(field)
        for i in range(int(r1), int(r2)+1):
            num[i] = num[i] + ":" + field
        for i in range(int(r3), int(r4)+1):
            num[i] = num[i] + ":" + field
    tickets = data[2].split()[2:]
    return num, fields, tickets


# 
def count2(data):
    print()
    num, fields, tickets = parse_data2(data)
    filtered_tickets = []
    for ticket in tickets:
        ok = True
        for value in ticket.split(','):
            if int(value) not in num:
                ok = False
                break
        if ok:
            filtered_tickets.append(ticket)
# class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19

# your ticket:
# 11,12,13

# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9
# Based on the nearby tickets in the above example,
# the first position must be row,
# the second position must be class,
# and the third position must be seat
# you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

# index in each ticket
    tf = defaultdict(str)
    for ticket in filtered_tickets:
        for index, value in enumerate(ticket.split(',')):
            tf[index] = tf[index] + num[int(value)]
            # print(index, value, num[int(value)])
    print(num)
    for f in fields:
        print('field:', f)
    print(tf)
    for k, v in tf.items():
        print(v)
        for f in fields:
            if v.count(f) == 3:
                print(">>>", f, "<<<", k, v, v.count(f))

    total = 0
    return total


if __name__ == "__main__":
    main()
