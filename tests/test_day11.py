from src.day11 import count1, count2
from src.day11 import calc_grid, calc_grid2


def test_calc_grid():
    input_data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    data = [line for line in input_data.splitlines()]
    grid = ["." + line + "." for line in data]
    grid = ['.' * (len(data[0]) + 2)] + grid + ['.' * (len(data[0]) + 2)]

    grid = calc_grid(grid)
    assert grid == [
        '............',
        '.#.##.##.##.',
        '.#######.##.',
        '.#.#.#..#...',
        '.####.##.##.',
        '.#.##.##.##.',
        '.#.#####.##.',
        '...#.#......',
        '.##########.',
        '.#.######.#.',
        '.#.#####.##.',
        '............',
    ]

    grid = calc_grid(grid)
    assert grid == [
        '............',
        '.#.LL.L#.##.',
        '.#LLLLLL.L#.',
        '.L.L.L..L...',
        '.#LLL.LL.L#.',
        '.#.LL.LL.LL.',
        '.#.LLLL#.##.',
        '...L.L......',
        '.#LLLLLLLL#.',
        '.#.LLLLLL.L.',
        '.#.#LLLL.##.',
        '............',
    ]

    grid = calc_grid(grid)
    assert grid == [
        '............',
        '.#.##.L#.##.',
        '.#L###LL.L#.',
        '.L.#.#..#...',
        '.#L##.##.L#.',
        '.#.##.LL.LL.',
        '.#.###L#.##.',
        '...#.#......',
        '.#L######L#.',
        '.#.LL###L.L.',
        '.#.#L###.##.',
        '............',
    ]


def test_part_one():
    input_data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    data = [line for line in input_data.splitlines()]
    assert count1(data) == 37


def test_calc_grid2():
    input_data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    expected_grid_1 = [
        '............',
        '.#.##.##.##.',
        '.#######.##.',
        '.#.#.#..#...',
        '.####.##.##.',
        '.#.##.##.##.',
        '.#.#####.##.',
        '...#.#......',
        '.##########.',
        '.#.######.#.',
        '.#.#####.##.',
        '............',
    ]
    expected_grid_2 = [
        '............',
        '.#.LL.LL.L#.',
        '.#LLLLLL.LL.',
        '.L.L.L..L...',
        '.LLLL.LL.LL.',
        '.L.LL.LL.LL.',
        '.L.LLLLL.LL.',
        '...L.L......',
        '.LLLLLLLLL#.',
        '.#.LLLLLL.L.',
        '.#.LLLLL.L#.',
        '............',
    ]
    expected_grid_3 = [
        '............',
        '.#.L#.##.L#.',
        '.#L#####.LL.',
        '.L.#.#..#...',
        '.##L#.##.##.',
        '.#.##.#L.##.',
        '.#.#####.#L.',
        '...#.#......',
        '.LLL####LL#.',
        '.#.L#####.L.',
        '.#.L####.L#.',
        '............',
    ]

    data = [line for line in input_data.splitlines()]
    grid = ["." + line + "." for line in data]
    grid = ['.' * (len(data[0]) + 2)] + grid + ['.' * (len(data[0]) + 2)]

    grid_1 = calc_grid2(grid)
    assert grid_1 == expected_grid_1

    grid_2 = calc_grid2(grid_1)
    assert grid_2 == expected_grid_2

    grid_3 = calc_grid2(grid_2)
    assert grid_3 == expected_grid_3


def test_part_two():
    input_data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    data = [line for line in input_data.splitlines()]
    assert count2(data) == 26
