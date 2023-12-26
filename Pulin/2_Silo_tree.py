class StateNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []

    def add_child(self, child_state):
        child_node = StateNode(child_state, parent=self)
        self.children.append(child_node)
        return child_node

def print_state_space_tree(node, level=0):
    print("     " * level + str(node.state))
    for child in node.children:
        print_state_space_tree(child, level + 1)

# Example usage:
initial_state = [["","",""],["","",""],["","",""],["","",""],["","",""]]
root = StateNode(initial_state)

child_state_B1 = [["","","O"],["","",""],["","",""],["","",""],["","",""]]
child_state_C1 = [["","",""],["","","O"],["","",""],["","",""],["","",""]]
child_state_D1 = [["","",""],["","",""],["","","O"],["","",""],["","",""]]
child_state_E1 = [["","",""],["","",""],["","",""],["","","O"],["","",""]]
child_state_F1 = [["","",""],["","",""],["","",""],["","",""],["","","O"]]
child_state_B2 = [["","","X"],["","",""],["","",""],["","",""],["","",""]]
child_state_C2 = [["","",""],["","","X"],["","",""],["","",""],["","",""]]
child_state_D2 = [["","",""],["","",""],["","","X"],["","",""],["","",""]]
child_state_E2 = [["","",""],["","",""],["","",""],["","","X"],["","",""]]
child_state_F2 = [["","",""],["","",""],["","",""],["","",""],["","","X"]]

node_B1 = root.add_child(child_state_B1)
node_C1 = root.add_child(child_state_C1)
node_D1 = root.add_child(child_state_D1)
node_E1 = root.add_child(child_state_E1)
node_F1 = root.add_child(child_state_F1)
node_B2 = root.add_child(child_state_B2)
node_C2 = root.add_child(child_state_C2)
node_D2 = root.add_child(child_state_D2)
node_E2 = root.add_child(child_state_E2)
node_F2 = root.add_child(child_state_F2)

#node_G1 = node_B1.add_child(child_state_G1)


print_state_space_tree(root)