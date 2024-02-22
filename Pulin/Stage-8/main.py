import copy
class silo:
    def  __init__(self):
        self.state=[]
        self.possible_state=[]
        self.temp_state=[]

    #Get Silo state from CV
    def get_state(self):
        pass
    
    #Enter the Silo State manually
    def enter_state(self):
        for i in range(5):
            x = list(map(int, input(f"Enter balls in Silo {i + 1} : ").split(',')))
            self.state.append(copy.deepcopy(x))
            self.temp_state.append(copy.deepcopy(x))
            """self.state.append(x)
            self.temp_state.append(x)"""
        print("Ball Arrangement in Silo : ", self.state)
        #self.temp_state=self.state.copy()

    def enter_ball_red(self,silo_number):
        if 0<=silo_number<=4:
            if self.temp_state[silo_number][2] == 0 :
                for i in range(3):
                    if self.temp_state[silo_number][i] == 0:
                        self.temp_state[silo_number][i] = -1
                        break
                    else:
                        continue
            else:
                print("Silo is already filled")
        else:
            print("Error in Silo Number selection")
        print("After Enter_Red_ball function : ",self.temp_state)

    def enter_ball_blue(self,silo_number):
        if 0<=silo_number<=4:
            if self.temp_state[silo_number][2] == 0 :
                for i in range(3):
                    if self.temp_state[silo_number][i] == 0:
                        self.temp_state[silo_number][i] = 1
                        break
                    else:
                        continue
            else:
                print("Silo is already filled")
        else:
            print("Error in Silo Number selection")
        print("After Enter_Blue_ball function : ",self.temp_state)
    
    def make_move(self):
        #self.state=self.temp_state
        pass

    def generate_heuristic_value():
        pass

    def generate_next_state(self):
        for i in range(5):
            self.enter_ball_blue(i)
            print(self.temp_state)
            self.possible_state.append(self.temp_state)
            """key = tuple(map(tuple, self.temp_state))
            self.possible_state[key] = 0"""
        print(self.possible_state)

si=silo()
si.enter_state()
si.enter_ball_blue(2)
#si.enter_ball_blue(2)
#si.enter_ball_blue(2)
#si.enter_ball_blue(2)
si.generate_next_state()
print("Final State : ",si.state)
print("Limbo State : ",si.temp_state)
print("Possible State : ",si.possible_state)