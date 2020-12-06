def main():
    with open("data/day6.txt", "r") as f:
        data = f.read().split('\n\n')

    print(count1(data))
    print(count2(data))


# 6387
def count1(data):
    return sum(len(set(d.replace('\n', ''))) for d in data)


# 3039
def count2(data):
    total = 0
    for groups in data:
        people = [set(list(group)) for group in groups.split('\n')]
        total += len(people[0].intersection(*people))
    return total


if __name__ == "__main__":
    main()
