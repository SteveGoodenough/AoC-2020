import pytest
from src.day15 import count


@pytest.mark.parametrize(
    "input_data, validate_count", [
        ("0,3,6", 436),
        ("1,3,2", 1),
        ("2,1,3", 10),
        ("2,3,1", 78),
        ("3,2,1", 438),
        ("3,1,2", 1836),
    ]
)
def test_part_one(input_data, validate_count):
    data = [int(line) for line in input_data.split(',')]
    assert count(data, 2020) == validate_count


@pytest.mark.parametrize(
    "input_data, validate_count", [
        ('0,3,6', 175594),
        ('1,3,2', 2578),
        ('2,1,3', 3544142),
        ('1,2,3', 261214),
        ('2,3,1', 6895259),
        ('3,2,1', 18),
        ('3,1,2', 362),
    ]
)
def test_part_two(input_data, validate_count):
    data = [int(line) for line in input_data.split(',')]
    assert count(data, 30000000) == validate_count
