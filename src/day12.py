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


directions = "ESWNESW"


# 2280
def count1(data):
    direction = "E"
    n = 0
    e = 0
    for i in data:
        cmd = i[:1]
        dist = int(i[1:])
        # print(c, v)
        if cmd == "N":
            n += dist
        elif cmd == "S":
            n -= dist
        elif cmd == "E":
            e += dist
        elif cmd == "W":
            e -= dist
        elif cmd == "F":
            if direction == "E":
                e += dist
            elif direction == "W":
                e -= dist
            elif direction == "S":
                n -= dist
            else:
                n += dist
        elif cmd == "L":
            direction = directions[directions.find(direction) + 4 - dist // 90]
        elif cmd == "R":
            direction = directions[directions.find(direction) + dist // 90]
    return abs(n) + abs(e)


# 38693
def count2(data):
    n = 0
    e = 0
    wn = 1
    we = 10
    for i in data:
        c = i[:1]
        v = int(i[1:])
        # print(c, v, e, n, we, wn)
        # waypoint move
        if c == "N":
            wn += v
        elif c == "S":
            wn -= v
        elif c == "E":
            we += v
        elif c == "W":
            we -= v
        elif c == "L":
            for r in range(v // 90):
                t = we
                we = -wn
                wn = t
        elif c == "R":
            for r in range(v // 90):
                t = wn
                wn = -we
                we = t
        elif c == "F":
            e += we * v
            n += wn * v
        else:
            print(f'unknown command {i}')
            break
    # print(abs(n), abs(e))
    total = abs(n) + abs(e)
    return total


if __name__ == "__main__":
    main()
