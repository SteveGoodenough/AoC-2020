
import pytest
from src.day10 import count1, count1alt, count2


def test_part_one():
    input_data = """16
10
15
5
1
11
7
19
6
12
4"""
    data = [int(line) for line in input_data.splitlines()]
    assert count1(data) == 35
    assert count1alt(data) == 35

def test_part_one1():
    input_data = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
    data = [int(line) for line in input_data.splitlines()]
    assert count1(data) == 220
    assert count1alt(data) == 220


def test_part_two():
    pass
