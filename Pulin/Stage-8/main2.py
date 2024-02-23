import copy
from Def_Off import demo as do

class silo:
    def  __init__(self):
        self.state=[]
        self.possible_states=[]
        self.score_array=[]

    #Get Silo state from CV
    def get_state(self):
        pass

    #Enter the Silo State manually
    def enter_state(self):
         for i in range(5):
            x = list(map(int, input(f"Enter balls in Silo {i + 1} : ").split(',')))
            self.state.append(copy.deepcopy(x))

    def enter_red_ball(self,silo_number):
        temp_state = copy.deepcopy(self.state)
        if 0<=silo_number<=4:
            if temp_state[silo_number][2] == 0 :
                for i in range(3):
                    if temp_state[silo_number][i] == 0:
                        temp_state[silo_number][i] = -1
                        return temp_state
                    else:
                        continue
            else:
                print("Silo is already filled")
                return temp_state
        else:
            print("Error in Silo Number selection")
            return temp_state

    def enter_blue_ball(self,silo_number):
        temp_state = copy.deepcopy(self.state)
        if 0<=silo_number<=4:
            if temp_state[silo_number][2] == 0 :
                for i in range(3):
                    if temp_state[silo_number][i] == 0:
                        temp_state[silo_number][i] = 1
                        return temp_state
                    else:
                        continue
            else:
                print("Silo is already filled")
                return temp_state
        else:
            print("Error in Silo Number selection")
            return temp_state
    
    #Finalize the move by changing the state with the value passed in it 
    def make_move(self,best_state):
        self.state = best_state

        #Returns the best possible state from all Possible states
    def generate_heuristic_value(self):
        self.score_array=[]
        hv = do()
        hv.two_o_mode_check=hv.check_2_o_winning_condition
        for i in range(5):
            score=0
            for basket in self.possible_states[i]:
                priority = hv.evaluate_priority(basket)
                score+=priority
            self.score_array.append(score)

    #Select the next state
    def select_state(self):
        max_score=self.score_array.index(max(self.score_array))
        self.make_move(self.possible_states[max_score])

    def generate_next_state(self):
        self.possible_states=[]
        for i in range(5):
            self.possible_states.append(copy.deepcopy(self.enter_blue_ball(i)))
        print(self.possible_states)
    
si=silo()
si.enter_state() #Entering the initial state
si.generate_next_state() #Generating all the next possible state
si.generate_heuristic_value()
print(si.state) #Printing the current state
print(si.score_array)
si.select_state()
si.generate_next_state() #Generating all the next possible state
si.generate_heuristic_value()
print(si.state) 
print(si.score_array)