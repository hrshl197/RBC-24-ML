from Def_Off_2 import main as m
import copy

x=1
state = [[],["","",""],["o","",""],["x","",""],["o","o",""],["o","x",""],["x","o",""],["x","x",""],["o","o","o"],["o","o","x"],["o","x","o"],["o","x","x"],["x","o","o"],["x","o","x"],["x","x","o"],["x","x","x"]]
file_path = r'E:\RBC-24-ML\Pulin\Stage-9\use_output_1.txt'
with open(file_path, 'r') as file:
    for line in file:
        my_list = line.split(",")
        my_list = [int(item) for item in my_list]
        use_list=[]
        initial_state=[]
        #print(my_list)
        for i in range(5):
            temp=state[my_list[i]]
            use_list.append(copy.deepcopy(temp))
        
        #print("use list : " ,use_list)
        temp_list=copy.deepcopy(use_list)
        #print("temp_list: ",temp_list)
        next_state=m(temp_list)
        #print(next_state)
        print(x,".",use_list," ---> ",next_state)
        x+=1
        
