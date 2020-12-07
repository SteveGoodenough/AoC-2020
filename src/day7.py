def main():
    with open("data/day7.txt", "r") as f:
        data = [line.split() for line in f.readlines()]

    print(count1(data))
    print(count2(data))


# 370
def count1(data):
    rules = {}
    for line in data:
        parent = line[0] + line[1]
        children = []
        if line[4] != 'no':
            i = 4
            while i < len(line):
                child = line[i + 1] + line[i + 2]
                children.append(child)
                i += 4
        rules[parent]=children
    return (len(set(count(rules, 'shinygold'))))


def count(rules, col):
    result = []
    for k, v in rules.items():
        if col in v:
            result.append(k)
            result = result + count(rules, k)
    return result


# 29547
def count2(data):
    rules = {}
    for line in data:
        parent = line[0] + line[1]
        children = []
        if line[4] != 'no':
            i = 4
            while i < len(line):
                child = line[i + 1] + line[i + 2]
                children.append((int(line[i]),child))
                i += 4
        rules[parent]=children
    return number_of_bags('shinygold', rules) - 1


def number_of_bags(colour, rules):
    return 1 + sum(count * number_of_bags(child_colour, rules) for count, child_colour in rules[colour])


if __name__ == "__main__":
    main()
