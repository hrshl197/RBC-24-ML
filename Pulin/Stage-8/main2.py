import copy
class silo:
    def  __init__(self):
        self.state=[]
        self.possible_states=[]

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
        pass

        #Returns the best possible state from all Possible states
    def generate_heuristic_value(self):
        pass

    def generate_next_state(self):
        for i in range(5):
            self.possible_states.append(copy.deepcopy(self.enter_blue_ball(i)))
        print(self.possible_states)
    
si=silo()
si.enter_state() #Entering the initial state
si.generate_next_state() #Generating all the next possible state
print(si.state) #Printing the current state