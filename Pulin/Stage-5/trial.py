import torch

# Create a tensor (replace this with your actual tensor)
my_tensor = torch.tensor([[3, 8, 5, 12, 7]])
my_tensor=my_tensor.squeeze()
# Use PyTorch functions to find the index of the second highest number
sorted_indices = torch.argsort(my_tensor, descending=True)
second_highest_index = sorted_indices[2]

# Print the result
print("Index of the second highest number:", second_highest_index.item())