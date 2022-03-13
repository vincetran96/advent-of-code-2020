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

def part1(input: str) -> tuple:
    conditions = {} # Dict of conditions names and conditions values
    conditions_order = {} # Dict of correct order of conditions in each ticket line
    valid_tickets = [] # List of valid ticket values
    nearby = False
    your = False
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

            # Lines with "your" ticket info
            if "your" in line and your is False:
                your = True
            if your and "," in line:
                your_ticket_values = [int(n) for n in line.strip().split(",")]
            
            # Lines with nearby tickets info
            if "nearby" in line and nearby is False:
                nearby = True
                your = False
            if nearby and "," in line:    
                ticket_values = [int(n) for n in line.strip().split(",")]
                isValid_ticket = True # Validity of the ticket
                for ticket_value in ticket_values:
                    isValid_value = False
                    for ck, cv in conditions.items():
                        if check_condition(ticket_value, cv):
                            isValid_value = True
                            
                            # # Append condition name to cond. list if not in
                            # if ck not in conditions_list:
                            #     conditions_list.append(ck)
                            
                            # # Skip checking altogether if cond. list is full
                            # if len(conditions_list) == len(conditions.keys()):
                            #     break
                            
                            break
                    # If one ticket value is invalid, the ticket is invalid
                    if isValid_value is False:
                        result += ticket_value
                        isValid_ticket = False
                if isValid_ticket is True:
                    valid_tickets.append(ticket_values)
                # something is wrong with the valid tickets list


        
        # Part 2?
        unchecked_idx = sorted(list(range(len(conditions.keys()))))
        print(unchecked_idx)
        for ck, cv in conditions.items():
            print(f"Checking condition {ck}")
            for idx in unchecked_idx:
                isCorrect_idx = True
                for ticket_values in valid_tickets:
                    if check_condition(ticket_values[idx], cv) is False:
                        isCorrect_idx = False
                        break
                if isCorrect_idx is True:
                    print(f">> Index {idx} is correct for condition {ck}")
                    conditions_order[ck] = idx
                    unchecked_idx.remove(idx) # Not sure if this list is updated within for loop
                    break
            print(f">> {unchecked_idx}")


                    
    return result, conditions_order


if __name__ == "__main__":
    print(part1(INPUT_TEST))
    # print(part1(INPUT))
    # print(check_condition(35, (30, 260, 284, 950)))