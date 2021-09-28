from typing import Union


S = 2020
INPUT = "day/1/input"

def findTwo(numbers: set, s: int) -> Union[int, None]:
    for n in numbers:
        n_other = s - n
        if n_other in numbers:
            return n * n_other
    return None

def part1():
    with open(INPUT, "r") as openfile:
        numbers = set(int(line.strip("\n")) for line in openfile.readlines())
        return findTwo(numbers, S)

def part2():
    with open(INPUT, "r") as openfile:
        numbers = sorted(int(line.strip("\n")) for line in openfile.readlines())
        for i, n in enumerate(numbers):
            S_other = S - n
            found = findTwo(set(numbers[i+1:]), S_other)
            if found:
                return n * found
        return None



if __name__ == "__main__":
    print(part1())
    print(part2())
