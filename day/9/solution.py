from typing import Iterable


INPUT = "day/9/input"

def findTwoSum(numbers: Iterable[int], s: int) -> bool:
    '''Finds if two elements in `numbers` sum up to `s`
    '''
    for n in numbers:
        n_other = s - n
        if n_other in numbers and n_other != n:
            return True
    return False

def part1(input: str, preamble_len: int = 5):
    preambles = []
    with open(input, "r") as openfile:
        for _ in range(preamble_len):
            preambles.append(int(openfile.readline().strip()))
        while True:
            next_ = openfile.readline().strip()
            if next_:
                next_ = int(next_)
                check = findTwoSum(preambles, next_)
                if not check:
                    return next_
                preambles.pop(0)
                preambles.append(next_)

def part2(input: str, preamble_len: int = 5):
    target = part1(input, preamble_len)
    if target:
        with open(input, "r") as openfile:
            while True:
                line = openfile.readline().strip()
                if not line:
                    break
                candidates = [int(line)]
                current_start = openfile.tell()
                while True:
                    next_ = int(openfile.readline().strip())
                    candidates.append(next_)
                    sm = sum(candidates)
                    if sm == target:
                        return max(candidates) + min(candidates)
                    elif sm > target:
                        openfile.seek(current_start)
                        break
                

if __name__ == "__main__":
    # print(part1(INPUT, 25))
    print(part2(INPUT, 25))
