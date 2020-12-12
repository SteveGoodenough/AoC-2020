from time import time


def main():
    with open("data/day12.txt", "r") as f:
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


directions = "ESWN" * 2
movement = {'N': (1, 0), 'S': (-1, 0), 'E': (0, 1), 'W': (0, -1)}


# 2280
def count1(data):
    direction = "E"
    north = 0
    east = 0
    for line in data:
        cmd = line[0]
        dist = int(line[1:])
        if cmd in "NSEW":
            north += dist * movement[cmd][0]
            east += dist * movement[cmd][1]
        elif cmd == "F":
            north += dist * movement[direction][0]
            east += dist * movement[direction][1]
        elif cmd == "L":
            direction = directions[directions.find(direction) + 4 - dist // 90]
        elif cmd == "R":
            direction = directions[directions.find(direction) + dist // 90]
    return abs(north) + abs(east)


# 38693
def count2(data):
    north = 0
    east = 0
    waypoint_north = 1
    waypoint_east = 10
    for line in data:
        cmd = line[0]
        dist = int(line[1:])
        if cmd in "NSEW":
            waypoint_north += dist * movement[cmd][0]
            waypoint_east += dist * movement[cmd][1]
        elif cmd == "L":
            for _ in range(dist // 90):
                waypoint_north, waypoint_east = waypoint_east, -waypoint_north
        elif cmd == "R":
            for _ in range(dist // 90):
                waypoint_north, waypoint_east = -waypoint_east, waypoint_north
        elif cmd == "F":
            east += waypoint_east * dist
            north += waypoint_north * dist
    return abs(north) + abs(east)


if __name__ == "__main__":
    main()
