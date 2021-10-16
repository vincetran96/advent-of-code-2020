# Part 1
## Challenges
- Refrain from reading the whole input
- Go back some lines (going forward is trivial)
- Stop when a command line has already been processed

## High-level process (see `part1_1`)
- Prepare (relevant stuff only):
    - List of `line ends` read
    - Set of lines run (no need for ordering so a set is good)
    - Int of line cursor (for going backward)
    - String of current operation
    - Int of `jump arg` value
- For each line read (a `while` loop):
    - Read the line
    - Loop break conditions:
        - The end of file: break
        - `Line end` already run and not `jumping`: break
        - Append `line end` to list of `line ends` read if not in
        - Update cursor according to `line end`
    - If `jumping` forward:
        - Simply decrease `jump arg` by 1
    - Else, process the command accordingly, including `jumping` backward
## Comments
- Key point of my solution is: **jump forward line-by-line, while jump backward instantly**; simply because reading new lines must be done by every line, while jumping back can be done by seeking the input file
- My current solution is not elegant

# Part 2
## Challenges
- Refrain from reading the whole input
- Go back some lines
- Redo by swapping `nop` for `jmp` operations when a loop occurs
## Some reasoning
- Either an `nop` or `jmp` must be "swapped" for the program to run completely from begin to end without entering an infinite loop
- Initially, there exists an infinite loop within the program, preventing it from terminating
- If the `nop` or `jmp` that must be swapped is located within the lines that are not executed in the "loop", the "loop" will just stay there
- Therefore, the `nop` or `jmp` that must be swapped **is located within the lines that are executed in the "loop"**
- To find which operation line to swap...
    - We create a list storing **all** the lines with `nop` or `jmp` operations within the first infinite "loop"
    - For each time we encounter a loop when running the program, we jump back to the last line in that list, swap operations, and restore the accumulator value
    - Keep running the program and repeating getting back to the last line until that list is empty
## High-level process (see `part2`)
- Prepare these, in addition to the things in part 1:
    - A list of locations of lines with `nop` or `jmp` operations `(1)`
    - A list of the values of the accumulator corresponding to each of the location of the above list `(2)`
    - A lock boolean variable indicating whether to continue adding locations to list `(1)`
    - A "swapping" boolean indicating if we are swapping operation
- For each line read:
    - Read the line
    - Check break conditions:
        - End of file
        - `Line_end` already run and not jumping:
            - If not swapping:
                - If list of lines to swap still available:
                    - Jump the file back to the last `nop` or `jmp` line
                - Else, break
    - If `jumping` forward:
        - Decrease `jump_arg` by 1
    - Else:
        - If the operation is either `nop` or `jmp`
            - If not `locked`, append the `line_end` and the current `accumulator` to the list `(1)` and `(2)`
            - If swapping, perform the swap
            - Then process the operation as part 1
