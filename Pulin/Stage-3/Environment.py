from random import randint
from Epsilon_Greedy import EpsilonGreedy as eg

class siloEnvironment:
    def __init__(self):
        self.Silo_State=[["", "", ""],["", "", ""],["", "", ""],["", "", ""],["", "", ""]]
        self.q_values=[0.1,0.1,0.1,0.1,0.1] # temporaray for checking 
        self.red_won_silo=0
        self.blue_won_silo=0
        self.total_balls=0
        self.reward=0
        self.epsilon=0 # temporary completely wrong
        self.is_done=False
        
    def reset(self):
        self.Silo_State=[["", "", ""],["", "", ""],["", "", ""],["", "", ""],["", "", ""]]
        self.red_won_silo=0
        self.blue_won_silo=0
        self.total_balls=0
        self.reward=0
        self.is_done=False

    def step(self):
        # Perform an action and return the new state, reward, and whether the game is done
        # select agent either blue or red
        s = randint(0,1)
        self.EG = eg(self.epsilon)
        if s==0:
            print("Blue agent selected")
            self.Silo_number=self.EG.choose_action(self.q_values)
        elif s==1:
            print("Red agent selected")
            self.Silo_number=self.EG.choose_action(self.q_values)
        else:
            print("Error in agent selsction")
        
        self.previous_Silo_State=self.Silo_State

        # put the ball in silo 
        if 0<=self.Silo_number<=4: # Checking wheather the selected silo number is in five
            if len(self.Silo_State[self.Silo_number])<4: # checking wheather the silo is empty
                for i in range(len(self.Silo_State[self.Silo_number])):
                    if s==0:
                        if self.Silo_State[self.Silo_number][i] == '':
                            self.Silo_State[self.Silo_number][i] = 'o'
                            break
                    elif s==1:
                        if self.Silo_State[self.Silo_number][i] == '':
                            self.Silo_State[self.Silo_number][i] = 'x'
                            break
            else:
                print("Silo is already filled")
        else:
            print("Error in Silo Number")

        self.new_Silo_State=self.Silo_State

        # TODO Generate Reward here generated from reward file 
        # self.reward=reward_func(self,previous_Silo_Stat,new_Silo_State,self.Silo_number,s)

        # Checking the winning condition 
        for i in self.Silo_State:
            if i == ['o','o','o'] or i == ['o','x','o'] or i == ['x','o','o']:
                self.blue_won_silo+=1
            elif i == ['x','x','x'] or i == ['x','o','x'] or i == ['o','x','x']:
                self.red_won_silo+=1

        # Checking wheather all the silo are full or not
        for i, ball in enumerate(self.Silo_State):
            if ball != '':
                self.total_balls+=1

        if self.blue_won_silo==3 or self.red_won_silo==3 or self.total_balls==15:
            # self.reset()
            self.is_done=True
        
        # Putting all this variable back to zero for rechecking of win condition and reset condition
        self.blue_won_silo=0
        self.red_won_silo=0
        self.total_balls=0
        