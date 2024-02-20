class silo:
    def  __init__(self):
        self.state=[]
        self.possible_state=[]
        self.limo_state=[]

    def get_state(self):
        pass

    def enter_state(self):
        for i in range(5):
            x = list(map(int, input(f"Enter balls in Silo {i + 1} : ").split(',')))
            self.state.append(x)
            self.limo_state.append(x)
        print("Ball Arrangement in Silo : ", self.state)

    def enter_ball_red(self,silo_number):
        if 0<=silo_number<=4:
            if self.limo_state[silo_number][2] == 0 :
                for i in range(3):
                    if self.limo_state[silo_number][i] == 0:
                        self.limo_state[silo_number][i] = -1
                        break
                    else:
                        continue
            else:
                print("Silo is already filled")
        else:
            print("Error in Silo Number selection")

    def enter_ball_blue(self,silo_number):
        if 0<=silo_number<=4:
            if self.limo_state[silo_number][2] == 0 :
                for i in range(3):
                    if self.limo_state[silo_number][i] == 0:
                        self.limo_state[silo_number][i] = 1
                        break
                    else:
                        continue
            else:
                print("Silo is already filled")
        else:
            print("Error in Silo Number selection")
        print("After Enter_Blue_ball function : ",self.state)
    
    def make_move(self):
        #self.state=self.limo_state
        pass

    def generate_heuristic_value():
        pass

    def generate_next_state(self):
        for i in range(5):
            self.enter_ball_blue(i)
            print(self.limo_state)
            #self.possible_state[self.limo_state]=0
            #self.limo_state=self.state
        print(self.possible_state)

si=silo()
si.enter_state()
si.enter_ball_blue(2)
si.enter_ball_blue(2)
si.enter_ball_blue(2)
si.enter_ball_blue(2)
#si.generate_next_state()
print("Final State : ",si.state)