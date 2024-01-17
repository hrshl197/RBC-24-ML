class reward:
  def __init__(self):
    self.red_reward = 0
    self.blue_reward = 0
    self.bluewin = 0
    self.redwin = 0

  def reward_func(self,final_Silo_state,Silo_number,agent):

    reward = 0

    for j in final_Silo_state:
      if j == ['0','0','0'] or j == ['0','1','0'] or j == ['1','0','0']:
          self.bluewin +=1
      elif j == ['1','1','1'] or j == ['1','0','1'] or j == ['0','1','1']:
          self.redwin +=1    

    i = final_Silo_state[Silo_number]

    if agent == 0:
      if i == ['0','0','0'] or i == ['0','1','0'] or i == ['1','0','0']:
        self.blue_reward += 10
      """elif i == ['1','1','1'] or i == ['1','0','1'] or i == ['0','1','1']:
        self.blue_reward += -10"""

      if self.bluewin == 3:
         self.blue_reward += 100
      """elif self.redwin == 3:
         self.blue_reward += -100"""
      
      reward = self.blue_reward
      self.blue_reward = 0
    else:
      """if i == ['0','0','0'] or i == ['0','1','0'] or i == ['1','0','0']:
        self.red_reward += -10"""
      if i == ['1','1','1'] or i == ['1','0','1'] or i == ['0','1','1']:
        self.red_reward += 10

      """if self.bluewin == 3:
         self.red_reward += -100"""
      if self.redwin == 3:
         self.red_reward += 100     

      reward = self.red_reward
      self.red_reward = 0

    return reward

    

    



       
      

    
    

