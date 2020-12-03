import pytest
from src.day3 import count_trees


# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2
@pytest.mark.parametrize(
    "offset_x, offset_y, validate_tree_count", [
        (1, 1, 2),
        (3, 1, 7),
        (5, 1, 3),
        (7, 1, 4),
        (1, 2, 2),
    ]
)
def test_count_trees_with_example_data(offset_x, offset_y, validate_tree_count):
    terrain = [
        '..##.......',
        '#...#...#..',
        '.#....#..#.',
        '..#.#...#.#',
        '.#...##..#.',
        '..#.##.....',
        '.#.#.#....#',
        '.#........#',
        '#.##...#...',
        '#...##....#',
        '.#..#...#.#',
    ]
    assert count_trees(terrain, offset_x, offset_y) == validate_tree_count


def test_count_trees_with_clear_path():
    terrain = [
        '.###',
        '###.',
    ]
    assert count_trees(terrain, 3, 1) == 0


def test_count_trees_with_skipping_lines():
    terrain = [
        '.#########',
        '##########',
        '#.########',
        '##########',
        '##.#######',
        '##########',
    ]
    assert count_trees(terrain, 1, 2) == 0
