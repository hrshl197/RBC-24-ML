from collections import deque
from graphviz import Digraph

class SiloState:
    def __init__(self, state):
        self.state = state
        self.children = []

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

def visualize_silo_states(node, dot=None, level=0, parent_name=None, child_name=None):
    if dot is None:
        dot = Digraph(comment='Silo State Tree')

    dot.node(str(parent_name), str(node.state))

    for i, child in enumerate(node.children):
        new_child_name = f"{child_name}_{i}" if child_name else str(i)
        dot.node(new_child_name, str(child.state))
        dot.edge(str(parent_name), new_child_name)
        visualize_silo_states(child, dot=dot, level=level + 1, parent_name=new_child_name)

    return dot


# Initial state: 5 empty baskets
initial_state = [[] for _ in range(5)]

# Generate the tree of all possible silo states
silo_states_tree = generate_silo_states(initial_state, max_depth=4)

# Visualize the tree and save it to a file (e.g., 'silo_state_tree')
dot = visualize_silo_states(silo_states_tree)
dot.render('silo_state_tree', format='png', cleanup=True)
