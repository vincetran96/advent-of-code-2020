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
            line_end = openfile.tell()
            line = openfile.readline()

            # Loop break conditions
            if not line:
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
                        line_cursor = line_cursor + jmp_arg
                        openfile.seek(read_lines[line_cursor])
                        jmp_arg = 0
                    run_lines.add(line_end)
                elif op == "acc":
                    total += int(arg)
                    run_lines.add(line_end)
        return total, read_lines

def part2(input: str):
    with open(input, "r") as openfile:
        total = 0
        read_lines = [] # ending locations of lines read
        run_lines = set()
        line_cursor = 0
        op = ""
        jmp_arg = 0
        nop_jmp_lines = [] # locations of `nop` and `jmp` lines
        nop_jmp_totals = [] # totals at each `nop` and `jmp` line
        nop_jmp_lock = False
        swapping = False # swap `nop` for `jmp` and vice versa
        line_swapped = ""
        
        while True:
            line_end = openfile.tell() # move this up here for end-of-file
            line = openfile.readline().strip()

            # Loop break conditions
            if not line:
                break

            if line_end in run_lines and jmp_arg == 0:
                if not swapping:
                    if nop_jmp_lines and nop_jmp_totals:
                        openfile.seek(nop_jmp_lines.pop())
                        total = nop_jmp_totals.pop()
                        swapping = True
                        nop_jmp_lock = nop_jmp_lock or True
                        continue # continue next loop, ignore all below
                    else:
                        print(">>>>> BREAK")
                        break
            
            if line_end not in read_lines:
                read_lines.append(line_end)
            line_cursor = read_lines.index(line_end)
            
            if op == "jmp" and jmp_arg > 0:
                jmp_arg -= 1
            else:
                op, arg = line.split(" ")
                if op == "acc":
                    total += int(arg)
                else: # either `nop` or `jmp`
                    if not nop_jmp_lock:
                        nop_jmp_lines.append(line_end)
                        nop_jmp_totals.append(total)
                    
                    if swapping:
                        op = "nop" if op == "jmp" else "jmp"
                        swapping = False
                        line_swapped = line
                    
                    if op == "jmp":
                        jmp_arg = int(arg)
                        if int(arg) > 0:
                            jmp_arg = jmp_arg - 1
                        elif int(arg) < 0:
                            line_cursor = line_cursor + jmp_arg
                            openfile.seek(read_lines[line_cursor])
                            jmp_arg = 0
                run_lines.add(line_end)
        
        return total, line_swapped
    
if __name__ == "__main__":
    # print(part1_1(INPUT))
    # print(part1(INPUT))
    print(part2(INPUT))
