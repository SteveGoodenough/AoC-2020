import re

pattern = re.compile("[a-z0-9]+")


def main():
    with open("data/day4.txt", "r") as f:
        pa = f.read().splitlines()
    print(count1(pa))
    print(count2(pa))


# 192
def count1(pa):
    pa.append('')
    total = 0
    fields = 0
    cid = False
    for p in pa:
        if (p == ""):
            total += (fields == 8 or (fields == 7 and not cid))
            cid = False
            fields = 0
        else:
            fields += len(p.split())
            cid = cid or (p.find('cid:') > -1)
    return total


# 101
def count2(pa):
    pa.append('')
    total = 0
    num_fields = 0
    cid = False
    for p in pa:
        if (p == ""):
            total += (num_fields == 8 or (num_fields == 7 and not cid))
            cid = False
            num_fields = 0
        else:
            fields = p.split()
            for field in fields:
                num_fields += validate(field) is True
            cid = cid or (p.find('cid:') > -1)
    return total


def validate(field):
    key, value = field.split(":")
    if key == 'byr':
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        return value.isnumeric() and (1920 <= int(value) <= 2002)
    elif key == 'iyr':
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        return value.isnumeric() and 2010 <= int(value) <= 2020
    elif key == 'eyr':
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        return value.isnumeric() and 2020 <= int(value) <= 2030
    elif key == 'hgt':
        # hgt (Height) - a number followed by either cm or in:
        #  If cm, the number must be at least 150 and at most 193.
        #  If in, the number must be at least 59 and at most 76.
        if value[-2:] == "cm":
            return value[:-2].isnumeric() and 150 <= int(value[:-2]) <= 193
        elif value[-2:] == "in":
            return value[:-2].isnumeric() and 59 <= int(value[:-2]) <= 76
    elif key == 'hcl':
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        return value[:1] == "#" and len(value[1:]) == 6 and pattern.fullmatch(value[1:]) is not None
    elif key == 'ecl':
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        return f'|{value}|' in '|amb|blu|brn|gry|grn|hzl|oth|'
    elif key == 'pid':
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        return len(value) == 9 and value.isnumeric()
    elif key == 'cid':
        # cid (Country ID) - ignored, missing or not.
        return True


if __name__ == "__main__":
    main()
