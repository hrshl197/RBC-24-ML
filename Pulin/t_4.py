def generate_list_states(current_state, index, max_value, result):
    if index == len(current_state):
        result.append(current_state.copy())
        return

    for value in range(1, max_value + 1):
        current_state[index] = value
        generate_list_states(current_state, index + 1, max_value, result)

def print_list_states(states):
    i=1
    for state in states:
        print(state,i)
        i=i+1

# Define parameters
list_length = 5
max_value = 15

# Generate all possible states of the list
initial_state = [0] * list_length
all_states = []
generate_list_states(initial_state, 0, max_value, all_states)

# Print all possible states
print_list_states(all_states)

