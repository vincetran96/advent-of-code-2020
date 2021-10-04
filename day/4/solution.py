

INPUT = "day/4/input"
REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def check_byr(byr: str) -> bool:
    '''Checks byr
    '''
    ibyr = int(byr)
    return (len(byr) == 4 and ibyr >= 1920 and ibyr <= 2002)

def check_iyr(iyr: str) -> bool:
    '''Checks iyr
    '''
    iiyr = int(iyr)
    return (len(iyr) == 4 and iiyr >= 2010 and iiyr <= 2020)

def check_eyr(eyr: str) -> bool:
    '''Checks eyr
    '''
    ieyr = int(eyr)
    return (len(eyr) == 4 and ieyr >= 2020 and ieyr <= 2030)

def check_hgt(hgt: str) -> bool:
    '''Checks hgt
    '''
    if "cm" in hgt:
        h_cm = int(hgt[:hgt.find("cm")])
        return h_cm >= 150 and h_cm <= 193
    elif "in" in hgt:
        h_in = int(hgt[:hgt.find("in")])
        return h_in >= 59 and h_in <= 76
    return False

def check_hcl(hcl: str) -> bool:
    '''Checks hcl
    '''
    legit = "abcdef0123456789"
    ret = True
    if "#" not in hcl:
        ret = False
    else:
        code = hcl[hcl.find("#")+1:]
        ret = all((chr in legit) for chr in code)
    return ret

def check_ecl(ecl: str) -> bool:
    '''Checks ecl
    '''
    legit = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return ecl in legit

def check_pid(pid: str) -> bool:
    '''Checks pid
    '''
    return len(pid) == 9 and all(str.isdigit(d) for d in pid)

def check_requirements(splitted: list, part: int) -> bool:
    '''
        `part`: 1 or 2
    '''
    checked_bools = set() # list of bools
    fields = set()
    for kv in splitted:
        if kv:
            key = kv[:kv.find(":")]
            value = kv[kv.find(":")+1:]
            fields.add(key)
            if part == 2:
                if key == "byr":
                    checked_bools.add(check_byr(value))
                elif key == "iyr":
                    checked_bools.add(check_iyr(value))
                elif key == "eyr":
                    checked_bools.add(check_eyr(value))
                elif key == "hgt":
                    checked_bools.add(check_hgt(value))
                elif key == "hcl":
                    checked_bools.add(check_hcl(value))
                elif key == "ecl":
                    checked_bools.add(check_ecl(value))
                elif key == "pid":
                    checked_bools.add(check_pid(value))
    checked_bools.add(REQUIRED_FIELDS.issubset(fields))
    return all(checked_bools)


def part1(input: str) -> int:
    with open(input, "r") as openfile:
        person_line = ""
        good = 0
        while True:
            line = openfile.readline()
            if not line or line == "\n":
                if person_line == "":
                    break
                else:
                    splitted = person_line.split(" ")
                    fields = set()
                    for kv in splitted:
                        if kv:
                            fields.add(kv[:kv.find(":")])
                    if REQUIRED_FIELDS.issubset(fields):
                        good += 1
                        print("GOOD: ")
                        print(fields)
                    else:
                        print("BAD: ")
                        print(REQUIRED_FIELDS.difference(fields))
                    person_line = ""
            else:
                person_line = person_line + " " + line.strip()
        return good

def solve(input: str, part: int) -> int:
    with open(input, "r") as openfile:
        person_line = ""
        good = 0
        while True:
            line = openfile.readline()
            if not line or line == "\n":
                if person_line == "":
                    break
                else:
                    splitted = person_line.split(" ")
                    if check_requirements(splitted, part):
                        good += 1
                person_line = ""
            else:
                person_line = person_line + " " + line.strip()
        return good

if __name__ == "__main__":
    print(part1(INPUT))
    print(check_hcl("#123abc"))
    print(check_hcl("#123abz"))
    print(check_hcl("123abc"))
    print(check_pid("000000001"))
    print(check_pid("0123456789"))
    print(solve(INPUT, 2))
