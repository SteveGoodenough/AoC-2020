def main():
    with open("data/day5.txt", "r") as f:
        data = f.read().splitlines()

    print(count1(data))
    print(count2(data))


def calc_id(ticket):
    return int(ticket.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), 2)


# 908
def count1(data):
    return max(sorted([calc_id(ticket) for ticket in data]))


# 619
def count2(data):
    tickets = sorted([calc_id(ticket) for ticket in data])
    id_check = tickets[0]
    for id in tickets:
        if id != id_check:
            return id_check
        id_check += 1


if __name__ == "__main__":
    main()
