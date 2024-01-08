import torch
import random
from collections import deque
from Epsilon_Greedy import EpsilonGreedy as eg
from Environment import siloEnvironment as ev 
import numpy as np

MAX_MEMORY=100_000_000

class RLAgent:
    def __init__(self, state_space_size, action_space_size):
        # Initialize your agent's parameters and policy here
        self.n_games=0
        self.epsilon=0 # control the randomness
        self.gamma=0 # discount rate
        self.memory=deque(maxlen=MAX_MEMORY) # pop from left is max memory get full 
        self.model = None # waiting for model
        self.trainer = None # waiting for model

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self, state, action, reward, next_state, done):
        pass

    """def get_action(self, state):
        pass

    def get_state(self, game):
        pass"""

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = RLAgent()
    game = ev()
    while True:
        game.step()
        # get old state
        state_old = 

        # get move
        final_move =

        # perform move and get new state
        state_new =
        
        # train short memory

        # remember

        if game.is_done:
            # train long memory, plot result
