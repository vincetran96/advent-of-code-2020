from typing import Iterable, Union


S = 2020
INPUT = "day/1/input"

def findTwo(numbers: Iterable, s: int) -> Union[int, None]:
    for n in numbers:
        n_other = s - n
        if n_other in numbers:
            return n * n_other
    return None

def part1(input: str):
    with open(input, "r") as openfile:
        numbers = set(int(line.strip("\n")) for line in openfile.readlines())
        return findTwo(numbers, S)

def part2(input: str):
    with open(input, "r") as openfile:
        numbers = sorted(int(line.strip("\n")) for line in openfile.readlines())
        for i, n in enumerate(numbers):
            S_other = S - n
            found = findTwo(numbers[i+1:], S_other)
            if found:
                return n * found
        return None


if __name__ == "__main__":
    print(part1(INPUT))
    print(part2(INPUT))
