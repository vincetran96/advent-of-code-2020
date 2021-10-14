INPUT = "day/8/input"

def part1(input: str) -> int:
    with open(input, "r") as openfile:
        total = 0
        read_lines = []
        run_lines = set()
        line_cursor = 0
        op = ""
        jmp_arg = 0
        while True:
            line = openfile.readline()

            if not line and jmp_arg == 0:
                break

            line_end = openfile.tell()
            if line_end in run_lines and jmp_arg == 0:
                break
            if line_end not in read_lines:
                read_lines.append(line_end)
            line_cursor = read_lines.index(line_end)
            
            if op == "jmp" and jmp_arg != 0:
                if jmp_arg > 0:
                    jmp_arg -= 1
                else:
                    line_cursor = line_cursor + jmp_arg - 1
                    openfile.seek(read_lines[line_cursor])
                    jmp_arg = 0
            else:
                op, arg = line.split(" ")
                if op == "jmp":
                    jmp_arg = int(arg) - 1
                    run_lines.add(line_end)
                elif op == "acc":
                    total += int(arg)
                    run_lines.add(line_end)
        return total

def part1_1(input: str) -> int:
    '''A slightly different take on the solution to part 1;
    Hopefully to be more understandable
    '''
    with open(input, "r") as openfile:
        total = 0
        read_lines = []
        run_lines = set()
        line_cursor = 0
        op = ""
        jmp_arg = 0
        while True:
            line = openfile.readline()

            # Loop break conditions
            if not line:
                break

            line_end = openfile.tell()
            if line_end in run_lines and jmp_arg == 0:
                break
            if line_end not in read_lines:
                read_lines.append(line_end)
            line_cursor = read_lines.index(line_end)
            
            if op == "jmp" and jmp_arg > 0:
                jmp_arg -= 1
            else:
                op, arg = line.split(" ")
                if op == "jmp":
                    jmp_arg = int(arg)
                    if int(arg) > 0:
                        jmp_arg = jmp_arg - 1
                    elif int(arg) < 0:
                        line_cursor = line_cursor + jmp_arg - 1
                        openfile.seek(read_lines[line_cursor])
                        jmp_arg = 0
                    run_lines.add(line_end)
                elif op == "acc":
                    total += int(arg)
                    run_lines.add(line_end)
        return total

def part2(input: str):
    with open(input, "r") as openfile:
        total = 0
        read_lines = []
        run_lines = set()
        run_lines_order = []
        line_cursor = 0
        op = ""
        jmp_arg = 0
        while True:
            line = openfile.readline().strip()
            line_end = openfile.tell() # move this up here for end-of-file

            # Loop break conditions
            if not line:
                read_lines.append(line_end)
                break

            if line_end in run_lines and jmp_arg == 0:
                break
            if line_end not in read_lines:
                read_lines.append(line_end)
            line_cursor = read_lines.index(line_end)
            
            if op == "jmp" and jmp_arg > 0:
                jmp_arg -= 1
            else:
                op, arg = line.split(" ")
                if op == "jmp":
                    jmp_arg = int(arg)
                    if int(arg) > 0:
                        jmp_arg = jmp_arg - 1
                    elif int(arg) < 0:
                        line_cursor = line_cursor + jmp_arg - 1
                        openfile.seek(read_lines[line_cursor])
                        jmp_arg = 0
                elif op == "acc":
                    total += int(arg)
                # if line_end not in run_lines:
                run_lines_order.append(((op, arg), line_end))
                run_lines.add(line_end)
        
        return total, run_lines_order, read_lines, read_lines.index(run_lines_order[-1][1])
    
if __name__ == "__main__":
    # print(part1_1(INPUT))
    # print(part1(INPUT))
    print(part2(INPUT))
