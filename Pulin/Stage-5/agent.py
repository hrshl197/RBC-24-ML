import torch,random,numpy as np
from Def_Off import demo as D 
from collections import deque
from Environmen_new import siloEnvironment
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
        self.model = Linear_QNet(3, 256, 1) 
        self.trainer = QTrainer(self.model, LR, gamma=self.gamma)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE) # list of tuples
        else:
            mini_sample = self.memory

        for state, action, reward, next_state, done in mini_sample:
            self.trainer.train_step(state, action, reward, next_state, done)
        """states, actions, rewards, next_states, dones = zip(*mini_sample)
        for o in range(15):
            self.trainer.train_step(states[o], actions[o], rewards[o], next_states[o], dones[o])"""

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        # print("the value of states: ",states)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_silo_number(self,state,filled_silo_list):
        # random moves: tradeoff exploration / exploitation
        self.epsilon = 80 - self.n_games
        #silo_selected = [0,0,0,0,0]
        
        if random.randint(0, 200) < self.epsilon:#explore
            move = random.randint(0, 4)
            #silo_selected[move] = 1
            while move in filled_silo_list:
                move = random.randint(0, 4)
            print(filled_silo_list,"if selected")
            return move
        else:#exploit
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            #silo_selected[move] = 1
            print(filled_silo_list)
            temp=1
            sorted_indices = torch.argsort(prediction, descending=True)
            while move in filled_silo_list:
                if temp==4:
                    break
                move = sorted_indices[temp].item()
                temp=temp+1
            return move
            """if move in filled_silo_list:
                move = sorted_indices[temp].item()
                temp=temp+1
                if move in filled_silo_list:
                    move = sorted_indices[temp].item()
                    temp=temp+1
                    if move in filled_silo_list:
                        move = sorted_indices[temp].item()
                        temp=temp+1
                        if move in filled_silo_list:
                            move = sorted_indices[temp].item()
                            temp=temp+1
                            return move
                        return move
                    return move
                return move
            return move"""

    def take_action_blue(self,state_old,silo_selected):
        if 0<=silo_selected<=4: # Checking wheather the selected silo number is in five
            if len(state_old[silo_selected])<4: # checking wheather the silo is empty
                for i in range(len(state_old[silo_selected])):
                    if state_old[silo_selected][i] == 0:
                        state_old[silo_selected][i] = 1
                        break
            else:
                print("Silo is already filled")
        else:
            print("Error in Silo Number",silo_selected)
        return state_old
    
    def take_action_red(self,state_old,silo_selected):
        if 0<=silo_selected<=4: # Checking wheather the selected silo number is in five
            if len(state_old[silo_selected])<4: # checking wheather the silo is empty
                for i in range(len(state_old[silo_selected])):
                    if state_old[silo_selected][i] == 0:
                        state_old[silo_selected][i] = -1
                        break
            else:
                print("Silo is already filled")
        else:
            print("Error in Silo Number",silo_selected)
        return state_old

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = blueAgent()
    game = siloEnvironment()
    
    """# get old state
    state_old = game.Silo_State"""

    i=0
    j=0
    while j<20:
        # not taking this for first for loop  
        if i==0:
            # get old state
            state_old = game.Silo_State
        elif i>=1:
            state_old = state_new
        i=i+1
        
        # get list of silo which are full
        filled_silo_list = game.full_silo_list(state_old)
        # get move
        silo_selected = agent.get_silo_number(state_old,filled_silo_list)
        """silo_selected_list = agent.get_silo_number(state_old)
        for j in silo_selected_list:
            if silo_selected_list[j] == 1:
                silo_selected=j"""
        
        # perform move and get new state
        s = random.randint(0,1)
        if s==0:
            # Blue Agent
            state_new = agent.take_action_blue(state_old,silo_selected)
        elif s==1:
            # Red Agent
            temp_instance=D() # instance of Deff_off
            silo_selected=temp_instance.main(state_old)
            state_new = agent.take_action_red(state_old,silo_selected)

        game.rewardCalculate(state_new)

        # train short memory
        agent.train_short_memory(state_old,silo_selected,game.reward,state_new,game.game_Over)

        # remember
        agent.remember(state_old,silo_selected,game.reward,state_new,game.game_Over)

        #check game over condition and check winning condition
        bol = game.check_Game_Over(state_new)
        print("Round :",i,' Agent Selected :',s,"Silo Selected : ",silo_selected,"reward : ",game.reward,"\nCurrent state : ",state_new)

        if bol:
            print(i)
            i=0
            j=j+1
            # train long memory, plot result
            print("__________________________________________Game Over__________________________________________")
            print('Final State : ',state_new)
            #game.reset()
            agent.n_games+=1
            # agent.train_long_memory() TODO keeping train_long_memory out for first time running/generation of model.pth file
            
            #if game.reward>record:
            #    record=game.reward
            agent.model.save() 

            print('Game', agent.n_games, 'Score', game.reward, 'Record:', record)

            """plot_scores.append(game.reward)
            total_score += game.reward
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)"""
            game.reset()

if __name__=="__main__":
    train()