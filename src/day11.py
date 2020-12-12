from time import time


def main():
    with open("data/day11.txt", "r") as f:
        data = f.read().splitlines()
        # data = f.read().split('\n\n')
        # data = [int(line) for line in f]

    time_start = time()
    print(count1(data))
    time_part1 = time()

    print(count2(data))
    time_part2 = time()

    print(f'Part one time: {1000*(time_part1-time_start):.0f}ms')
    print(f'Part two time: {1000*(time_part2-time_part1):.0f}ms')


# 2329
def count1(data):
    grid = ["." + line + "." for line in data]
    grid = ['.' * (len(data[0]) + 2)] + grid + ['.' * (len(data[0]) + 2)]
    while True:
        new_grid = calc_grid(grid)
        if new_grid == grid:
            total = 0
            for line in new_grid:
                total += line.count('#')
            return total
        grid = new_grid


def calc_grid(grid):
    new_grid = [grid[0]]
    for y in range(1, len(grid)):
        new_line = '.'
        for x in range(1, len(grid[0])-1):
            if grid[y][x] == "L":
                c = count_adjacent(grid, x, y)
                new_line += '#' if c == 0 else grid[y][x]
            elif grid[y][x] == "#":
                c = count_adjacent(grid, x, y)
                new_line += 'L' if c >= 4 else grid[y][x]
            else:
                new_line += '.'
        new_grid.append(new_line + '.')
    return new_grid


def count_adjacent(grid, x, y):
    adjacent = grid[y-1][x-1:x+2].count('#')
    adjacent += grid[y+1][x-1:x+2].count('#')
    adjacent += grid[y][x-1] == '#'
    adjacent += grid[y][x+1] == '#'
    return adjacent


# 2138
def count2(data):
    grid = ["." + line + "." for line in data]
    grid = ['.' * (len(data[0]) + 2)] + grid + ['.' * (len(data[0]) + 2)]
    while True:
        new_grid = calc_grid2(grid)
        if new_grid == grid:
            total = 0
            for line in new_grid:
                total += line.count('#')
            return total
        grid = new_grid


def calc_grid2(grid):
    new_grid = [grid[0]]
    for y in range(1, len(grid)):
        new_line = '.'
        for x in range(1, len(grid[0])-1):
            if grid[y][x] == "L":
                c = count_adjacent2(grid, x, y)
                new_line += '#' if c == 0 else grid[y][x]
            elif grid[y][x] == "#":
                c = count_adjacent2(grid, x, y)
                new_line += 'L' if c >= 5 else grid[y][x]
            else:
                new_line += '.'
        new_grid.append(new_line + '.')
    return new_grid


# this is, just a horror show
def count_adjacent2(grid, x, y):
    adjacent = 0
    for i in range(1, x):
        if grid[y][x-i] != '.':
            adjacent += grid[y][x-i] == '#'
            break
    for i in range(x + 1, len(grid[0])-1):
        if grid[y][i] != '.':
            adjacent += grid[y][i] == '#'
            break
    for i in range(1, y):
        if grid[y-i][x] != '.':
            adjacent += grid[y-i][x] == '#'
            break
    for i in range(1, len(grid) - y - 1):
        if grid[y+i][x] != '.':
            adjacent += grid[y+i][x] == '#'
            break
    for i in range(1, min(y, x)):
        if grid[y-i][x-i] != '.':
            adjacent += grid[y-i][x-i] == '#'
            break
    for i in range(1, min(y, len(grid[0])-x)):
        if grid[y-i][x+i] != '.':
            adjacent += grid[y-i][x+i] == '#'
            break
    for i in range(1, min(len(grid) - y, x)):
        if grid[y+i][x-i] != '.':
            adjacent += grid[y+i][x-i] == '#'
            break
    for i in range(1, min(len(grid) - y, len(grid[0])-x)):
        if grid[y+i][x+i] != '.':
            adjacent += grid[y+i][x+i] == '#'
            break
    return adjacent


if __name__ == "__main__":
    main()
