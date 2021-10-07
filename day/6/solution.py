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
        group_questions = {""}
        total = 0
        while True:
            line = openfile.readline()
            if not line or line == "\n":
                if group_questions == {""}:
                    break
                else:
                    # print(group_questions)
                    if "" in group_questions:
                        group_questions.remove("")
                    total += len(group_questions)
                group_questions = {""}
            else:
                if group_questions == {""}:
                    group_questions.update(set(line.strip()))
                else:
                    group_questions = group_questions.intersection(set(line.strip()))
        return total

if __name__ == "__main__":
    print(part1(INPUT))
    print(part2(INPUT))
