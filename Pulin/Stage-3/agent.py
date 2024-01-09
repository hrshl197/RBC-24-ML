import torch
import random
from collections import deque
from Epsilon_Greedy import EpsilonGreedy as eg
from Environment import siloEnvironment as ev 
import numpy as np
from model import Linear_QNet, QTrainer
from helper import plot

MAX_MEMORY=100_000_000
BATCH_SIZE=1000
LR=0.001

class RLAgent:
    def __init__(self):
        # Initialize your agent's parameters and policy here
        self.n_games=0
        self.epsilon=0 # control the randomness
        self.gamma=0.9 # discount rate
        self.memory=deque(maxlen=MAX_MEMORY) # pop from left is max memory get full 
        self.model = Linear_QNet(11, 256, 3) 
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE) # list of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

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
        state_old = game.previous_Silo_State

        # get move
        final_move =game.Silo_number

        # perform move and get new state
        state_new =game.new_Silo_State
        
        # train short memory
        agent.train_short_memory(state_old,final_move,game.reward,state_new,game.is_done)

        # remember
        agent.remember(state_old,final_move,game.reward,state_new,game.is_done)

        if game.is_done:
            # train long memory, plot result
            print('Final State : ',state_new)
            game.reset()
            agent.n_games+=1
            agent.train_long_memory()
            
            if game.reward>record:
                record=game.reward
                agent.model.save() 

            print('Game', agent.n_games, 'Score', game.reward, 'Record:', record)

            plot_scores.append(game.reward)
            total_score += game.reward
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)

if __name__=="__main__":
    train()