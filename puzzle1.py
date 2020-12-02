from datetime import datetime
from itertools import combinations
from math import prod


def main():
    with open("puzzle1.txt", "r") as f:
        numbers = [int(line) for line in f]

    # 224436
    # print(find_two(numbers))
    # print(find_two_comp(numbers))

    # # 303394260
    # print(find_3(numbers))
    # print(find_3_comp(numbers))

    print(find_2020(numbers, 2))
    print(find_2020(numbers, 3))

    print(find_2020_comp(numbers, 2))
    print(find_2020_comp(numbers, 3))


def find_2020(numbers, number_to_check):
    for n in (combinations(set(numbers), number_to_check)):
        if sum(n) == 2020:
            return prod(n)


def find_2020_comp(numbers, number_to_check):
    return [prod(n) for n in combinations(set(numbers), number_to_check) if sum(n) == 2020]


# older variants

def find_two(numbers):
    for n1 in numbers:
        for n2 in numbers:
            if (n1 + n2) == 2020:
                print(n1, n2, n1 * n2)
                return


def find_two_comp(numbers):
    print([n1 * n2 for n1 in numbers for n2 in numbers if n1 + n2 == 2020])


def find_3(numbers):
    for n1 in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if (n1 + n2 + n3) == 2020:
                    print(n1, n2, n3, n1 * n2 * n3)
                    return


def find_3_comp(numbers):
    print([n1 * n2 * n3 for n1 in numbers for n2 in numbers for n3 in numbers if n1 + n2 + n3 == 2020])


if __name__ == "__main__":
    main()
