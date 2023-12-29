from Def_Off import demo as do

class SiloGame:
    def __init__(self):
        self.state = [
            ["", "", ""], ["o", "", ""], ["x", "", ""], ["o", "o", ""], ["o", "x", ""],
            ["x", "o", ""], ["x", "x", ""], ["o", "o", "o"], ["o", "o", "x"], ["o", "x", "o"],
            ["o", "x", "x"], ["x", "o", "o"], ["x", "o", "x"], ["x", "x", "o"], ["x", "x", "x"]
        ]
        self.init_list = [["x", "", ""],["", "", ""],["", "", ""],["", "", ""],["", "", ""]]
        self.buffer = []
        self.Total_Silo = 5
        self.var = 0

    def state_selector(self, s):
        if self.verfiy_state(s)==1:
            self.var = 0
            return 1
        else:
            return 0
        
    def verfiy_state(self, s):
        j = 0
        for i in range(self.Total_Silo):
            for sublist in self.state:
                if sublist == s[i]:
                    j += 1
        if j == self.Total_Silo:
            return 1
        else:
            return 0
                    

    def verify_index_generater(self):
        j = 0
        self.index_list = []
        for i in range(self.Total_Silo):
            for sublist in self.state:
                if sublist == self.init_list[i]:
                    j += 1
                    index = self.state.index(sublist)
                    self.index_list.append(index)
        if j == self.Total_Silo:
            return 1
        else:
            return 0

    def calculate_next_state(self, ball, Silo_number):
        self.next_state = []
        cal_list = list(map(lambda x: x + 1, self.index_list)) 
        number = cal_list[Silo_number - 1]
        
        if 8 <= number <= 15:
            print("The silo is already full")
            return
        elif number >= 15 or number <= 0:
            print("An error occurred")
        elif ball.lower() == 'x':
            number = (2 * number) + 1
        elif ball.lower() == 'o':
            number = 2 * number
        else:
            print("Invalid Input error")

        cal_list[Silo_number - 1] = number
        self.index_list = list(map(lambda y: y - 1, cal_list))

        for i in range(self.Total_Silo):
            self.next_state.append(self.state[self.index_list[i]])
        print(f"State {self.var+1} is : ", self.next_state)
        self.var += 1
        self.buffer.append(self.next_state)

    def nxt_level_print(self):
        if self.verify_index_generater() == 1:
            for i in range(5):
                self.calculate_next_state('O', i+1)
                self.verify_index_generater()
            for i in range(5):        
                self.calculate_next_state('X', i+1)
                self.verify_index_generater()
        else:
            print("There's an error in initial state initialization of Silos ")

# usage
silo_game_instance = SiloGame()
Def_Off_instance = do()
silo_game_instance.nxt_level_print()
for i in range(100):
    # s = int(input("Enter the next state number to descend: "))
    s = Def_Off_instance.main(silo_game_instance.init_list)
    print()
    if silo_game_instance.state_selector(s) == 1:
        silo_game_instance.nxt_level_print()
    else:
        print("Error in state input")
 