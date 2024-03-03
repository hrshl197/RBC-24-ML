def check_2_x_winning_condition(basket_stacks):
    cnt = 0
    for i, basket in enumerate(basket_stacks):
        if basket == ['x','x','x'] or  basket == ['x','o','x'] or basket == ['o','x','x']:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False

def check_1_x_winning_condition(basket_stacks):
    x_count = 0
    o_count = 0
    x_x_empty_count = 0
    xo_count = 0

    for basket in basket_stacks:
        if basket == ['x', 'x', 'x'] or basket == ['x', 'o', 'x'] or basket == ['o', 'x', 'x']:
            x_count += 1
        elif basket == ['x', 'x', '']:
            x_x_empty_count += 1
        elif basket == ['o', 'o', 'o'] or basket == ['o', 'x', 'o'] or basket == ['x', 'o', 'o']:
            o_count += 1
        elif basket == ['x', 'o', ''] or basket == ['o', 'x', '']:
            xo_count += 1

    if x_count == 1 and o_count <= 2 and x_x_empty_count <= 2 and xo_count == 0:
        return True
    else:
        return False

def evaluate_priority(basket):
    if one_x_mode_check or two_x_mode_check:
        if basket == ['', '', '']:
            return 3
        elif basket == ['o', '', '']:
            return 2
        elif basket == ['x', '', '']:
            return 1
        elif basket == ['o', 'x', '']:
            return 7
        elif basket == ['o', 'o', '']:
            return 4
        elif basket == ['x', 'o', '']:
            return 6
        elif basket == ['x', 'x', '']:
            return 5
        else:
            return 0  # Def_for_1_x
    else:
        if basket == ['', '', '']:
            return 3
        elif basket == ['o', '', '']:
            return 2
        elif basket == ['x', '', '']:
            return 1
        elif basket == ['o', 'x', '']:
            return 7
        elif basket == ['o', 'o', '']:
            return 5
        elif basket == ['x', 'o', '']:
            return 6
        elif basket == ['x', 'x', '']:
            return 4
        else:
            return 0  # Off


def apply_move(basket_stack):
    for i, ball in enumerate(basket_stack):
        if ball == '':
            basket_stack[i] = 'o'
            return


def select_move(basket_stacks):
    max_priority = 0
    selected_move = None
    arr=[]
    for i, basket in enumerate(basket_stacks):
        priority = evaluate_priority(basket)
        arr.append(priority)
        if priority > max_priority:
            max_priority = priority
            selected_move = i
    #print(arr)
    #print(max_priority)
    
    seen = set()
    duplicates = set()
    for value in arr:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)
    #print(duplicates)

    if max_priority in duplicates:
        if max_priority == arr[2]:
            selected_move = 2
        elif max_priority == arr[1]:
            selected_move = 1
        elif max_priority == arr[3]:
            selected_move = 3
        elif max_priority == arr[0]:
            selected_move = 0
        else:
            selected_move = 4

    return selected_move


# Example usage:
#right_mostplace=top &left_mostplace=bottom
one_x_mode_check=False
two_x_mode_check=False
#basket_stacks =   [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
def main(basket_stacks):
    one_x_mode_check = check_1_x_winning_condition(basket_stacks)
    two_x_mode_check = check_2_x_winning_condition(basket_stacks)
    #print(one_x_mode_check)
    #print(two_x_mode_check)


    selected_move = select_move(basket_stacks)
    #print(selected_move)

    # apply_move(basket_stacks, selected_move)

    apply_move(basket_stacks[selected_move])
    
    return basket_stacks
    #print("--->", basket_stacks)

#main(basket_stacks)