import pytest
from src.day6 import count1, count2


def test_day_total_part_one():
    forms= """abc

a
b
c

ab
ac

a
a
a
a

b"""
    data = forms.split('\n\n')
    assert count1(data) == 11


def test_day_total_part_two():
    forms= """abc

a
b
c

ab
ac

a
a
a
a

b"""
    data = forms.split('\n\n')
    assert count2(data) == 6
