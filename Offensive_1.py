
"""
def apply_move(basket_stack):
    for i in basket_stack:
        if basket_stack[i] == '':
            basket_stack[i] = 'o'
            return
"""

def apply_move(basket_stack):
    for i, ball in enumerate(basket_stack):
        if ball == '':
            basket_stack[i] = 'o'
            return

def evaluate_priority(basket):
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
basket_stacks = [['x', 'o', ''], ['x', 'o', ''], ['x', 'o', 'o'], ['o', 'o', 'o'], ['x', 'x', 'o']]

selected_move = select_move(basket_stacks)
print(selected_move)

#apply_move(basket_stacks, selected_move)

apply_move(basket_stacks[selected_move])

print("Next state of basket stacks:", basket_stacks)
