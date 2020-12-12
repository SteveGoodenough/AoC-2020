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
        if grid == new_grid:
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
            if grid[y][x] == ".":
                new_line += '.'
            elif grid[y][x] == "L":
                c = count_adjacent(grid, x, y)
                if c == 0:
                    new_line += '#'
                else:
                    new_line += grid[y][x]
            else:
                c = count_adjacent(grid, x, y)
                if c >= 4:
                    new_line += 'L'
                else:
                    new_line += grid[y][x]
        new_grid.append(new_line + '.')
    return new_grid


def count_adjacent(grid, x, y):
    adjacent = grid[y-1][x-1:x+2].count('#')
    adjacent += grid[y+1][x-1:x+2].count('#')
    adjacent += grid[y][x-1] == '#'
    adjacent += grid[y][x+1] == '#'
    return adjacent


# 
def count2(data):
    total = 0
    return total


if __name__ == "__main__":
    main()
