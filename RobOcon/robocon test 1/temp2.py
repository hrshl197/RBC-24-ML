from collections import deque

class SiloState:
    def __init__(self, state):
        self.state = state
        self.children = []

def print_silo_states(node, level=0):
    if node is not None:
        print("  " * level + str(node.state))
        for child in node.children:
            print_silo_states(child, level + 1)

def generate_silo_states(baskets, max_depth):
    root = SiloState(baskets)
    queue = deque([(root, 0)])

    while queue:
        current_node, depth = queue.popleft()

        if depth < max_depth:
            for i, basket in enumerate(current_node.state):
                # Add a red ball
                new_baskets = current_node.state.copy()
                new_basket = new_baskets[i] + ['R']
                new_baskets[i] = new_basket
                child_node = SiloState(new_baskets)
                current_node.children.append(child_node)
                queue.append((child_node, depth + 1))

                # Add a blue ball
                if len(basket) < 3:
                    new_baskets = current_node.state.copy()
                    new_basket = new_baskets[i] + ['B']
                    new_baskets[i] = new_basket
                    child_node = SiloState(new_baskets)
                    current_node.children.append(child_node)
                    queue.append((child_node, depth + 1))

    return root

# Initial state: 5 empty baskets
initial_state = [[] for _ in range(5)]

# Generate and print the tree of all possible silo states
silo_states_tree = generate_silo_states(initial_state, max_depth=14)
print_silo_states(silo_states_tree)
