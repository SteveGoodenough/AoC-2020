from src.day12 import count1, count2


def test_part_one():
    input_data = """F10
N3
F7
R90
F11"""
    data = [line for line in input_data.splitlines()]
    assert count1(data) == 25


def test_part_two():
    input_data = """F10
N3
F7
R90
F11"""
    data = [line for line in input_data.splitlines()]
    assert count2(data) == 286
