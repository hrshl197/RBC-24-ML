import torch

class Linear_QNet(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = torch.nn.Linear(input_size, hidden_size)
        self.linear2 = torch.nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.nn.functional.relu(self.linear1(x))
        x = self.linear2(x)
        return x

def update_q_value(q_values, state, action, reward, next_state, alpha, gamma):
    current_q_value = q_values[state][action]
    max_next_q_value = max(q_values[next_state])
    
    td_error = reward + gamma * max_next_q_value - current_q_value
    updated_q_value = current_q_value + alpha * td_error

    q_values[state][action] = updated_q_value

    return q_values

# Create an instance of the Linear_QNet
input_size = 3
hidden_size = 256
output_size = 5
q_net = Linear_QNet(input_size, hidden_size, output_size)

# Create an example input tensor
input_tensor = torch.tensor([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9],
                             [10, 11, 12],
                             [13, 14, 15]], dtype=torch.float32)  # Example batch size of 1
input_tensor = input_tensor.unsqueeze(0)

# Predict Q-values
q_values = q_net(input_tensor)

# Print the predicted Q-values
print("Initial Q-values:")
print(q_values)

# Example Q-value update
state = [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]]  # Example current state index
action = [0,0,1,0,0]  # Example action index
reward = 1.0  # Example immediate reward
next_state = 1  # Example next state index
alpha = 0.1  # Example learning rate
gamma = 0.9  # Example discount factor

# Update Q-values
q_values_updated = update_q_value(q_values.tolist(), state, action, reward, next_state, alpha, gamma)

# Print the updated Q-values
print("Updated Q-values:")
print(q_values_updated)
