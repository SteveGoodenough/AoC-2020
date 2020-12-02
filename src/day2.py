# import re

def main():
    with open("day2.txt", "r") as f:
        data = f.read().splitlines()

    print(count1(data))
    print(count2(data))


# 465
def count1(data):
    total = 0
    for line in data:
        # elements = line.replace('-',' ').split()
        # elements = re.split('-| ', line)
        # min = int(elements[0])
        # max = int(elements[1])
        # char = elements[2][:-1]
        # count = elements[3].count(char)
        # count = pw.count(char[0])
        # if int(min) <= count <= int(max):
        #     total += 1
        min, max, char, pw = line.replace('-', ' ').split()
        total += int(min) <= pw.count(char[0]) <= int(max)
    return total


# 294
def count2(data):
    total = 0
    for line in data:
        # elements = line.replace('-',' ').split()
        # elements = re.split('-| ', line)
        # pos1 = int(elements[0])-1
        # pos2 = int(elements[1])-1
        # char = elements[2][:-1]
        # if bool(elements[3][pos1] == char) != bool(elements[3][pos2] == char):
        #     total += 1
        pos1, pos2, char, pw = line.replace('-', ' ').split()
        total += bool(pw[int(pos1)-1] == char[0]) != bool(pw[int(pos2)-1] == char[0])
    return total


if __name__ == "__main__":
    main()
