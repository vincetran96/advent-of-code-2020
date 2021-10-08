INPUT = "day/8/input"

def solve(input: str):
    with open(input, "r") as openfile:
        total = 0
        positions = []
        processed_positions = set()
        current_op = ""
        current_arg = 0
        line = openfile.readline()
        while True:
            # check line
            if current_arg == 0 and not line:
                print(">>>>> BREAK: empty line")
                break
            print(f"Seen {line}")
            
            # check position
            position = openfile.tell()
            if position not in positions:
                print(f">>>> append position {position}")
                positions.append(position)
            elif current_arg == 0 and position in processed_positions:
                print(">>>>> break: position already processed")
                print(position, positions, processed_positions)
                break
            
            # check current op to jump lines if necessary
            if current_arg != 0 and current_op == "jmp":
                if current_arg > 0:
                    current_arg -= 1
                    print(f">>>>> jumping forward 1, remaining {current_arg}")
                elif current_arg < 0:
                    seek_position = position_cursor + current_arg - 1
                    print(
                        f">>>>> jumping back {current_arg} to position {positions[seek_position]}"
                    )
                    openfile.seek(positions[seek_position])
                    current_arg = 0
                line = openfile.readline() # should it be here?

            # this now only works for jumping forward
            # when going backward, the "current line" is not supposed to be processed
            if current_arg == 0 and line:
                # process the command
                op, arg = line.strip().split(" ")
                current_op = op
                if op == "jmp":
                    current_arg = int(arg)
                elif op == "acc":
                    total += int(arg)
                processed_positions.add(position)
                position_cursor = positions.index(position)
                print(f"cursor: {position_cursor}; positions list: {positions}")
                print(f">>>>> PROCESS {line}")

            # Line reading block
            # or should it be here?
            # line should always be read...
            # if current_arg == 0:
            #     line = openfile.readline()

        return total


if __name__ == "__main__":
    print(solve(INPUT))
