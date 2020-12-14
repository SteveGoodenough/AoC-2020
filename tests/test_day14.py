from src.day14 import count1, count2


def test_part_one():
    input_data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    data = [line for line in input_data.splitlines()]
    assert count1(data) == 165


def test_part_two():
    input_data = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
    data = [line for line in input_data.splitlines()]
    assert count2(data) == 208
