from reward import reward as r
class siloEnvironment:
    def __init__(self):
        self.Silo_State=[["", "", ""],["", "", ""],["", "", ""],["", "", ""],["", "", ""]]
        self.red_won_silo=0
        self.blue_won_silo=0
        self.total_balls=0
        self.reward=0
        self.game_Over = False
 
    def reset(self):
        self.Silo_State=[["", "", ""],["", "", ""],["", "", ""],["", "", ""],["", "", ""]]
        self.red_won_silo=0
        self.blue_won_silo=0
        self.total_balls=0
        self.reward=0
        self.game_Over=False

    def check_Win_Condition(self):
        for i in self.Silo_State:
            if i == ['0','0','0'] or i == ['0','1','0'] or i == ['1','0','0']:
                self.blue_won_silo+=1
            elif i == ['1','1','1'] or i == ['1','0','1'] or i == ['0','1','1']:
                self.red_won_silo+=1
        if self.blue_won_silo==3 or self.red_won_silo==3 or self.total_balls==15:
            self.GameOver=True
        self.blue_won_silo=0
        self.red_won_silo=0

    def check_Game_Over(self):
        if self.game_Over:
            self.reset()

    def rewardCalculate(self,state_old,state_new,final_move):
        rewd=r()
        self.reward=rewd.reward_func(state_new,final_move,0)
