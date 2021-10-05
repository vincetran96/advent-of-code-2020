from typing import Iterable

INPUT = "day/5/input"

def get_middle(lower: int, upper: int) -> int:
    '''Gets middle number between lower and upper
    
    Assuming the number of numbers in the range (inclusive)
    is even
    '''
    return lower + int((upper - lower) / 2)

def get_binary_row(s: str, lower: int = 0, upper: int = 127) -> int:
    '''Returns the row number based on the binary space partitioning code
    '''
    if s == "F":
        return lower
    elif s == "B":
        return upper
    else:
        if s[0] == "F":
            return get_binary_row(s[1:], lower, get_middle(lower, upper))
        elif s[0] == "B":
            return get_binary_row(s[1:], get_middle(lower, upper) + 1, upper)

def get_binary_col(s: str, lower: int = 0, upper: int = 7) -> int:
    '''Returns the column number based on the binary space partitioning code
    '''
    if s == "L":
        return lower
    elif s == "R":
        return upper
    else:
        if s[0] == "L":
            return get_binary_col(s[1:], lower, get_middle(lower, upper))
        elif s[0] == "R":
            return get_binary_col(s[1:], get_middle(lower, upper) + 1, upper)

def get_seat_id(line: str) -> int:
    '''Returns seat id from `line`
    '''
    line = line.strip()
    row_code = line[:7]
    col_code = line[7:]
    row = get_binary_row(row_code)
    col = get_binary_col(col_code)
    seat_id = row * 8 + col
    return seat_id

def find_missing_id(ids: Iterable):
    '''Finds missing id from set of (consecutive) ids
    '''
    ids_sorted = sorted(ids)
    lower, upper = ids_sorted[0], ids_sorted[-1]
    return set(range(lower, upper + 1)).difference(ids)

def part1(input: str):
    max_seat_id = 0
    with open(input, "r") as openfile:
        for line in openfile.readlines():
            seat_id = get_seat_id(line)
            if seat_id > max_seat_id:
                max_seat_id = seat_id
        return max_seat_id

def part2(input: str):
    seat_ids = set()
    with open(input, "r") as openfile:
        for line in openfile.readlines():
            seat_id = get_seat_id(line)
            seat_ids.add(seat_id)
        missing_id = find_missing_id(seat_ids)
        return missing_id

if __name__ == "__main__":
    print(get_binary_row("FBFBBFF"))
    print(get_binary_col("RLR"))
    print(part1(INPUT))
    print(find_missing_id([10,11,13,14,15,16,17,18,20]))
    print(part2(INPUT))