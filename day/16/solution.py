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

def solution(input: str) -> tuple:
    conditions = {} # Dict of conditions names and conditions values
    conditions_order = {} # Dict of correct order of conditions in each ticket line
    valid_tickets = [] # List of valid ticket values
    nearby = False
    your = False
    result_part1 = 0
    result_part2 = 1
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
                        result_part1 += ticket_value
                        isValid_ticket = False
                if isValid_ticket is True:
                    valid_tickets.append(ticket_values)
                # something is wrong with the valid tickets list


        
        # Part 2?
        unchecked_idx = sorted(list(range(len(conditions.keys()))))
        for ck, cv in conditions.items():
            conditions_order[ck] = set()
            print(f"Checking condition {ck}")
            for idx in unchecked_idx:
                isCorrect_idx = True
                for ticket_values in valid_tickets:
                    if check_condition(ticket_values[idx], cv) is False:
                        isCorrect_idx = False
                        break
                if isCorrect_idx is True:
                    print(f">> Index {idx} is correct for condition {ck}")
                    conditions_order[ck].add(idx)
                    
                    # unchecked_idx.remove(idx) # Not sure if this list is updated within for loop
                    # break
            # print(f">> {unchecked_idx}")
        
        # Condition names with column indexes that satisfy it
        sorted_conditions_keys = sorted(conditions_order.items(), key=lambda x: len(x[1]))
        for i, e in enumerate(sorted_conditions_keys):
            if len(e[1]) == 1:
                conditions_order[e[0]] = e[1].pop()
            else:
                conditions_order[e[0]] = \
                    e[1].difference(sorted_conditions_keys[i-1][1]).pop()

        # Now look into your ticket
        for ck, cv in conditions_order.items():
            if ck.find("departure") == 0:
                result_part2 *= your_ticket_values[cv]


                    
    return result_part1, result_part2


if __name__ == "__main__":
    # print(solution(INPUT_TEST))
    print(solution(INPUT))
    # print(check_condition(35, (30, 260, 284, 950)))