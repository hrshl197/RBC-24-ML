def generate_list_states(current_state, index, max_value, result):
    if index == len(current_state):
        result.append(current_state.copy())
        return

    for value in range(1, max_value + 1):
        current_state[index] = value
        generate_list_states(current_state, index + 1, max_value, result)

def print_list_states(states):
    k=1
    for state in states:
        print(k,":-",state)
        k=k+1

# Define parameters
list_length = 5
max_value = 15

# Generate all possible states of the list
initial_state = [0] * list_length

statex = [
            ["","",""],
            ["o","",""],
            ["x","",""],
            ["o","o",""],
            ["o","x",""],
            ["x","o",""],
            ["x","x",""],
            ["o","o","o"],
            ["o","o","x"],
            ["o","x","o"],
            ["o","x","x"],
            ["x","o","o"],
            ["x","o","x"],
            ["x","x","o"],
            ["x","x","x"]
        ]

all_states = []

generate_list_states(initial_state, 0, max_value, all_states)
print(len(all_states))

for i in range(0,len(all_states)):
    for j in range(0,list_length):
        for k in range(1,max_value+1):
            if all_states[i][j] == k:
                all_states[i][j] = statex[k-1]

# Print all possible states
print_list_states(all_states)