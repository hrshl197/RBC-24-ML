"""
def apply_move(basket_stack):
    for i in basket_stack:
        if basket_stack[i] == '':
            basket_stack[i] = 'o'
            return
"""


def check_winning_condition(basket_stacks):
    for i in range(len(basket_stacks) - 1):
        if basket_stacks[i][-1] == 'x' and basket_stacks[i].count('x') >= 2 and \
                basket_stacks[i + 1][-1] == 'x' and basket_stacks[i + 1].count('x') >= 2:
            return True
    return False


def evaluate_priority(basket):
    if check_winning_condition(basket_stacks):
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
            return 0  # Default priority for other states
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
            return 0  # Default priority for other states


def apply_move(basket_stack):
    for i, ball in enumerate(basket_stack):
        if ball == '':
            basket_stack[i] = 'o'
            return


def select_move(basket_stacks):
    max_priority = 0
    selected_move = None

    for i, basket in enumerate(basket_stacks):
        priority = evaluate_priority(basket)
        if priority > max_priority:
            max_priority = priority
            selected_move = i

    return selected_move


# Example usage:
#right_mostplace=top &left_mostplace=bottom

basket_stacks =  [['o', 'x', 'o'], ['x', 'x', 'x'], ['o', 'o', ''], ['o', 'o', 'o'], ['x', 'x', 'x']]

selected_move = select_move(basket_stacks)
print(selected_move)

# apply_move(basket_stacks, selected_move)

apply_move(basket_stacks[selected_move])

print("Next state of basket stacks:", basket_stacks)