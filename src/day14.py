from time import time
from collections import defaultdict


def main():
    with open("data/day14.txt", "r") as f:
        data = f.read().splitlines()

    time_start = time()
    print(count1(data))
    time_part1 = time()

    print(count2(data))
    time_part2 = time()

    print(f'Part one time: {1000*(time_part1-time_start):.0f}ms')
    print(f'Part two time: {1000*(time_part2-time_part1):.0f}ms')


# 17028179706934
def count1(data):
    reg = defaultdict(int)
    mask = 0
    for line in data:
        if line[:4] == "mask":
            mask = line.split()[2]
        else:
            addr, value = line[4:].split("] = ")
            reg[addr] = bitmask(int(value), mask)
    return sum(int(v) for v in reg.values())


def bitmask(value, mask):
    binary_value = f'{value:b}'.zfill(36)
    mask_value = 0
    power_of_two = 1
    for i in range(35, -1, -1):
        if mask[i] == "1" or mask[i] == "X" and binary_value[i] == "1":
            mask_value += power_of_two
        power_of_two *= 2
    return mask_value


# 3683236147222
def count2(data):
    reg = defaultdict(int)
    mask = 0
    for line in data:
        if line[:4] == "mask":
            mask = line.split()[2]
        else:
            addr, value = line[4:].split("] = ")
            bitmask = addr_bitmask(int(addr), mask)
            burst = burst_values(bitmask)
            for addr in burst:
                reg[int(addr, 2)] = value
    return sum(int(v) for v in reg.values())


def addr_bitmask(value, mask):
    binary_value = f'{value:b}'.zfill(36)
    mask_value = ''
    for i in range(36):
        if mask[i] == "0":
            mask_value += binary_value[i]
        else:
            mask_value += mask[i]
    return mask_value


def burst_values(bitmask):
    bitmask_list = [bitmask]
    not_found = True
    while not_found:
        burst_list = []
        for item in bitmask_list:
            if (offset := item.find('X')) >= 0:
                burst_list.append(f'{item[:offset]}0{item[offset+1:]}')
                burst_list.append(f'{item[:offset]}1{item[offset+1:]}')
                not_found = False
            else:
                burst_list.append(item)
        if not_found:
            return burst_list
        bitmask_list = burst_list
        not_found = True


if __name__ == "__main__":
    main()
