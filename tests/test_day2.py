import pytest
from src.day2 import count1, count2

@pytest.mark.parametrize(
    "data, validate_count", [
        (['1-3 a: abcde'], 1),
        (['1-3 b: cdefg'], 0),
        (['2-9 c: ccccccccc'], 1),
        ([
            '1-3 a: abcde',
            '1-3 b: cdefg',
            '2-9 c: ccccccccc'], 2),
    ]
)
def test_count1_with_test_data(data, validate_count):
    assert count1(data) == validate_count


@pytest.mark.parametrize(
    "data, validate_count", [
        (['1-3 a: abcde'], 1),
        (['1-3 b: cdefg'], 0),
        (['2-9 c: ccccccccc'], 0),
        ([
            '1-3 a: abcde',
            '1-3 b: cdefg',
            '2-9 c: ccccccccc'], 1),
    ]
)
def test_count2_with_test_data(data, validate_count):
    assert count2(data) == validate_count
