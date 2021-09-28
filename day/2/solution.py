INPUT = "day/2/input"

def checkPart1(s: str, c: str, lower: int, upper: int) -> bool:
    '''Checks if `c` occurs within [`lower`, `upper`] times
        inside `s`
    '''
    count = 0
    for ch in s:
        if ch == c:
            count += 1
    return (count >= lower and count <= upper)

def checkPart2(s: str, c: str, lower: int, upper: int) -> bool:
    '''Checks if `c` occurs exclusively
        at `lower` OR `upper` positions inside `s`

        Note: no zero-index (e.g., index 1 means the start of `s`)
    '''
    lower_z = lower - 1
    upper_z = upper - 1
    return (s[lower_z] == c and s[upper_z] != c) \
        or (s[lower_z] != c and s[upper_z] == c)

def solve(input: str, part: int):
    '''Solves, depending on part
    '''
    
    count = 0
    with open(input, "r") as openfile:
        for line in openfile.readlines():
            policy, password = line.split(": ")
            lower_upper, chr = policy.split(" ")
            lower, upper = lower_upper.split("-")
            if part == 1:
                if checkPart1(password, chr, int(lower), int(upper)):
                    count += 1
            elif part == 2:
                if checkPart2(password, chr, int(lower), int(upper)):
                    count += 1
        return count

if __name__ == "__main__":
    print(solve(INPUT, 1))
    print(solve(INPUT, 2))
