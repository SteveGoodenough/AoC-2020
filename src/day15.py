from time import time


def main():
    with open("data/day15.txt", "r") as f:
        data = [int(v) for v in f.read().split(',')]

    time_start = time()
    print(count(data, 2020))
    time_part1 = time()

    print(count(data, 30000000))
    time_part2 = time()

    print(f'Part one time: {1000*(time_part1-time_start):.0f}ms')
    print(f'Part two time: {1000*(time_part2-time_part1):.0f}ms')


# 959
# ok for 2020 NOT for 30,000,000!
# def count1(data):
#     i = len(data)
#     for i in range(i, 2020):
#         v = data[i-1]
#         nv = -1
#         for b in range(i-2, -1, -1):
#             v2 = data[b]
#             if v == v2:
#                 nv = i - b - 1
#                 break
#         if nv == -1:
#             nv = 0
#         data.append(nv)
#     total = data[2019]
#     return total


# 959
# 116590
def count(data, iterations):
    iteration = len(data)
    num_last_used = {}
    for iteration, value in enumerate(data[:-1]):
        num_last_used[value] = iteration
    last_value = data[-1]

    for iteration in range(len(data), iterations):
        if last_value in num_last_used:
            new_value = iteration - num_last_used[last_value] - 1
            num_last_used[last_value] = iteration - 1
            last_value = new_value
        else:
            num_last_used[last_value] = iteration - 1
            last_value = 0
    return last_value


if __name__ == "__main__":
    main()
