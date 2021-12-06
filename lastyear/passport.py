from re import fullmatch 

def year(min, max):
    def check(num):
        try:
            a = int(num)
            return a >= min and a <= max
        except:
            return False
    return check

def height(s):
    print(f"Checking height {s} {s[-2:]}")
    try:
        if s[-2:] == 'cm':
            return int(s[:-2]) >= 150 and int(s[:-2]) <= 193
        elif s[-2:] == 'in':
            return int(s[:-2]) >= 59 and int(s[:-2]) <= 76
    except:
        return False

def is_valid(passport):
    keys = {
        'byr': year(1920, 2002), 
        'iyr': year(2010, 2020), 
        'eyr': year(2020, 2030),
        'hgt': height,
        'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 
        'hcl': lambda x: fullmatch('#[0-9a-f]{6}', x), 
        'pid': lambda x: fullmatch('[0-9]{9}', x)
    }
    for tok in passport.split():
        parts = tok.split(':')
        if parts[0] in keys:
            if keys[parts[0]](parts[1]):
                del keys[parts[0]]
            else:
                print(f"INVALID {tok} {parts[1]} {parts[0]}")
                return False
    return len(keys) == 0

with open(f"data/dayold4.txt") as f:
    data = f.read().split("\n\n")
    ret = 0
    for passport in data:
        if is_valid(passport):
            ret += 1
    print(f"Valid passports: {ret} of {len(data)}")