# Using a tuple (immutable) as a key
my_dict = {
    tuple(['John', 'Alice', 'Bob']): 'names',
    tuple([30, 25, 35]): 'ages',
    tuple(['New York', 'London', 'Paris']): 'cities'
}

# Displaying the dictionary
print(my_dict)
