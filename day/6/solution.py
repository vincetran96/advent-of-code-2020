INPUT = "day/6/input"

def part1(input: str) -> int:
    with open(input, "r") as openfile:
        group_questions = set()
        total = 0
        while True:
            line = openfile.readline()
            if not line or line == "\n":
                if not group_questions:
                    break
                else:
                    total += len(group_questions)
                group_questions = set()
            else:
                group_questions.update(set(line.strip()))
        return total

def part2(input: str) -> int:
    with open(input, "r") as openfile:
        group_questions = set()
        total = 0
        g = 0
        while True:
            line = openfile.readline()
            if not line or line == "\n":
                if not group_questions:
                    break
                else:
                    print(f'group {g}')
                    # print(group_questions)
                    total += len(group_questions)
                group_questions = set()
                g += 1
            else:
                if not group_questions:
                    print(group_questions)
                    group_questions.update(set(line.strip()))
                else:
                    print(group_questions.intersection(set(line.strip())))
                    group_questions = group_questions.intersection(set(line.strip()))
        return total

if __name__ == "__main__":
    # print(part1(INPUT))
    print(part2(INPUT))
