def main():
    with open("data/day3.txt", "r") as f:
        terrain = f.read().splitlines()

    # 265
    print(count_trees(terrain, 3, 1))

    # 3154761400
    print(
        count_trees(terrain, 1, 1) *
        count_trees(terrain, 3, 1) *
        count_trees(terrain, 5, 1) *
        count_trees(terrain, 7, 1) *
        count_trees(terrain, 1, 2)
    )


def count_trees(terrain, offset_x, offset_y):
    width = len(terrain[0])
    trees = 0
    x = 1
    for y, line in enumerate(terrain):
        if y % offset_y:
            continue
        trees += line[x - 1] == "#"
        x += offset_x
        if x > width:
            x = x % width
    return trees


if __name__ == "__main__":
    main()
