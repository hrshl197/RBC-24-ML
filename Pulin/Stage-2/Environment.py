from Blue import demo as bdo
from Red import demo as rdo
from random import randint

class Environment:
    def __init__(self):
        self.Silos_State=[["", "", ""],["", "", ""],["", "", ""],["", "", ""],["", "", ""]]

    def push_blue(self,temp):
        if 0<=temp<=4:
            if len(self.Silos_State[temp])<3:
                self.Silos_State[temp].append('o')
            else:
                print("blue : Silo is already filled")
        else:
            print("Error in Silo Number Generation")

    def push_red(self,temp):
        if 0<=temp<=4:
            if len(self.Silos_State[temp])<3:
                self.Silos_State[temp].append('x')
            else:
                print("red : Silo is already filled")
        else:
            print("Error in Silo Number Generation")

    def select_agent(self):
        s = randint(0,9)
        print("Random generated number is : ",s)
        if s%2==0:
            self.Blue_instance=bdo()
            Silo_number=self.Blue_instance.main(self.Silos_State)
            self.push_blue(Silo_number)
        elif s%2!=0:
            self.Red_instance=rdo()
            Silo_number=self.Red_instance.main(self.Silos_State)
            self.push_red(Silo_number)
        else:
            print("Error in agent selsction")

    def state_print(self):
        print(self.Silos_State)
    
    def win_condition(self):
        pass

    def reset(self):
        pass

game_instance=Environment()
for i in range(20):
    game_instance.select_agent()
    game_instance.state_print()