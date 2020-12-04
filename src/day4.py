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
        return value.isdigit() and (1920 <= int(value) <= 2002)
    elif key == 'iyr':
        return value.isdigit() and 2010 <= int(value) <= 2020
    elif key == 'eyr':
        return value.isdigit() and 2020 <= int(value) <= 2030
    elif key == 'hgt':
        if value[-2:] == "cm":
            return value[:-2].isdigit() and 150 <= int(value[:-2]) <= 193
        elif value[-2:] == "in":
            return value[:-2].isdigit() and 59 <= int(value[:-2]) <= 76
    elif key == 'hcl':
        return value[:1] == "#" and len(value[1:]) == 6 and pattern.fullmatch(value[1:]) is not None
    elif key == 'ecl':
        return value in ('amb','blu','brn','gry','grn','hzl','oth')
    elif key == 'pid':
        return len(value) == 9 and value.isdigit()
    elif key == 'cid':
        return True


if __name__ == "__main__":
    main()
