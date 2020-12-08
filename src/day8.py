import copy


def main():
    with open("data/day8.txt", "r") as f:
        data = [line.split() for line in f.readlines()]

    print(count1(data))
    print(count2(data))


# 1684
def count1(data):
    accumulator = 0
    lines = set()
    current_line = 0
    max_lines = len(data)
    while True:
        if current_line in lines:
            return accumulator
        lines.add(current_line)
        operation = data[current_line][0]
        argument = int(data[current_line][1])
        if operation == "acc":
            accumulator += argument
        
        if operation == "jmp":
            current_line += argument
        else:
            current_line += 1

        if current_line == max_lines:
            return (0-accumulator)


# 2188
def count2(data):
    accumulator = 0
    lines = set()
    current_line = 0
    while True:
        if current_line in lines:
            return accumulator
        lines.add(current_line)
        operation = data[current_line][0]
        argument = int(data[current_line][1])
        if operation == "acc":
            accumulator += argument
            current_line += 1
        elif operation == "jmp":
            d = copy.deepcopy(data)
            d[current_line][0] = "nop"
            r = count1(d)
            if r < 0:
                return 0-r
            current_line += argument
        else:
            if argument != 0:
                d = copy.deepcopy(data)
                d[current_line][0] = "jmp"
                r = count1(d)
                if r < 0:
                    return 0-r
            current_line += 1


if __name__ == "__main__":
    main()
