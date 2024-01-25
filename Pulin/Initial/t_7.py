class SiloGame:
    def __init__(self):
        self.state = [["", "", ""], ["", "", "O"], ["", "", "X"], ["", "O", "O"], ["", "X", "O"], ["", "O", "X"],
                      ["", "X", "X"], ["O", "O", "O"], ["X", "O", "O"], ["O", "X", "O"], ["X", "X", "O"],
                      ["O", "O", "X"], ["X", "O", "X"], ["O", "X", "X"], ["X", "X", "X"]]
        self.Total_Silo = 5
        self.init_list = []
        self.verify_list = []
        self.index_list = []
        self.next_state = []
        for i in range(self.Total_Silo):
            x = list(map(str, input(f"Enter balls in Silo {i + 1} : ").split(',')))
            self.init_list.append(x)
        print(f"Ball Arrangement in Silo : ", self.init_list)

    def verify_input_states(self):
        j = 0
        for i in range(self.Total_Silo):
            for sublist in self.state:
                if sublist == self.init_list[i]:
                    self.verify_list.append(sublist)
                    j += 1
                    # Generating the index_list
                    index = self.state.index(sublist)
                    self.index_list.append(index)
        print("All valid State of input are : ", self.verify_list)
        if j == self.Total_Silo:
            print("All Input State of Silo are valid")
        else:
            print("There is an invalid State in input")

    def calculate_next_state(self):
        cal_list = list(map(lambda x: x + 1, self.index_list)) 

        ball = input("Enter the type of ball you want to insert : ")
        Silo_number = int(input("Enter the silo number in which you want to enter the ball :  "))

        number = cal_list[Silo_number - 1]
        if 8 <= number <= 15:
            print("The silo is already full")
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

        print("Next state is : ", self.next_state)


# usage
silo_game_instance = SiloGame()
# silo_game_instance.take_silo_input()
silo_game_instance.verify_input_states()
silo_game_instance.calculate_next_state()
