INPUT = "day/3/input"

def check_tree(chr: str) -> bool:
    '''Checks if `c` is a tree
    '''
    return chr == "#"

def part1(input: str, right: int, down: int) -> int:
    '''Not counting the left most corner?
    '''
    count = 0
    with open(input, "r") as openfile:
        c = 0 # cursor
        down_counter = 0
        for i, line in enumerate(openfile.readlines()):
            line = line.strip()
            if down_counter > 0:
                down_counter -= 1
                continue
            else:
                down_counter = down - 1
            if i > 0: # only check tree for rows > 1
                if check_tree(line[c]):
                    count += 1
            c = c + right
            if c >= len(line):
                c = c % len(line)
        return count

def part2(input: str):
    return (
        part1(INPUT, 1, 1) * \
        part1(INPUT, 3, 1) * \
        part1(INPUT, 5, 1) * \
        part1(INPUT, 7, 1) * \
        part1(INPUT, 1, 2)
    )

if __name__ == "__main__":
    # print(part1(INPUT, 3, 1))
    print(part1(INPUT, 1, 2))
    print(part2(INPUT))
