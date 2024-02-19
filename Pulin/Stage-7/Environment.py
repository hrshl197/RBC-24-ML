import numpy as np
from IPython.display import display
import pandas as pd

class environment:

    def __init__(self):
        self.Silo_height=3 #board_height
        self.Silo_number=5 #board_width
        self.Silo_State=np.zeros([self.Silo_height, self.Silo_number], dtype=np.int8)
        self.red_score=0
        self.blue_score=0
        self.red_won_silo=0
        self.blue_won_silo=0
        self.reward=0
        self.isDone = False
        print(self.Silo_State)

    def reset(self):
        self.__init__()

    def get_available_actions(self):
        available_cols = []
        for j in range(self.Silo_number):
            if np.sum([self.Silo_State[:, j] == 0]) != 0:
                available_cols.append(j)
        return available_cols

    def check_game_done(self,player):
        if player == 'blue':
            check = '1 1 1 1'
            for j in range(self.Silo_number):
                if check in np.array_str(self.Silo_State[:, j]):
                    self.reward+=1
                    self.blue_score+=10
                    self.blue_won_silo+=1
        else:
            check = '2 2 2 2'
            for j in range(self.Silo_number):
                if check in np.array_str(self.Silo_State[:, j]):
                    self.reward+=-1
                    self.red_score+=10
                    self.red_won_silo+=1
        
        available_cols=self.get_available_actions()
        if self.red_won_silo+self.blue_won_silo==5 or available_cols==[]:
            self.isDone=True
        
        return self.reward

    def make_move(self,a,player):
        if a in self.get_available_actions():
            i = np.sum([self.Silo_State[:, a] == 0]) - 1
            if player=='blue':
                self.Silo_State[i, a] = 1
            else:
                self.Silo_State[i, a] = 2
        else:
            print('Move is invalid')
        
        return self.Silo_State.copy(), self.reward

    def render(self):
        rendered_board_state = self.board_state.copy().astype(str)
        #rendered_board_state = self.board_state.copy().astype(np.str)
        rendered_board_state[self.board_state == 0] = ' '
        rendered_board_state[self.board_state == 1] = 'O'
        rendered_board_state[self.board_state == 2] = 'X'
        display(pd.DataFrame(rendered_board_state))

env = environment()