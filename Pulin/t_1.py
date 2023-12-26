from itertools import product

class SiloState:
    def __init__(self, state):
        self.state = state
        self.children = []

def generate_silo_states(silo_count, balls_per_silo, ball_types):
    def generate_states(current_state, silo_index):
        if silo_index == silo_count:
            return SiloState(current_state)

        silo_node = SiloState(current_state.copy())
        for ball_combination in product(ball_types, repeat=balls_per_silo):
            new_state = current_state.copy()
            new_state[silo_index] = list(ball_combination)
            silo_node.children.append(generate_states(new_state, silo_index + 1))

        return silo_node

    root_state = [[] for _ in range(silo_count)]
    root = generate_states(root_state, 0)
    return root

def print_silo_states(node, level=0):
    if node is not None:
        print("     " * level + str(node.state))
        for child in node.children:
            print_silo_states(child, level + 1)

# Define parameters
silo_count = 2
balls_per_silo = 3
ball_types = ["X", "0"]  # Add more colors as needed

# Generate and print the tree of all possible silo states
silo_states_tree = generate_silo_states(silo_count, balls_per_silo, ball_types)
print_silo_states(silo_states_tree)
