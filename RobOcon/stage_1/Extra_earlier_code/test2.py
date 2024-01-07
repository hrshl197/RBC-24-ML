def print_state_space_tree(baskets, max_depth):
    stack = [(baskets, 0)]

    while stack:
        current_baskets, depth = stack.pop()

        for i, basket in enumerate(current_baskets):
            # Add a red ball
            new_basket = basket + ['R']
            new_baskets = current_baskets[:i] + [new_basket] + current_baskets[i+1:]
            print(f"Depth {depth + 1} - Add red ball to Basket {i + 1}: {new_baskets}")

            if depth + 1 < max_depth:
                stack.append((new_baskets, depth + 1))

            # Add a blue ball
            if len(basket) < 3:
                new_basket = basket + ['B']
                new_baskets = current_baskets[:i] + [new_basket] + current_baskets[i+1:]
                print(f"Depth {depth + 1} - Add blue ball to Basket {i + 1}: {new_baskets}")

                if depth + 1 < max_depth:
                    stack.append((new_baskets, depth + 1))

# Initial state: 5 empty baskets
initial_state = [[] for _ in range(5)]

# Print state space tree up to a certain depth
print_state_space_tree(initial_state, max_depth=2)
