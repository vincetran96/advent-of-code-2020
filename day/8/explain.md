# Part 1

## Challenges:
- Refrain from reading the whole input
- Go back some lines (going forward is trivial)
- Stop when a command line has already been processed

## High-level process:
- Prepare (relevant stuff only):
    - List of lines read
    - Set of lines processed (no need for ordering so a set is good)
    - String of current operation
    - Int of current arg value
- Read first line
- For each line read (a `while` loop):
    - Get ending position of the line (`line position`)
    - Append the position in the list of read lines if not in
    - Check break condition:
        - If `line position` in set of lines processed, break
    - Check if current operation is `jump`
        - If `jump` forward:
            - Decrease current arg by 1
        - If `jump` backward:
            - Seek the file to the position of the line **before** the desired line (tricky part)
            - Set current arg to 0
        - Ignore everything else in the loop
    - Process the command

## Comments
- My current solution is not elegant