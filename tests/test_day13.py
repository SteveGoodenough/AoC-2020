import pytest
from src.day13 import count1, count2


def test_part_one():
    input_data = """939
7,13,x,x,59,x,31,19"""
    data = [line for line in input_data.splitlines()]
    assert count1(data) == 295


def test_part_two():
    input_data = """111
17,x,13,19"""

    data = [line for line in input_data.splitlines()]
    assert count2(data) == 3417
