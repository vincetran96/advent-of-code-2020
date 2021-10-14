# Part 1

## Challenges:
- Refrain from reading the whole input
- Go back some lines (going forward is trivial)
- Stop when a command line has already been processed

## High-level process (see `part1_1`):
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
- Key point of my solution is: **jump forward line-by-line, while jump backward instantly**; simply because reading new lines must be done by every line, while jumping back can be done by seeking
- My current solution is not elegant