import networkx as nx
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.children = []
        self.parent = parent

# Function to recursively add nodes to the graph
def add_nodes_to_graph(graph, node):
    for child in node.children:
        graph.add_node(str(child.state))
        graph.add_edge(str(node.state), str(child.state))
        add_nodes_to_graph(graph, child)

# Create the root node
initial_state = "All silos are empty"
root = TreeNode(initial_state)

# Add child nodes to represent different game states
for i in range(5):
    team_a_state = f"Team A's state {i}"
    for j in range(5):
        team_b_state = f"Team B's state {j}"
        node = TreeNode(f"{team_a_state}, {team_b_state}", parent=root)
        root.children.append(node)
        for k in range(10):
            game_state = f"Game state {k}"
            child_node = TreeNode(game_state, parent=node)
            node.children.append(child_node)

# Create a directed graph to visualize the tree
G = nx.DiGraph()

# Add the root node and its children to the graph
G.add_node(str(root.state))
add_nodes_to_graph(G, root)

# Draw the tree
pos = nx.spring_layout(G, seed=42)
labels = nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')
nx.draw(G, pos, with_labels=False, node_size=2000, node_color="skyblue", font_size=8)
plt.show()
