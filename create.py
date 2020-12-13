# flake8: noqa
import sys
import os

src_base = """from time import time


def main():
    with open("data/day{day}.txt", "r") as f:
        data = f.read().splitlines()
        # data = [line.split() for line in f.readlines()]
        # data = f.read().split('\\n\\n')
        # data = [int(line) for line in f]

    time_start = time()
    print(count1(data))
    time_part1 = time()

    print(count2(data))
    time_part2 = time()

    print(f'Part one time: {1000*(time_part1-time_start):.0f}ms')
    print(f'Part two time: {1000*(time_part2-time_part1):.0f}ms')


# 
def count1(data):
    total = 0
    return total


# 
def count2(data):
    total = 0
    return total


if __name__ == "__main__":
    main()
"""

test_base = """import pytest
from src.day{day} import count1, count2


def test_part_one():
    input_data = '''
'''
    data = [line for line in input_data.splitlines()]
    # data = [int(line) for line in input_data.splitlines()]
    # data = [line.split() for line in input_data.split('\\n')]
    print(data)

    assert count1(data) == 0


# def test_part_two():
#     input_data = '''
# '''
#     data = [int(line) for line in input_data.splitlines()]
# 
#     assert count2(data) == 0
"""

def main():
    if len(sys.argv) > 1:
        day = int(sys.argv[1])
        print(f'Create day {day} files...')
        create_file(day, f'src/day{day}.py', src_base)
        create_file(day, f'tests/test_day{day}.py', test_base)
        create_file(day, f'data/day{day}.txt', '')


def create_file(day, src_path, template):
    print(f'Create {src_path}...')
    if not os.path.exists(src_path):
        with open(src_path, "w") as f:
            f.write(template.replace('{day}', str(day)).replace("'''", '"""'))
    else:
        print('Already exists, not overwriting')


if __name__ == "__main__":
    main()
