import random
import math

class GameState:
    def __init__(self, num_baskets=5, max_balls=3):
        self.num_baskets = num_baskets
        self.max_balls = max_balls
        self.state = [[None] * max_balls for _ in range(num_baskets)]  # Represents the state of baskets

    def get_legal_moves(self):
        legal_moves = []
        for basket in range(self.num_baskets):
            if len(self.state[basket]) < self.max_balls:
                legal_moves.append(basket)
        return legal_moves

    def is_game_over(self):
        for basket in range(self.num_baskets):
            if len(self.state[basket]) >= 2 and self.state[basket][-1] == 'blue':
                return True
        return False

    def execute_move(self, basket):
        if basket in self.get_legal_moves():
            self.state[basket].append('blue')
            if len(self.state[basket]) > 1:
                self.state[basket][-2] = 'red'  # Set the lower ball to red
            return True
        return False

    def get_winner(self):
        for basket in range(self.num_baskets):
            if len(self.state[basket]) >= 2 and self.state[basket][-1] == 'blue':
                return 'blue'
        return 'red'

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0

def mcts_search(state, num_simulations=1000):
    root = Node(state)

    for _ in range(num_simulations):
        node = root
        while not node.state.is_game_over() and not node.children:
            node = expand(node)

        if node.state.is_game_over():
            result = 1 if node.state.get_winner() == 'blue' else 0
        else:
            result = simulate(node.state)

        backpropagate(node, result)

    best_child = max(root.children, key=lambda x: x.visits)
    return best_child.state

def expand(node):
    legal_moves = node.state.get_legal_moves()
    if not legal_moves:
        return node

    chosen_move = random.choice(legal_moves)
    child_state = node.state.clone()
    child_state.execute_move(chosen_move)
    child_node = Node(child_state, parent=node)
    node.children.append(child_node)
    return child_node

def simulate(state):
    while not state.is_game_over():
        legal_moves = state.get_legal_moves()
        chosen_move = random.choice(legal_moves)
        state.execute_move(chosen_move)
    return 1 if state.get_winner() == 'blue' else 0

def backpropagate(node, result):
    while node:
        node.visits += 1
        node.value += result
        node = node.parent
        result = 1 - result

if __name__ == "__main__":
    initial_state = GameState()

    while not initial_state.is_game_over():
        initial_state = mcts_search(initial_state)

    winner = initial_state.get_winner()
    print(f"The winner is {winner}")
