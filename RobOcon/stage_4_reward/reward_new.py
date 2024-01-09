from Environment import siloEnvironment as ev

class reward:
  def __init__(self):
    self.red_reward = 0
    self.blue_reward = 0
    self.bluewin = 0
    self.redwin = 0

  def reward_func(self,intial_Silo_state,final_Silo_state):

    self.bluewin = 0
    self.redwin = 0
    self.red_reward = 0
    self.blue_reward = 0

    #reward = [0,0]

    for i in final_Silo_state:
      if i == ['o','o','o'] or i == ['o','x','o'] or i == ['x','o','o']:
        self.blue_reward += 10
        self.red_reward  += -10
        self.bluewin +=1
        
      elif i == ['x','x','x'] or i == ['x','o','x'] or i == ['o','x','x']:
        self.blue_reward += -10
        self.red_reward  += 10
        self.redwin +=1

    """for j in final_Silo_state:
      if j == ['o','o','o'] or j == ['o','x','o'] or j == ['x','o','o']:
          self.bluewin +=1
      elif j == ['x','x','x'] or j == ['x','o','x'] or j == ['o','x','x']:
          self.redwin +=1"""
    
    if self.bluewin == 3:
         self.blue_reward += 100
         self.red_reward  += -100
    elif self.redwin == 3:
         self.red_reward += 100
         self.blue_reward += -100
         

    #reward = [self.blue_reward,self.red_reward]
    

    return self.blue_reward,self.red_reward

    

    



       
      

    
    

