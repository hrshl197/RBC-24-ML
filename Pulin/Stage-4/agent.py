import torch,random,numpy as np
from Def_Off import demo as D 
from collections import deque
from Environment import siloEnvironment
from model import Linear_QNet, QTrainer
from helper import plot

MAX_MEMORY=100_000_000
BATCH_SIZE=1000
LR=0.001

class blueAgent:
    def __init__(self):
        # Initialize your agent's parameters and policy here
        self.n_games=0
        self.epsilon=0 # control the randomness
        self.gamma=0.9 # discount rate
        self.memory=deque(maxlen=MAX_MEMORY) # pop from left is max memory get full 
        self.model = Linear_QNet(3, 256, 5) 
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

    def get_silo_number(self,state):
        # random moves: tradeoff exploration / exploitation
        self.epsilon = 80 - self.n_games
        # final_move = [0,0,0,0,0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 4)
            # final_move[move] = 1
        else:
            #state0 = torch.tensor(state, dtype=torch.float)
            state0 = torch.tensor([[float(item) if item else 0.0 for item in inner_list] for inner_list in state], dtype=torch.float32)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            #final_move[move] = 1

        return move

    def take_action(self,state_old,final_move):
        if 0<=final_move<=4: # Checking wheather the selected silo number is in five
            if len(state_old[final_move])<4: # checking wheather the silo is empty
                for i in range(len(state_old[final_move])):
                    if state_old[final_move][i] == '':
                        state_old[final_move][i] = '0'
                        break
            else:
                print("Silo is already filled")
        else:
            print("Error in Silo Number")
        return state_old

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = blueAgent()
    game = siloEnvironment()
    
    # get old state
    state_old = game.Silo_State
    tensor_state_old = torch.tensor([[float(item) if item else 0.0 for item in inner_list] for inner_list in state_old], dtype=torch.float32)
    # tensor_state_old = torch.tensor([[float(item) for item in inner_list] for inner_list in state_old], dtype=torch.float32)

    while True:
        
        i=0
        if i>=1:
            state_old = state_new
            tensor_state_old = torch.tensor([[float(item) if item else 0.0 for item in inner_list] for inner_list in state_old], dtype=torch.float32)
        
        # get move
        final_move =agent.get_silo_number(state_old)
        
        s = random.randint(0,1)
        if s==0:
            # perform move and get new state
            state_new = agent.take_action(state_old,final_move)
        elif s==1:
            temp_instance=D() 
            state_new=temp_instance.main(state_old)

        game.rewardCalculate(state_old,state_new,final_move)
        tensor_state_new = torch.tensor([[float(item) if item else 0.0 for item in inner_list] for inner_list in state_new], dtype=torch.float32)
        # tensor_state_new = torch.tensor([[float(item) for item in inner_list] for inner_list in state_new], dtype=torch.float32)


        # train short memory
        agent.train_short_memory(tensor_state_old,final_move,game.reward,tensor_state_new,game.game_Over)

        # remember
        agent.remember(tensor_state_old,final_move,game.reward,tensor_state_new,game.game_Over)
        print("One round completed")
        
        if game.game_Over:
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
        i=i+1

if __name__=="__main__":
    train()