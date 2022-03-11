INPUT = "day/16/input"
INPUT_TEST = "day/16/input_test"

def check_condition(
        input: int,
        cond: tuple[int]
    ) -> bool:
    '''Checks whether the input satisfy the field condition
    '''
    
    if len(cond) != 4:
        raise ValueError("Length of condition must be 4")
    return (input >= cond[0] and input <= cond[1]) \
            or (input >= cond[2] and input <= cond[3])

def part1(input: str) -> int:
    conditions = {}
    nearby = False
    result = 0
    with open(input, "r") as openfile:
        while True:
            line = openfile.readline()
            if not line:
                break
            
            # Lines with fields info
            if ": " in line:
                condition = ()
                field, conditions_raw = line.strip().split(": ")
                left_right = conditions_raw.split(" or ")
                for e in left_right:
                    for value in e.split("-"):
                        condition = condition + (int(value), )
                conditions[field] = condition
            
            # Lines with nearby tickets info
            if "nearby" in line and nearby is False:
                nearby = True
            if nearby and "," in line:    
                ticket_values = [int(n) for n in line.strip().split(",")]
                for ticket_value in ticket_values:
                    valid = False
                    for condition in conditions.values():
                        if check_condition(ticket_value, condition):
                            valid = True
                            break
                    if valid is False:
                        result += ticket_value
    return result


if __name__ == "__main__":
    print(part1(INPUT))
    # print(check_condition(35, (30, 260, 284, 950)))