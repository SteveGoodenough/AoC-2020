
from src.day9 import count1, count2


def test_part_one():
    input_data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
    data = [int(line) for line in input_data.splitlines()]
    assert count1(data, 5) == 127


def test_part_two():
    input_data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
    data = [int(line) for line in input_data.splitlines()]
    assert count2(data, 5) == 62
