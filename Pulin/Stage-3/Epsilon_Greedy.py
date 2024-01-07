import random

class EpsilonGreedy:
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def choose_action(self, q_values):
        if random.random() < self.epsilon:
            # Explore: Choose a random action
            return random.choice(range(len(q_values)))
        else:
            # Exploit: Choose the action with the highest Q-value
            return max(enumerate(q_values), key=lambda x: x[1])[0]