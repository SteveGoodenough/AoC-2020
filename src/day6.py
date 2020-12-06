def main():
    with open("data/day6.txt", "r") as f:
        data = f.read().split('\n\n')
    
    print(count1(data))
    print(count2(data))
    # print(count2(data))


# 6387
def count1(data):
    total = 0
    for d in data:
        total += len(set(list(d.replace('\n',''))))
    return total


# 3039
def count2(data):
    total = 0
    for groups in data:
        people = [set(list(group)) for group in groups.split('\n')]
        for person in people[1:]:
            people[0].intersection_update(person)
        total += len(people[0])
    return total


if __name__ == "__main__":
    main()
