# flake8: noqa
import sys
import os

src_base = """
def main():
    with open("data/day{day}.txt", "r") as f:
        data = f.read().split('\\n\\n')
    
    print(count1(data))
    print(count2(data))


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

test_base = """
import pytest
from src.day{day} import count1, count2


def test_part_one():
    pass


def test_part_two():
    pass
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
            f.write(template.replace('{day}', str(day)))
    else:
        print('Already exists, not overwriting')


if __name__ == "__main__":
    main()
